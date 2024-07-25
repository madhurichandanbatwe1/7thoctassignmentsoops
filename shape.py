class shape:
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height
        
    def area(self,side):
        if side==4 and self.length==self.width==self.height:
            return self.length**2
        elif side==3 and self.length!=self.height:
            return 0.5*self.length*self.height
        elif side==4 and self.length!=self.height:
            return self.length*self.height
        
    def perimeter(self,side):
        if side==4 and self.length==self.width==self.height:
            return self.length*4
        elif side==3 and self.length!=self.height!=self.width:
            return self.length+self.width+self.height
        
square=shape(24,24,24)
print(square.area(4))
print(square.perimeter(4))
        