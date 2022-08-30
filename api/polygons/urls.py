from django.urls import path

from .views import TriangleListView, SquareListView


urlpatterns = [
    path('triangle/list', TriangleListView.as_view(), name="triangle-list"),
    path('square/check', SquareListView.as_view(), name="square-list"),
]
