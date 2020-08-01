import math
class  fields:
    def __init__(self, m1, m2, r, f):
        self.m1Unknown = False
        self.m2Unknown = False
        self.rUnknown = False
        self.fUnknown  = False
        if m1 == "":
            self.m1Unknown = True
        else:
            self.m1 = float(m1)
        if m2 == "":
            self.m2Unknown = True
        else:
            self.m2 = float(m2)
        if r == "":
            self.rUnknown = True
        else:
            self.r = float(r)
        if f == "":
            self.fUnknown = True
        else:
            self.f = float(f)
    def solve(self):
        G = 0.0000000000667408
        if(self.m1Unknown):
            self.m1 = (self.f * pow(self.r, 2))/ (G * self.m2)
        elif(self.m2Unknown):
            self.m2 = (self.f * pow(self.r, 2))/ (G * self.m1)
        elif(self.rUnknown):
            self.r = math.sqrt((G * self.m1 * self.m2)/self.f)
        elif(self.fUnknown):
            self.f = (G * self.m1 * self.m2)/(pow(self.r, 2))
        gfieldStrengthm1onm2 = (self.m1 * G)/pow(self.r, 2)
        gfieldStrengthm2onm1 = (self.m2 * G)/pow(self.r, 2)
        return("Mass 1: {}, Mass 2: {}, Radius: {}, Force: {}, Field Strength of m2 on m1: {}, Field Strength of m1 on m2: {}".format(self.m1,self.m2,self.r,self.f,gfieldStrengthm2onm1,gfieldStrengthm1onm2))




    #we need to have something that calculates the acceleration due to gravity in a field eg an astronaut 70kg astronaut has a weight of 500 newtons find the acceleration due to gravity
