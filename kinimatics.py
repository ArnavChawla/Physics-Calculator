# -*- coding: utf-8 -*-
class kinematics:
    def __init__(self, s, u, v, a, t):

        self.sKnown = False
        self.uKnown = False
        self.tKnown = False
        self.aKnown = False
        self.vKnown = False
        if s != "":
            self.sKnown = True
            self.s = float(s)
        if u != "":
            self.uKnown = True
            self.u =float(u)
        if t != "":
            self.tKnown = True
            self.t = float(t)
        if a != "":
            self.aKnown = True
            self.a = float(a)
        if v != "":
            self.vKnown = True
            self.v = float(v)




    def solve(self):
        if self.sKnown and self.uKnown and self.vKnown:
            self.a = (self.v**2-self.u**2) / (2 * self.s)
            self.t = 2 * self.s / (self.u + self.v)
            st = "Acceleration = {}<br> Time = {}<br>".format(self.a,self.t)
            return st

        elif self.sKnown and self.uKnown and self.aKnown:
            #v = sqrt(u**2 + 2 * a * s)
            #t1 = -u / a + sqrt(2 * a * s + u**2) / a
            #t2 = -u / a - sqrt(2 * a * s + u**2) / a
            self.t = (-self.u + sqrt(self.u**2 - 4(.5 * self.a)(-self.s)))/self.a
            self.v = self.u + self.a * self.t
            print("")
            #print "Final velocity =",v, "or ",-v
            st = "Final Velocity = {}<br>Time = {}<br>".format(self.v,self.t)
            return st

        elif self.sKnown and self.uKnown and self.tKnown:
            self.a = 2 * (self.s - self.u * self.t) / self.t**2
            self.v = self.u + self.a *self.t
            print("")
            print("Final velocity =",self.v)
            print("Acceleration =",self.a)
            st= "Final Velocity = {}<br>Acceleration = {}".format(self.v,self.a)
            return st

        elif self.sKnown and self.vKnown and self.aKnown:
            #u = sqrt(v**2 - 2 * a * s)
            self.t = (2 * self.v + sqrt(4 * self.v**2 - 4 * self.a * 2 * self.s))/(2 *self.a)

            #t1 = 2 * s / (v + sqrt(v**2 - 2 * a * s))

           #t2 = 2 * s / (v - sqrt(v**2 - 2 * a * s))
            self.u = self.v - self.a * self.t
            print("")
            print("Initial velocity =",self.u)
            print("Time =",self.t)
            st = "Inital Velocity = {}<br>Time = {}".format(self.u,self.t)
            return st

        elif self.sKnown and self.vKnown and self.tKnown:
            self.u = (2 * self.s - self.v * self.t)/self.t
            self.a = (self.v - self.u) / self.t
            print("")
            print("Initial velocity =",self.u)
            print("Acceleration =",self.a)
            st = "Inital Velocity = {}<br>Acceleration = {}<br>".format(self.u,self.a)
            return st

        elif self.sKnown and self.aKnown and self.tKnown:
            self.u = (self.s - 0.5 * self.a * self.t**2) / self.t
            self.v = self.u + self.a * self.t
            print("")
            print("Initial velocity =",self.u)
            print("Final velocity =",self.v)
            st = "Inital Velocity = {}<br>Final Velocity = {}<br>".format(self.u,self.v)
            return st

        elif self.uKnown and self.vKnown and self.aKnown:
            self.s = (self.v**2 - self.u**2) / (2 * self.a)
            self.t = (self.v - self.u) / self.a
            print("")
            print("Distance =",self.s)
            print("Time =",self.t)
            st = "Distance = {}<br>Time = {}<br>".format(self.s,self.t)
            return st

        elif self.uKnown and self.vKnown and self.tKnown:
            self.s = 0.5 * (self.u+self.v) * self.t
            self.a = (self.v - self.u) / self.t
            print("")
            print("Distance =",self.s)
            print("Acceleration =",self.a)
            st = "Distance = {}<br>Acceleration = {}<br>".format(self.s,self.a)
            return st

        elif self.uKnown and self.aKnown and self.tKnown:
            self.v = self.u + self.a * self.t
            self.s = self.u * self.t + 0.5 * self.a * self.t**2
            print("")
            print("Final velocity =",self.v)
            print("Distance =",self.s)
            st = "Final Velocity = {}<br>Distance = {}<br>".format(self.v,self.s)
            return st

        elif self.vKnown and self.aKnown and self.tKnown:
            self.u = self.v - self.a * self.t
            self.s = self.u *self.t + .5 * self.a * (self.t**2)
            print("")
            print("Initial velocity =",self.u)
            print("Distance =",self.s)
            st = "Initial Velocity = {}<br>Distance = {}<br>".format(self.u,self.s)
            return st
