# -*- coding: utf-8 -*-
# EQUATIONS
# horizontal direction
# Δx=v(x)t
# Vertical Direction
# y acceleration is constant -9.8 m/s^2
# vy=v0y+ayt
# Δy=((vy+v0y)/(2))t
# Δy=v0yt+ 0.5(ay)(t^2)
# (vy)^2=(v0y^2)+2(ay)(Δy)

# x velocity =  v(cos(θ))
# there is never acceleration in the x direction
# chage in x position = Δx=v(x)t
# change in poisition Δx = v(cos(θ))

# theta,vi,ih,fh,vx,vy,vf,vfy,vfx
import math
class motion:

    def __init__ (theta, Initial, final, initalvelocity, time):

        self.thetaKnown = False
        self.initalKnown = False
        self.finalKnown = False
        self.velocityKnown = False
        self.timeKnown = False
        if theta != "":
            self.theta = float(theta)
            self.thetaKnown = True
        if Inital != "":
            self.ih = float(Inital)
            self.initalKnown = True
        if final != "":
            self.fh = float(final)
            self.finalKnown = True
        if initalvelocity != "":
            self.iv = float(initalvelocity)
            self.velocityKnown = True
        if time != "":
            self.time = float(time)
            self.velocityKnown = True
    def run():
        if self.
