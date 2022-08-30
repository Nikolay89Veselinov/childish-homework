from rest_framework import serializers

from polygons.models import Triangle, Square, Polygon, Point


class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = ('x', 'y')


class TriangleSerializer(serializers.ModelSerializer):
    vertices = PointSerializer(many=True)

    class Meta:
        model = Triangle
        fields = ('id', 'vertices')


class SquareSerializer(serializers.ModelSerializer):
    square_id = serializers.IntegerField()
    point_x = serializers.FloatField()
    point_y = serializers.FloatField()

    class Meta:
        model = Square
        fields = ('square_id', 'point_x', 'point_y')

    def validate(self, value):
        square_id = self.initial_data['square_id']
        point_x = float(self.initial_data['point_x'])
        point_y = float(self.initial_data['point_y'])
        square = Square.objects.get(id=square_id)
        x = square.vertices.values()[0]['x']
        y = square.vertices.values()[0]['y']

        if point_x >= x and point_y >= x and point_x <= y and point_y <= y:
            return True
        else:
            return False