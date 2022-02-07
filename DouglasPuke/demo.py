
from utils import Debuger
import numpy as np

from shapely.geometry import LineString
# from shapely.geometry import Line
from shapely.geometry import Point
from shapely.geometry import box

import argparse


def DouglasPluke(lines, deita=0.00001, debuger=None):

    if debuger != None:
        debuger.DrawShapelyLineString(track, 5)
        # debuger.DrawShapelyLineStringAsPoints(track, 50)

    ori = lines
    # deita = 0.00001
    finish = False
    result1 =  [0, len(ori.coords)-1]

    while not finish:
        finish = True
        result = result1
        result1 = [0]

        for j in range(0, len(result)-1):
            start = result[j]
            end = result[j+1]
            seg = LineString([ori.coords[start], ori.coords[end]])

            if debuger != None:
                segRegion = seg.buffer(deita)
                debuger.DrawShapelyLineString(segRegion.exterior,0.5)

            maxidx = -1
            maxdis = 0
            for i in range(start+1, end):
                p = Point(ori.coords[i])


                dis = p.distance(seg)
                if dis > maxdis:
                    maxdis = dis
                    maxidx = i

                if debuger != None:
                    debuger.DrawShapelyPoint(p, 'red')
                    # debuger.DrawText(p, dis)
                # print('dis:', dis)

            if maxidx != -1 and maxdis > deita:
                result1.append(maxidx)
                if start != maxidx-1:
                    finish = False
                if end != maxidx+1:
                    finish = False

            result1.append(end)

    result_coords = [ori.coords[i] for i in result1]

    resultLineStrings = LineString(result_coords)

    if debuger != None:
        debuger.DrawShapelyLineString(resultLineStrings, linewidth=1,  color='red')

    return resultLineStrings



import json
from types import SimpleNamespace

data = '''
[
    {
        "ErrorCode" : 0,
        "ErrorString" : "No Error",
        "Track" : [
            {
                "Latitude" : 39.5008621580,
                "Longitude" : 116.39212240880,
                "Orientation" : -5.820404620015175,
                "TblName" : "",
                "Time" : 1641544690,
                "Userid" : 5
            },
            {
                "Latitude" : 39.50085764403051,
                "Longitude" : 116.3921230051291,
                "Orientation" : -5.775053442639424,
                "TblName" : "",
                "Time" : 1641544630,
                "Userid" : 5
            }
        ]
    }
]
'''


with open('line.json', 'rt') as f:
    data = f.read()

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print(x[0].Track)

coordinates = [(pt.Longitude, pt.Latitude) for pt in x[0].Track]
print(coordinates)


track = LineString(coordinates)








# track = LineString([[0, 0], [15, 13], [22, 16], [28,25]])
width = track.bounds[2] - track.bounds[0]
height = track.bounds[3] - track.bounds[1]
bounds = [i for i in track.bounds]
bounds[0] -= width/10.0
bounds[1] -= height/10.0
bounds[2] += width/10.0
bounds[3] += height/10.0

# box = box(*track.bounds)
# box = box.buffer(box.boundary.width)
# bounds = box.bounds


debuger = Debuger(xrange=(bounds[0], bounds[2]), yrange=(bounds[1], bounds[3]))




debuger.DrawShapelyLineString(track, 5)
# debuger.DrawShapelyLineStringAsPoints(track, 50)

result = DouglasPluke(track)

debuger.DrawShapelyLineString(result, 1, color='red')
debuger.DrawShapelyLineStringAsPoints(result, 50)
debuger.Show()

print(len(track.coords),":", len(result.coords))





