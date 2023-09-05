import pygame
import os
import time
import shutil
import importlib



class Object:
  def __init__(self, name, parent):
    
    self.name = name
    if os.path.isdir(name):
      files = os.listdir(name)
      #print(files)
      self.assets = {}
      self.scripts = {}
      for file in files:
        breakDown = file.split(".")
        #print(breakDown)
        if len(breakDown) >= 2:
          if breakDown[1] == "py":
            self.scripts[breakDown[0]] = file
          self.scripts[breakDown[0]] = file
    else:
      os.mkdir(name)
      if parent != None:
        #pass # Copy assets from parent object
        for i in os.listdir(parent):
          try:
            shutil.copy(parent + "/" + i, name + "/" + i)
          except:
            print("ERROR COPYING FILE: " + i + " FROM PARENT OBJECT")
        
  def call(self, script):
    #print("test1")
    from loadData import quickData
    if script in self.scripts:
      #print("test2")
      #print(script, self.name)
      previousObject = quickData["currentObject"]
      quickData["currentObject"] = self.name

      object = importlib.import_module(f"{self.name}.{script}")
      object.run()
      
      quickData["currentObject"] = previousObject
      
  


defaultObj = Object("Default", None)
screenObj = Object("Screen", None)
squareObj = Object("Square", "Default")
triangleObj = Object("Triangle", "Default")
outlineObj = Object("Outline", "Default")
circleObj = Object("Circle", "Default")
imageObj = Object("Image", "Default")
inputObj = Object("Inputs", None)
textObj = Object("Text", "Default")
#helloObj = Object("Hello", "Text")

def getObjectDict():
  objectDict = {
    defaultObj.name : defaultObj,
    screenObj.name : screenObj,
    squareObj.name : squareObj,
    triangleObj.name : triangleObj,
    outlineObj.name : outlineObj,
    circleObj.name : circleObj,
    imageObj.name : imageObj,
    inputObj.name : inputObj,
    textObj.name : textObj,
  }
  return objectDict
