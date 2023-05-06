from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    all_person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_person})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        #get
        name = request.POST["name"]
        age = request.POST["age"]
        #save
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request, "Successfully Created")
        #redirect
        return redirect("/")
    else:
        return render(request, "form.html")
    
def edit(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "Successfully Updated")
        return redirect("/")
    else:
        person = Person.objects.get(id=person_id)
        return render(request, "edit.html", {"person":person})
    
def delete(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request, "Successfully Delete")
    return redirect("/")