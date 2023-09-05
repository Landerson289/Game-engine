import Objects
import time
import os
from loadData import quickData, load, upload

quickData["currentObject"] = None

print("initialising objects")

Objects.defaultObj.call("init")
Objects.screenObj.call("init")
Objects.squareObj.call("init")
Objects.triangleObj.call("init")
Objects.outlineObj.call("init")
Objects.circleObj.call("init")
Objects.imageObj.call("init")
Objects.textObj.call("init")
Objects.inputObj.call("init")


def run():
  while True:
    startTime = time.time()
    # Figure out where to put this
    quickData["renderQueue"].append("Image")
    
    Objects.screenObj.call("update2")
    quickData["renderQueue"] = []
    
    print("done")
    endTime = time.time()
    print("fps = " + str(1/(endTime - startTime)))
    #time.sleep(10000)
run()
