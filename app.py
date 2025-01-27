from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

color_dictionary = {
  "WHITE": 0xFFFFFF,
  "BLACK": 0x0,
  "ORANGE": 0xff6500,
  "MAGENTA": 0xff00ff,
  "CYAN": 0x00ffff,
  "YELLOW": 0xffff00,
  "LIME": 0xbfff00,
  "PINK": 0xff748c,
  "PURPLE": 0x800080,
  "BLUE": 0x0000ff,
  "BROWN": 0xa52a2a,
  "GREEN": 0x00ff00,
  "RED": 0xff0000
}
class Color(BaseModel):
  color_name: str

current_color: Color = Color(color_name="BLACK")

@app.post("/color")
async def set_color(color: Color):
  global current_color
  current_color = color
  return "color set to " + current_color.color_name

@app.get("/color")
async def get_color():
  return { 
    "rgb": color_dictionary[current_color.color_name]
  }