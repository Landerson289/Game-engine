from loadData import quickData, data, objectData
import pygame

def run():
  global quickData
  this = quickData["currentObject"]
  objectData[this]["update"] = False
  quickData["renderQueue"] = []
  quickData["pixels"] = ("/////////" * data["width"] + ".") * data["width"]

  if type(data["background"]) == str and data["background"] != "texture":
    #If the background points to a image render the image into the  texture file
    surface = pygame.image.load(data["background"])
    surface = pygame.transform.scale(surface, (data["width"], data["height"]))
    texture = ""
    for y in range(surface.get_height()):
      for x in range(surface.get_width()):
        colour = surface.get_at((x,y))
        if colour[3] >= 0.5:
          string = ""
          for i in range(3):
            s = str(colour[i])
            if len(s) == 1:
              s = "00" + s
            elif len(s) == 2:
              s = "0" + s
            string += s
        else:
          string = "/////////"
        texture += string
      texture += "."

    f = open("Screen/texture", "w")
    f.write(texture)
    f.close()
