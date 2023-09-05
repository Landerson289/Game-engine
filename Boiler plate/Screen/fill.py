from loadData import quickData, data
import pygame, time

def tupleToString(colour):
  string = ""
  for i in colour:
    s = str(i)
    while len(s) < 3:
      s = "0" + s
    string += s
  return string


def run():
  print("filling screen")
  
  if type(data["background"]) == tuple:
    quickData["pixels"] = (tupleToString(data["background"]) * data["width"] + ".") * data["height"]
    
  elif type(data["background"]) == str:
    quickData["pixels"] = ""

    #open texture file and draw it to the screen

    texture = open("Screen/texture").read()
    rows = texture.split(".")
    if len(rows) - 1 != data["height"]:
      print("ERROR: NOT ENOUGH ROWS IN BACKGROUND TEXTURE")
      time.sleep(1000)
      
    for row in rows:
      if len(row)//9 - 1 == data["width"]:
        print("ERROR: ROW NOT WIDE ENOUGH")
        time.sleep(1000)

    quickData["pixels"] = texture
    
  print("screen filled")
