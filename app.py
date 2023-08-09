from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Hardcoded font pairing mapping
font_pairing_mapping = {
    "Arial": "Helvetica",
    "Times New Roman": "Georgia",
    "Courier New": "Monospace",
    # Add more font pairings here
}

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html") as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.get("/pairing/")
async def get_pairing(original_font: str):
    if original_font in font_pairing_mapping:
        paired_font = font_pairing_mapping[original_font]
        return {"original_font": original_font, "paired_font": paired_font}
    else:
        raise HTTPException(status_code=404, detail="Font pairing not found")
