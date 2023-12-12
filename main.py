
#dowloading the dataset from Roboflow
from roboflow import Roboflow
rf = Roboflow(api_key="P0IdQ8jZWlbmmKyNSMwg")
project = rf.workspace("aniket-fpzba").project("dustbin-finder")
dataset = project.version(1).download("yolov8")
