from django.shortcuts import render

def home(request):
    context={
        'text': 'Estamos dentro da Home',
        'title': 'Home',
    }

    return render(
        request, 
        'home/index.html',
        context=context,
    )