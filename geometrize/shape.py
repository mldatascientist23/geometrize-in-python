import numpy as np
from PIL import Image, ImageDraw

class Shape:
    def draw_mask(self, size):
        raise NotImplementedError

class Triangle(Shape):
    def __init__(self, pts): self.pts = pts
    def draw_mask(self, size):
        m = Image.new('L', size, 0)
        ImageDraw.Draw(m).polygon(self.pts, fill=255)
        return np.array(m)/255

class Rectangle(Shape):
    def __init__(self, x,y,w,h): self.rect=(x,y,w,h)
    def draw_mask(self, size):
        m = Image.new('L', size, 0)
        x,y,w,h=self.rect
        ImageDraw.Draw(m).rectangle([x,y,x+w,y+h], fill=255)
        return np.array(m)/255

class Ellipse(Shape):
    def __init__(self, x,y,w,h): self.box=(x,y,x+w,y+h)
    def draw_mask(self, size):
        m = Image.new('L', size, 0)
        ImageDraw.Draw(m).ellipse(self.box, fill=255)
        return np.array(m)/255

class Circle(Ellipse):
    def __init__(self, x,y,r): super().__init__(x-r,y-r,2*r,2*r)

class Line(Shape):
    def __init__(self, x1,y1,x2,y2): self.line=(x1,y1,x2,y2)
    def draw_mask(self, size):
        m = Image.new('L', size, 0)
        ImageDraw.Draw(m).line(self.line, fill=255, width=1)
        return np.array(m)/255
