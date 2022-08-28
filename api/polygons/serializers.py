from rest_framework import serializers

from polygons.models import Triangle, Square


class TriangleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Triangle
        fields = '__all__'


class SquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Square
        fields = '__all__'
