from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import markdown
import os
import random

router = APIRouter(tags=["README.md"])

@router.get("/", response_class=HTMLResponse)
async def serve_markdown_page():
    md_path = os.path.join("Templates", "index.md")
    with open(md_path, "r") as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content)
    r = random.randint(20, 255)
    g = random.randint(20, 255)
    b = random.randint(20, 255)
    
    styled_html_content = f"""
    <html>
    <head>
        <style>
            body {{
                background-color: {f"rgb({r}, {g}, {b})"};
                color: {"black" if (r + g + b) / 3 > 100 else "white"};
                font-family: Arial, sans-serif;
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    return HTMLResponse(content=styled_html_content)