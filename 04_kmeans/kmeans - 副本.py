import numpy as np
import cv2
from matplotlib import pyplot as plt

Z = np.array([
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873],
[1023.000000, 0.942478],
[247.000000, 1.989675],
[1027.000000, 0.942478],
[342.000000, 2.199115],
[916.000000, 0.942478],
[783.000000, 0.104720],
[903.000000, 1.047198],
[754.000000, 1.151917],
[151.000000, 1.884956],
[795.000000, 1.047198],
[1102.000000, 0.942478],
[787.000000, 0.104720],
[791.000000, 1.047198],
[491.000000, 0.000000],
[1020.000000, 0.942478],
[-140.000000, 2.932153],
[1098.000000, 0.837758],
[-305.000000, 3.036873],
[907.000000, 1.047198],
[465.000000, 1.256637],
[616.000000, 0.000000],
[-302.000000, 3.036873]
])

'''
#converttonp.float32
#definecriteriaandapplykmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center=cv2.kmeans(Z,2,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
#Nowseparatethedata,Notetheflatten()
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]
#Plotthedata
plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(center[:,0],center[:,1],s =80,c = 'y',marker = 's')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()
'''
Z = np.float32(Z)
F = np.array([[1.0,0.0],[0.0,200.0]],dtype=np.float32)
Z = np.dot(Z,F)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 1.0)
ret,label,center=cv2.kmeans(Z,21,criteria,10,cv2.KMEANS_PP_CENTERS)
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]

#for rho,theta in center:
#    print "%f, %f" % (rho,theta)

img = cv2.imread('4.jpg')
for rho,theta in center:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 +1000*(-b))
    y1 = int(y0 +1000*(a))
    x2 = int(x0 -1000*(-b))
    y2 = int(y0 -1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#Plotthedata
plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(center[:,0],center[:,1],s =80,c = 'y',marker = 's')

plt.scatter(Z[:,0],Z[:,1])
plt.xlabel('rho')
plt.ylabel('theta')
plt.show()
'''
