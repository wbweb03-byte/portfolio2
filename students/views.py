from django.shortcuts import render, redirect, get_object_or_404
from .models import Students
from .forms import StudentCreation

# Create your views here.

def dashboard(request):
    
    return render(request, "dashboard.html")


def students_views(request):
    students = Students.objects.all()
    return render(request, "students.html", {"students":students })

def student_details(request, id):

    student = get_object_or_404(
        Students,
        id=id
    )

    return render(
        request,
        "details.html",
        {"student": student})

def students_add(request):

    forms = StudentCreation()

    if request.method == "POST":

        forms = StudentCreation(request.POST,request.FILES)

        if forms.is_valid():

            forms.save()

            return redirect("students_views")

    return render(request,"add_student.html",{"forms": forms})


from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Students
from .forms import StudentCreation


def students_edit(request, id):

    student = get_object_or_404(Students,id=id)

    forms = StudentCreation(instance=student)

    if request.method == "POST":

        forms = StudentCreation( request.POST, request.FILES, instance=student)

        if forms.is_valid():

            forms.save()

            return redirect("students_views")

    return render(request, "add_student.html", {"forms": forms})

def students_delete(request, id):

    student = get_object_or_404(
        Students,
        id=id
    )

    if request.method == "POST":

        student.delete()

        return redirect(
            "students_views"
        )

    return render(
        request,
        "delete.html",
        {"student": student}
    )
