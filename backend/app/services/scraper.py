import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException

def scrape_url(url: str) -> str:
    """Extract article text from a given URL."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        # Check content type to avoid trying to parse images/pdfs
        content_type = response.headers.get('Content-Type', '').lower()
        if 'text/html' not in content_type:
            raise HTTPException(status_code=400, detail=f"Unsupported content type: {content_type}. Only HTML pages can be analyzed.")

        soup = BeautifulSoup(response.content, "html.parser")
        
        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        # Try to find the main article content (common tags)
        paragraphs = soup.find_all("p")
        article_text = " ".join([p.get_text() for p in paragraphs])
        
        # Clean up whitespace
        article_text = " ".join(article_text.split())
        
        if len(article_text) < 100:
             # Try a broader search if paragraphs are empty
             article_text = soup.get_text(separator=" ")
             article_text = " ".join(article_text.split())

        if len(article_text) < 50:
             raise HTTPException(status_code=400, detail="Could not extract sufficient text from the URL. The page might be protected or too short.")

        return article_text

    except requests.Timeout:
        raise HTTPException(status_code=408, detail="Request to URL timed out.")
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch URL: {str(e)}")
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=f"Error during URL processing: {str(e)}")
