from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

# Hardcoded font pairing mapping (lowercase keys for case-insensitive matching)
font_pairing_mapping = {
    "arial": "times",
    "twisted": "gogo",
}

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html") as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.get("/pairing/")
async def get_pairing(original_font: str):
    original_font_lower = original_font.lower()  # Convert input to lowercase
    if original_font_lower in font_pairing_mapping:
        paired_font = font_pairing_mapping[original_font_lower]
        return {"original_font": original_font_lower, "paired_font": paired_font}
    else:
        raise HTTPException(status_code=404, detail="Font pairing not found")
