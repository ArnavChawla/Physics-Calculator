# -*- coding: utf-8 -*-
#variables
#m1 = mass of object 1
#m2 = mass of object 2
#v1 = velocity of object 1
#v2 = velocity of object 2
#vf = velocity final for inelastic collisions
#vi = velocity initial for expolision collisions
#give the users three options for collisionType that returns either 'inelastic' 'elastic' or 'explosion'
#elastic has v1 m1 v2 m2 v2f v1f
#inelastic m1 v1 m2 v2 vf
#explosion m1 vi m2 v1 v2
#make sure that they fill all but one form or else it will fail
class collision:
    def __init__(self, collisionType, m1, v1, m2, v2, vf, vi, v2f, v1f):
        self.collisionType = collisionType
        self.v1Unknown = False
        self.v2Unknown = False
        self.m1Unknown = False
        self.m2Unknown = False
        self.viUnknown =False
        self.vfUnknown = False
        self.v2fUnknown =False
        self.v1fUnknown =False
        if v1 == "":
            self.v1Unknown = True
        else:
            self.v1 = float(v1)
        if v2 == "":
            self.v2Unknown = True
        else:
            self.v2 = float(v2)
        if m1 == "":
            self.m1Unknown = True
        else:
            self.m1 = float(m1)
        if m2 == "":
            self.m2Unknown = True
        else:
            self.m2 = float(m2)
        if vi == "":
            self.viUnknown = True
        else:
            self.vi = float(vi)

        if vf == "":
            self.vfUnknown = True
        else:
            self.vf = float(vf)

        if v2f == "":
            self.v2fUnknown = True
        else:
            self.v2f = float(v2)

        if v1f == "":
            self.v1fUnknown = True
        else:
            self.v1f = float(v1f)
    def run(self):
        if (self.collisionType.lower() == 'inelastic' and self.vfUnknown):
            self.vf = (self.m1 * self.v1 + self.m2 * self.v2)/(self.m1 + self.m2)
            pf1 = self.m1 * self.vf
            pi1 = self.m1 * self.v1
            pf2 = self.m2 * self.vf
            pi2 = self.m2 * self.v2
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return ('Final velocity ='+str(self.vf)+'m/s<br>'+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str(self.m1 * self.v1 + self.m2 * self.v2)+"<br>"+'Total momentum final:'+str((self.m1 + self.m2)*self.vf)+"<br>")
        elif(self.collisionType.lower() == 'inelastic' and self.v2Unknown):
            self.v2 = ((self.m1 + self.m2) * self.vf - (self.m1 * self.v1))/self.m2
            pf1 = self.m1 * self.vf
            pi1 = self.m1 * self.v1
            pf2 = self.m2 * self.vf
            pi2 = self.m2 * v2
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return ('Initial velocity of object 2 ='+str(self.v2)+'m/s'+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str(self.m1 * self.v1 + self.m2 * self.v2)+"<br>"+'Total momentum final:'+str(((self.m1 + self.m2)*self.vf)))
        elif(self.collisionType.lower() == 'inelastic' and self.m2Unknown):
            self.m2 = ((m1 + m2) * vf - (m1 * v1))/v2
            pf1 = self.m1 * self.vf
            pi1 = self.m1 * self.v1
            pf2 = self.m2 * self.vf
            pi2 = self.m2 * self.v2
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return('Mass of object 2 ='+str(self.m2)+'kg'+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str(self.m1 * self.v1 + self.m2 * self.v2)+"<br>"+'Total momentum final:'+str((self.m1 + self.m2)*self.vf)+"<br>")
        elif(self.collisionType == 'inelastic' and v1Unknown):
            self.v1 = ((self.m1 + self.m2) * self.vf - (self.m2 * self.v2))/self.m1
            pf1 = self.m1 * self.vf
            pi1 = self.m1 * self.v1
            pf2 = self.m2 * self.vf
            pi2 = self.m2 * self.v2
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return('Initial velocity of object 1 ='+str(self.v1)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str(self.m1 * self.v1 + self.m2 * self.v2)+"<br>"+'Total momentum final:'+str((self.m1 + self.m2)*self.vf)+"<br>")
        elif(self.collisionType.lower() == 'inelastic' and self.m1Unknown):
            m1 = ((self.m1 + self.m2) * self.vf - (self.m2 * self.v2))/self.v1
            pf1 = self.m1 * self.vf
            pi1 = self.m1 * self.v1
            pf2 = self.m2 * self.vf
            pi2 = self.m2 * self.v2
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return('Mass of object 1 ='+str(self.m1)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str(self.m1 * self.v1 + self.m2 *self.v2)+"<br>"+'Total momentum final:'+str((self.m1 + self.m2)*self.vf)+"<br>")
        elif(self.collisionType.lower() == 'elastic' and self.v2fUnknown):
            print("m1: {} m2:{} v1:{} v2:{} v1f{}".format(self.m1,self.m2,self.v1,self.v2,self.v1f))
            self.v2f = ((self.m2 * self.v2) + self.m1 * (self.v1 - self.v1f))/self.m2
            pf1 = self.m1 * self.v1f
            pi1 = self.m1 * self.v1
            pf2 = self.m2 * self.v2f
            pi2 = self.m2 * self.v2
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return('Final velocity of object 2 ='+str(self.v2f)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str(self.m1 * self.v1 + self.m2 * self.v2)+"<br>"+'Total momentum final:'+str(self.m1 * self.v1f + self.m2 * self.v2f))
        elif(self.collisionType.lower() == 'elastic' and self.v1fUnknown):
            self.v1f = ((self.m1 * self.v1) + self.m2 * (self.v2 - self.v2f))/self.m1
            pf1 = self.m1 * self.v1f
            pi1 = self.m1 * self.v1
            pf2 = self.m2 * self.v2f
            pi2 = self.m2 * self.v2
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return  ('Final velocity of object 1 ='+str(self.v1f)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str(self.m1 * self.v1 +self.m2 * self.v2)+"<br>"+'Total momentum final:'+str(self.m1 * self.v1f + self.m2 * self.v2f))
        elif(self.collisionType.lower() == 'elastic' and self.v2Unknown):
            v2 = (self.m1*(self.v1f - self.v1)+self.m2*self.v2f)/self.m2
            pf1 = self.m1 * self.v1f
            pi1 = self.m1 * self.v1
            pf2 = self.m2 * self.v2f
            pi2 = self.m2 * self.v2
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return('Initial velocity of object 2 ='+str(self.v2)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str(self.m1 * self.v1 + self.m2 * self.v2)+"<br>"+'Total momentum final:'+str(self.m1 * self.v1f + self.m2 *self.v2f))
        elif(self.collisionType.lower() == 'elastic' and self.v1Unknown):
            self.v1 = (self.m2*(self.v2f - self.v2)+self.m1*self.v1f)/self.m1
            pf1 = self.m1 * self.v1f
            pi1 = self.m1 * self.v1
            pf2 = self.m2 * self.v2f
            pi2 = self.m2 * self.v2
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return('Initial velocity of object 1 ='+str(self.v1)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str(self.m1 * self.v1 + self.m2 * self.v2)+"<br>"+'Total momentum final:'+str(self.m1 * self.v1f + self.m2 * self.v2f))
        elif(self.collisionType.lower() == 'elastic' and self.m2Unknown):
            m2 = (self.m1 * (self.v1f - self.v1))/(self.v2 - self.v2f)
            pf1 = self.m1 * self.v1f
            pi1 = self.m1 * self.v1
            pf2 = self.m2 * self.v2f
            pi2 = self.m2 * self.v2
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            return('mass of object 2 ='+str(self.m2)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str(self.m1 * self.v1 + self.m2 * self.v2)+"<br>"+'Total momentum final:'+str(self.m1 * self.v1f + self.m2 * self.v2f))
        elif(self.collisionType.lower() == 'elastic' and self.m1Unknown):
            self.m1 = (self.m2 * (self.v2f - self.v2))/(self.v1 - self.v1f)
            pf1 = self.m1 * self.v1f
            pi1 = self.m1 * self.v1
            pf2 = self.m2 * self.v2f
            pi2 = self.m2 * self.v2
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return ('mass of object 1 ='+str(self.m1)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str(self.m1 * self.v1 + self.m2 *self.v2)+"<br>"+'Total momentum final:'+str(self.m1 * self.v1f + self.m2 * self.v2f))
        elif(self.collisionType.lower() == 'explosion' and self.v2Unknown):
            self.v2 = ((self.m1 + self.m2) * self.vi - (self.m1 * self.v1)) / self.m2
            pf1 = self.m1 * self.v1
            pi1 = self.m1 * self.vi
            pf2 = self.m2 * self.v2
            pi2 = self.m2 * self.vi
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return ('Final velocity of object 2 ='+str(self.v2)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str((self.m1 + self.m2) * self.vi)+"<br>"+'Total momentum final:'+str(self.m1 * self.v1 + self.m2 * self.v2))
        elif(self.collisionType.lower() == 'explosion' and self.v2Unknown):
            self.v1 = ((self.m1 + self.m2) * self.vi - (self.m2 * self.v2)) /self.m1
            self.pf1 = self.m1 * self.v1
            pi1 = self.m1 * self.vi
            pf2 = self.m2 * self.v2
            pi2 = self.m2 * self.vi
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            print("a")
            return ('Final velocity of object 1 ='+str(self.v1)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str((self.m1 + self.m2) * self.vi)+"<br>"+'Total momentum final:'+str(self.m1 * self.v1 + self.m2 * self.v2))
        elif(self.collisionType.lower() == 'explosion' and self.viUnknown):
            self.vi = (self.m1 * v1 + self.m2 * self.v2)/ (self.m1 + self.m2)
            pf1 = self.m1 * self.v1
            pi1 = self.m1 * self.vi
            pf2 = self.m2 * self.v2
            pi2 = self.m2 * self.vi
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            return ('Initial velocity ='+str(self.vi)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str((self.m1 + self.m2) * self.vi)+"<br>"+'Total momentum final:'+str(self.m1 * self.v1 + self.m2 * self.v2))
        elif(self.collisionType.lower() == 'explosion' and self.m2Unknown):
            self.m2 = (self.m1 * (self.v1 - self.vi))/(self.vi - self.v2)
            pf1 = self.m1 * self.v1
            pi1 = self.m1 * self.vi
            pf2 = self.m2 * self.v2
            pi2 = self.m2 * self.vi
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            return ('Mass of object 2 ='+str(self.m2)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str((self.m1 + self.m2) * self.vi)+"<br>"+'Total momentum final:'+str(self.m1 * self.v1 + self.m2 * self.v2))
        elif(self.collisionType.lower() == 'explosion' and self.m1Unknown):
            self.m1 = (self.m2 * (self.v2 - self.vi))/(self.vi - self.v1)
            pf1 = self.m1 * self.v1
            pi1 = self.m1 * self.vi
            pf2 = self.m2 * self.v2
            pi2 = self.m2 * self.vi
            changeP1 = str(pf1 - pi1)
            changeP2 = str(pf2 - pi2)
            return('Mass of object 1 ='+str(self.m1)+"<br>"+'Δp object 1 ='+changeP1+"<br>"+'Δp object 2 ='+changeP2+"<br>"+'Total momentum initial:'+str((self.m1 + self.m2) * self.vi)+"<br>"+'Total momentum final:'+str(self.m1 * self.v1 + self.m2 * self.v2))
        else:
            return ('yikesy')
