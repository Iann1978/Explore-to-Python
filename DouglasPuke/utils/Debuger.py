# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:12:35 2020

@author: Iann
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines



class Debuger():
    def __init__(self, xrange=(-15,115), yrange=(-15,115)):
        fig, ax = plt.subplots(figsize=(9 , 8))

        ax.set_xlim(xrange[0], xrange[1])
        ax.set_ylim(yrange[0], yrange[1])
        plt.title("RESEARCH ON AIRCRAFT FOR AVOIDING RADAR")

        self.fig = fig
        self.ax = ax
        return



    def DrawLine(self, p0, p1, c='grey', linewidth=0.2):
        pts = [p0 ,p1]
        xy = np.stack(pts ,axis=1)
        x = xy[0]
        y = xy[1]
        line = lines.Line2D(x ,y ,c=c ,linewidth=linewidth)
        self.ax.add_line(line)

    def DrawLineString(self, lineString, linewidth=1, color=None):
        xy = np.stack(lineString ,axis=1)
        x = xy[0]
        y = xy[1]
        line = lines.Line2D(x ,y, linewidth=linewidth, color=color)
        self.ax.add_line(line)

    def DrawShapelyLineString(self, lineString, linewidth=1, color=None):
        xy = [(i[0], i[1]) for i in lineString.coords]
        self.DrawLineString(xy, linewidth=linewidth, color=color)

    def DrawShapelyLineStringAsPoints(self, lineString, s=20):
            for pt in lineString.coords:
                self.DrawPoint(pt,s=s)

    def DrawPoint(self, pt, s=20, c='black'):
        plt.scatter(pt[0], pt[1], s=s, c=c)

    def DrawShapelyPoint(self, pt, c='black'):
        plt.scatter(pt.coords[0][0],pt.coords[0][1], s=20, c=c)

    def DrawText(self, pt, text):
        plt.text(pt.coords[0][0],pt.coords[0][1], text)



    def Show(self):
        plt.show()