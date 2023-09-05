import loadData

def run():
  this = loadData.quickData["currentObject"]

  loadData.objectData[this]["update"] = False
  
  loadData.objectData["collision area"] = []
  texture = open(this + "/texture").read()
  rows = texture.split(".")
  
  y = 0
  for row in rows:
    x = 0
    index = 0
    while index < len(row):
      if row[index] == "-":
        x -= 1
        index += 1
      else:
        if row[index: index+9] != "/////////":
          loadData.objectData[this]["collision area"].append([x,y])
        x += 1
        index += 9
    y += 1
