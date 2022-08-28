from django.contrib import admin

from .models import Point, Triangle, Square


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('id', 'x', 'y')


@admin.register(Triangle)
class TriangleAdmin(admin.ModelAdmin):
    pass


@admin.register(Square)
class SquareAdmin(admin.ModelAdmin):
    pass