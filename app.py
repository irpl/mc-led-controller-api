from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Color(BaseModel):
  rgb: int

current_color = 0

@app.post("/color")
async def set_color(color: Color):
  current_color = color
  return "color set to " + current_color

@app.get("/color")
async def get_color():
  return current_color