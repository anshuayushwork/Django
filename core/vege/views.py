from django.shortcuts import render ,redirect
from .models import *

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
    
    return render(request, "recepies.html",context)


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

        
    
     return render(request, "update_recepies.html",context)


     

def delete_recepie(request,id):
    queryset= Recepie.objects.get(id=id)
    queryset.delete()
    return redirect('recepies')


