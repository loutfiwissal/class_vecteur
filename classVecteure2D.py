class vecteure2D () :
    _count = 0
    def __init__(self,X,Y):
        self.__X = X
        self.__Y = Y
        vecteure2D._count = vecteure2D._count + 1


#Getters
    def getX (self) :
        return self.__X
    def getY (self) :
        return self.__Y


#Setters
    def setX (self,X) :
        self.__X = X
    def setY (self,Y) :
        self.__Y = Y
    

#Method 
    def Tostring (self) :
        print (f"l'abscusse X = {(self.getX())}")
        print (f"l'ordonne Y = {(self.getY())}")
        print( f"vecteure numero = {(vecteure2D._count)}")
    
    def Equals (self,V2) :
        X1,Y1 = self.getX() , self.getY()
        X2,Y2 = V2.getX() , V2.getY()

        if (X1==X2) and (Y1==Y2) :
            return True
        else:
            return False
    
    def Norme (self) :
           return (((self.__X)**2+ (self.__Y)**2))**0.5
    

# the child class
class vecteure3D (vecteure2D):
    def __init__(self,X,Y,Z):
        super().__init__(X,Y)
        self.__Z = Z
    
#getter
    def getZ (self):
        return self.__Z
    
#setter
    def setZ (self,Z):
        self.__Z = Z

#method
    def Tostring (self) :
       super().Tostring()
       print (f"Z = {(self.getZ())}")
    
    def equals(self,V3) :
        X2,Y2,Z2= self.getX , self.getY , self.getZ
        X3,Y3,Z3= V3.getX(), V3.getY() ,V3.getZ()

        if (X2==X3) and (Y2==Y3) and (Z2==Z3):
            return True
        else:
            return False
        
    def Norme(self):
        return (((self.getX())**2+ (self.getY())**2 + (self.__Z)**2))**0.5

#main programme
v1 = vecteure2D(6,8)
v1.Tostring()
print ("the norm of a vector :",v1.Norme())
v2 = vecteure2D (6,7)
print (v1.Equals(v2))

v2.Tostring()
print ("the norm of a vector :",v2.Norme())
print (v1.Equals(v2))
 
v3 = vecteure3D(4,6,7)
v3.Tostring()
print ("the norm of a vector :",v3.Norme())