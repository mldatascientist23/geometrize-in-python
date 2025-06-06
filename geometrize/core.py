import random
import numpy as np
from .bitmap import Bitmap
from .shape import Triangle, Rectangle, Ellipse, Circle, Line
from .renderer import render_shape

class Geometrizer:
    def __init__(self, bitmap, shape_type='triangle', alpha=0.5, trials=50):
        self.bitmap = bitmap
        self.canvas = bitmap.pixels.copy()
        self.shape_type = shape_type
        self.alpha = alpha
        self.trials = trials

    def _create_shape(self):
        w,h = self.bitmap.width, self.bitmap.height
        t = self.shape_type
        if t=='triangle':
            pts = [(random.randint(0,w), random.randint(0,h)) for _ in range(3)]
            return Triangle(pts)
        if t=='rectangle':
            x,y = random.randint(0,w), random.randint(0,h)
            return Rectangle(x,y, random.randint(1,w//4), random.randint(1,h//4))
        if t=='ellipse':
            x,y = random.randint(0,w), random.randint(0,h)
            return Ellipse(x,y, random.randint(1,w//4), random.randint(1,h//4))
        if t=='circle':
            x,y = random.randint(0,w), random.randint(0,h)
            return Circle(x,y, random.randint(1,min(w,h)//8))
        if t=='line':
            return Line(random.randint(0,w), random.randint(0,h),
                        random.randint(0,w), random.randint(0,h))
        return Triangle([(0,0),(1,0),(0,1)])

    def _score(self, new_canvas):
        return ((self.bitmap.pixels - new_canvas)**2).sum()

    def find_best(self):
        best = None
        for _ in range(self.trials):
            shape = self._create_shape()
            mask = shape.draw_mask((self.bitmap.width, self.bitmap.height))
            orig = self.canvas.copy()
            region = orig * mask[:,:,None]
            avg = (region.sum((0,1)) / (mask.sum()+1e-8)).astype(np.int16)
            new_canvas = render_shape(orig, mask, avg, self.alpha)
            err = self._score(new_canvas)
            if best is None or err < best['error']:
                best = {'canvas':new_canvas, 'error':err}
        return best

    def run(self, iterations=100):
        for _ in range(iterations):
            best = self.find_best()
            self.canvas = best['canvas']
        return self.canvas
