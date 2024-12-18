from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import markdown
import os

router = APIRouter(tags=["README.md"])

@router.get("/", response_class=HTMLResponse)
async def serve_markdown_page():
    # Read the Markdown file from the Templates folder
    md_path = os.path.join("Templates", "index.md")
    with open(md_path, "r") as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Return as HTML response
    return HTMLResponse(content=html_content)