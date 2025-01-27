from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Color(BaseModel):
  rgb: int

current_color: Color = Color(rgb=0)

@app.post("/color")
async def set_color(color: Color):
  global current_color
  current_color = color
  return "color set to " + str(current_color.rgb)

@app.get("/color")
async def get_color():
  return current_color