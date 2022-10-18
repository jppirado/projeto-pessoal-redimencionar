from django.shortcuts import render
from .forms import ImagemModelForm
# Create your views here.

def home( request ):

    if str(request.method) == 'POST':
        form = ImagemModelForm( request.POST, request.FILES or None)
        print( form )
        if form.is_valid():
            form.save()
            form = ImagemModelForm()
    else:
        form = ImagemModelForm() 


    ctx = {
        'form' : form
    }

    return render( request  , 'home.html' , ctx )


