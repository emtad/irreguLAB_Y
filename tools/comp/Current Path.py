import System
import os
import Rhino

try:
    doc = Rhino.RhinoDoc.ActiveDoc
    filePath = doc.Path
    fileName = doc.Name
    path = filePath.split(fileName)[0]
    name = fileName.split('.')[0]
except:
    exit('Save Rhino file or supply valid file path.')

Path = path
Name = name