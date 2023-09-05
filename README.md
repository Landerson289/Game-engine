# Game-engine
## Overview

## Object system
This game engine uses 'objects' to run the game, an object is a folder containing scripts and assets relating to the game object. This will usually include the assets inherited from the defaukt object, which include: init; rendering; data; texture. As well as any others that are specific to an object's function, like a movement script. However an object does not have to use these default scripts as they are mainly for visual objects, therefore objects like the input manager and the screen object to not need to use them.

Objects created by a user will most likely have a parent object, such as the default object or a enemy object (for a specific enemy type), from which it will copy the assets and scripts. It is important to note that once the child object has been created, changes to the parent object will not be inherited. Therefore the objects are seperate upon creation.

Objects should be defined in the 'Objects.py' file by creating an instance of the Object class, typically named like "{name}Obj" and added to the object dictionary in the getObjectDict function, the latter part of that proccess. 
## Texture rendering

## Rendering to the screen

## Rendering images

## Handling data

## Handling inputs

## Text
