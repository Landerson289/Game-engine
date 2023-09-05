import pygame
from Objects import getObjectDict

pygame.init()

def myType(type):
  if type == int:
    mytype = "int"
  elif type == str:
    mytype = "str"
  elif type == float:
    mytype = "float"
  elif type == list:
    mytype = "list"
  #elif type == file?:
    #mytype = "file"
  return mytype

def load(file):
  f = open(file).read().splitlines()
  data = {}
  for i in f:
    item = i.split(" ")
    if len(item) > 1:
      if item[2] == "int":
        data[item[0]] = int(item[3])
      elif item[2] == "str":
        data[item[0]] = item[3]
      elif item[2] == "float":
        data[item[0]] = float(item[3])
      elif item[2] == "tuple":
        hold = item[3].split(",")
        hold[0] = hold[0][1:]
        hold[-1] = hold[-1][0:-1]
        final = ()
        for h in hold:
          final = final + (int(h),)
        data[item[0]] = final
      elif item[2] == "list":
        pass
      elif item[2] == "file":
        pass
      else:
        print("ERROR: UNKOWN TYPE " + item[2])
  #print(data)
  return data
def upload(file, data):
  string = ""
  for item in data:
    string += item + " = " + myType(type(data[item])) + " " + str(data[item]) + "\n"
  f = open(file, "w")
  f.write(string)
  f.close()
data = load("data")
screen = pygame.display.set_mode((data["width"],data["height"]))

quickData = {}

objectDict = getObjectDict()
objectData = {}

for object in objectDict:
  objectData[object] = {}


