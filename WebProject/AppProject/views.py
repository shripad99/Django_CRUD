from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import User


def home(request):
    data = User.objects.all()
    return render(request, 'base.html', {'st': data})


def loginuser(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not name or not email or not password:
            return render(request, "base.html", {"error": "Please enter all the required fields"})

        obj = User.objects.create(name=name, email=email, password=password)
        obj.save()
    data = User.objects.all()
    return render(request, 'base.html', {'st': data})


def update_data(request, pk):
    student = get_object_or_404(User, pk=pk)
    print(student)
    if request.method == 'POST':
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.password = request.POST.get("password")
        student.save()
        return redirect('home')
    return render(request, 'update.html', {'student': student})


def delete_data(request, pk):
    if request.method == 'POST':
        pi = User.objects.get(pk=pk)
        pi.delete()
    return redirect('home')
