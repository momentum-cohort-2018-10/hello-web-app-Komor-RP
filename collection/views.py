from django.shortcuts import render




def index(request):
    number = 6
    thing = "Thing name"
    return render(request, 'index.html', {
        'number': number,
        'thing': thing,
    })
# Create your views here.
