from django.urls import path

from triangle.views import get_form


app_name = 'triangle'
urlpatterns = [
    path('', get_form, name='triangle_view'),
]
