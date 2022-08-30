from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import generics, status
from rest_framework.response import Response

from polygons.models import Square, Triangle
from polygons.utils import if_right, is_equilateral, get_triangle_id

from .serializers import SquareSerializer, TriangleSerializer


class TriangleListView(generics.ListAPIView):
    queryset = Triangle.objects.all()
    serializer_class = TriangleSerializer

    def list(self, request, *args, **kwargs):

        try:
            type = request.GET['type']
        except MultiValueDictKeyError as e:
            data = {
                'message': 'missing query param in request'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        if type == 'equilateral':
            triangle = self.queryset.exclude(id__in=get_triangle_id(self.queryset.all(), is_equilateral)).all()
        elif type == 'right-angled':
            triangle = self.queryset.exclude(id__in=get_triangle_id(self.queryset.all(), if_right)).all()

        serializer = TriangleSerializer(triangle, many=True)

        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class SquareListView(generics.ListAPIView):
    queryset = Square.objects.all()
    serializer_class = SquareSerializer

    def list(self, request, *args, **kwargs):
        try:
            square_id = request.GET['square_id']
            point_x = request.GET['point_x']
            point_y = request.GET['point_y']
        except MultiValueDictKeyError:
            data = {
                'message': 'missing query param in request'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.queryset.filter(id=square_id)

        if queryset.exists():
            serializer = self.serializer_class(data={'square_id': square_id, 'point_x': point_x, 'point_y': point_y})
            if serializer.is_valid():
                import ipdb; ipdb.set_trace()
                data = {'message': 'inside: True' if serializer.validated_data else 'inside: False'}
                return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
