from django.shortcuts import render

from triangle.forms import TriangleForm


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
