import pygame
import Objects
import time
from loadData import data, screen, quickData, objectData

def run():
  #screen.fill(data["background"])
  print("Updating objects")
  
  print(objectData["Image"]["update"])
  for object in Objects.getObjectDict():
    #try:
      if objectData[object]["update"] == True:
        Objects.getObjectDict()[object].call("update")
    #except:
    #  print(object)
    #  time.sleep(10000)
  

  print("Managing inputs")
  Objects.inputObj.call("manage")
  
  print("Updating Screen")
  
  Objects.screenObj.call("fill")
  
  objectDict = Objects.getObjectDict()
  for object in quickData["renderQueue"]:
    objectDict[object].call("new_render")
  
  #draw the pixels on the screen
  print("drawing pixels")
  pixels = quickData["pixels"]
  rows = pixels.split(".")
  
  index = 0
  x = 0
  y = 0

  

  for row in rows:
    nextColour = row[0:9]
    index = 0
    x = 0
    start = 0
    while index < len(row):
      #get a line of colours that are all the same
      colour = nextColour
      nextColour = row[index+9:index+18]
      if colour != nextColour or "." in nextColour:
        if colour != "/////////":
          colour = (int(colour[0:3]), int(colour[3:6]), int(colour[6:9]))
          pygame.draw.rect(screen, colour, pygame.Rect(start, y, x-start, 1))
        start = x
      index += 9
      x += 1
        #draw a rectangle there
      #increment position and index
    y += 1
  pygame.display.update()
