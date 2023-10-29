from django.shortcuts import render
from django.views import generic
from .forms import MarkForm

from .models import Mark


class MarkList(generic.ListView):
    template_name = "combustible/mark.html"
    model = Mark
    context_object_name = "obj"
    ordering = ["description"]


def mark_save(request):
    context = {}
    template_name = "combustible/mark_list.html"

    if request.method == "POST":
        description = request.POST.get("description")
        obj = None

        if request.POST.get("id"):
            obj = Mark.objects.filter(id=request.POST.get("id")).first()
        else:
            obj = Mark.objects.filter(description=description).first()
        if obj:
            obj.description = description
            obj.save()
        else:
            Mark.objects.create(description=description)

    obj = Mark.objects.all().order_by("description")
    context["obj"] = obj

    return render(request, template_name, context)


def mark_delete(request, pk):
    context = {}
    template_name = "combustible/mark_list.html"

    obj = Mark.objects.filter(id=pk).first()
    obj.delete()

    obj = Mark.objects.all().order_by("description")
    context["obj"] = obj

    return render(request, template_name, context)


def mark_edit(request, pk=None):
    context = {}
    template_name = "combustible/mark_form.html"

    if pk:
        obj = Mark.objects.filter(id=pk).first()
        form = MarkForm(request.POST or None, instance=obj)
    else:
        form = MarkForm(request.POST or None)

    context["form"] = form
    context["obj"] = obj

    return render(request, template_name, context)
