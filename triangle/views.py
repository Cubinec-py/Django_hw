from django.shortcuts import render, redirect, get_object_or_404

from triangle.forms import TriangleForm
from triangle.forms import PersonForm
from triangle.models import Person


def index(request):
    return render(request, 'triangle/index.html', {})


def get_form(request):
    hypotenuse = None
    if 'submit' in request.GET:
        form = TriangleForm(request.GET)
        if form.is_valid():
            catet1 = form.cleaned_data["catet1"]
            catet2 = form.cleaned_data["catet2"]
            hypotenuse = round(((catet1 ** 2 + catet2 ** 2) ** 0.5), 2)
    else:
        form = TriangleForm()
    return render(
        request, 'triangle/triangle_form.html',
        {
            'get_form': form,
            'hypotenuse': hypotenuse
        }
    )


def post_person(request):
    if request.method == 'POST':
        person_form = PersonForm(data=request.POST)
        if person_form.is_valid():
            Person.objects.create(
                first_name=person_form.cleaned_data['first_name'],
                last_name=person_form.cleaned_data['last_name'],
                email=person_form.cleaned_data['email']
            )
            return redirect("triangle:index")
    else:
        person_form = PersonForm()
    return render(
        request,
        "triangle/person_form.html",
        {
            'person_form': person_form,
        }
    )


def edit_person(request, pk):
    obj = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person_form = PersonForm(data=request.POST, instance=obj)
        if person_form.is_valid():
            person_form.save()
            return redirect("triangle:index")
    else:
        person_form = PersonForm(instance=obj)
    return render(
        request,
        "triangle/edit_person_form.html",
        {
            'person_form': person_form,
            'obj': obj,
        }
    )
