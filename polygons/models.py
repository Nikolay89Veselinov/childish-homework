from django.db import models

from .utils import distance2D



class Point(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return f'x={self.x}, y={self.y}'

class Polygon(models.Model):
    vertices = models.ManyToManyField(Point)

    class Meta:
        abstract = True


class Triangle(Polygon):

    def get_area(self):
        param_1, param_2, param_3 = self.vertices.all()
        x1, y1 = param_1.x, param_1.y
        x2, y2 = param_2.x, param_2.y
        x3, y3 = param_3.x, param_3.y
        area = (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
        area = abs(area * 0.5)
        return(area)

    def get_perimeter(self):
        param_1, param_2, param_3 = self.vertices.all()
        perimeter = distance2D(param_1.x,param_1.y,param_2.x,param_2.y)+distance2D(param_1.x,param_1.y,param_3.x, param_3.y)+distance2D(param_3.x,param_3.y,param_2.x,param_2.y)
        return perimeter


class Square(Polygon):

    def get_area(self):
        param_1, param_2, param_3, param_4 = self.vertices.all()
        area = abs(param_1.x - param_1.y)
        return(abs(area * area))


    def get_perimeter(self):
        param_1, param_2, param_3, param_4 = self.vertices.all()
        area = abs(param_1.x - param_1.y)
        return(abs(area * 4))