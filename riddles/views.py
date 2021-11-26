from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Student
from django.views.generic import TemplateView, ListView

# получение данных из бд
def index(request):
    queryset = Student.objects.all()
    context = {'Student': queryset}
    return render(request, "my_site.html", context)

# удаление данных из бд
def delete(request, id):
    try:
        p = Student.objects.get(id=id)
        p.delete()
        return HttpResponseRedirect("/")
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Student()
        tom.Full_Name = request.POST.get("Full_Name")
        tom.Faculty = request.POST.get("Faculty")
        tom.Group = request.POST.get("Group")
        tom.Course = request.POST.get("Course")
        tom.Date = request.POST.get("Date")
        tom.Reason = request.POST.get("Reason")
        tom.save()
    return HttpResponseRedirect("/")

# изменение данных в бд
def edit(request, id):
    try:
        tom = Student.objects.get(id=id)

        if request.method == "POST":
            tom.Full_Name = request.POST.get("Full_Name")
            tom.Faculty = request.POST.get("Faculty")
            tom.Group = request.POST.get("Group")
            tom.Course = request.POST.get("Course")
            tom.Date = request.POST.get("Date")
            tom.Reason = request.POST.get("Reason")
            tom.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"tom": Student})
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")
