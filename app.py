from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Color(BaseModel):
  r: int
  g: int
  b: int

current_color: Color = Color(**{"r": 0, "g": 0, "b": 0})

@app.post("/wool")
async def set_color(color: Color):
  global current_color
  current_color = color
  return current_color

@app.get("/wool")
async def get_color():
  return current_color