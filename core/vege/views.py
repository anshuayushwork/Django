from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def recepies(request):
    """
    Render the recepies page.

    """
    if request.method == 'POST':
        data=request.POST
        recepie_image = request.FILES.get('recepie_image')
        recepie_name = data.get('recepie_name')
        recepie_description = data.get('recepie_description')

        # Save the recepie to the database
        Recepie.objects.create(
            recepie_name=recepie_name,
            recepie_description=recepie_description,
            recepie_image=recepie_image
        )



        # print(recepie_name, recepie_description,recepie_image)

         
        return redirect('recepies')
    queryset = Recepie.objects.all()
    context = {
        'recepies': queryset   
    }
    
    return render(request, "recepie/recepies.html",context)


def update_recepie(request,id):
     queryset = Recepie.objects.all()
     context = {
        'recepies': queryset   
    }
     if request.method == 'POST':
        data=request.POST
        recepie_image = request.FILES.get('recepie_image')
        recepie_name = data.get('recepie_name')
        recepie_description = data.get('recepie_description')

      
        queryset = Recepie.objects.get(id=id)
        queryset.recepie_name = recepie_name
        queryset.recepie_description = recepie_description
        if recepie_image:
            queryset.recepie_image = recepie_image
        queryset.save()

        return redirect('recepies')

        
    
     return render(request, "recepie/update_recepies.html",context)


     

def delete_recepie(request,id):
    queryset= Recepie.objects.get(id=id)
    queryset.delete()
    return redirect('recepies')

def login_page(request):

    if request.user.is_authenticated:
       return redirect('/recepies/')

    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')
        print(username, password)
        if not User.objects.filter(username=username).exists():
                messages.error(request, "Invalid username ")
                return redirect('/login/')
        user = authenticate(username = username, password=password)

        if user is None:
            messages.error(request, "Invalid password")
            return redirect('/login/')
        else:
            login(request ,user)
            return redirect('/recepies/')


    return render(request, "login.html")


def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')   
        username = request.POST.get('Username')
        password = request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.error(request, "Username already exists")
            return redirect('/register/')

        user= User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            
        )

        user.set_password(password)
        user.save()

        messages.success(request, "Registration successful")

        return redirect('/register/')
    return render(request, "register.html")