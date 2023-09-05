#The texture holds a pixel array of the object with 255150000 refering to (255, 150, 0)
#Other characters are ///////// for a transparent texture and . for next line.
import time # for testing
import loadData
import Objects

def insert_pixels(texture, pixels, pos):
  rows = texture.split(".")
  row = rows[pos[1]]
  newRow = row[0:int(9*pos[0])] + pixels + row[int(pos[0]*9 + len(pixels)):]
  return newRow

def run():
  objDict = Objects.getObjectDict()
  this = loadData.quickData["currentObject"]
  
  object = objDict[this]
  
  texture = open(this + "/texture").read()
  localData = loadData.load(this + "/data")
  position = [localData["x"], localData["y"]]
  
  rows = texture.split(".")
  newTexture = ""
  y = 0
  for row in rows:
    x = 0
    if len(row) > 0:
      while row[0] == "-":
        x -= 1
        row = row[1:]
      if "/" not in row:
        pixelPos = [x+position[0], y+position[1]]
        if pixelPos[0] < 0:
          row = row[-pixelPos[0]*9:]
          pixelPos[0] = 0
        row = insert_pixels(loadData.quickData["pixels"], row, pixelPos)
      else:
        sections = row.split("/////////")
        for section in sections:
          if section != "":
            pixelPos = [x+position[0], y+position[1]]
            if pixelPos[0] < 0:
              section = section[-pixelPos[0]*9:]
            row = insert_pixels(loadData.quickData["pixels"], section, pixelPos)
          x += len(section)/9 + 1
    newTexture += row + "."  
    y += 1  
