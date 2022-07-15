from django.urls import path

from triangle.views import get_form, post_person, index, edit_person


app_name = 'triangle'
urlpatterns = [
    path('', index, name='index'),
    path('hypotenuse/', get_form, name='triangle_view'),
    path('person/', post_person, name='person_view'),
    path('person/<int:pk>/', edit_person, name='edit_person_view')
]
