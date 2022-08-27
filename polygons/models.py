from django.db import models


class Point(models.Model):
    x = models.FloatField()
    y = models.FloatField()


class Polygon(models.Model):
    vertices = models.ManyToManyField(Point)

    class Meta:
        abstract = True


class Triangle(Polygon):
    pass


class Square(Polygon):
    pass
