from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def honours(request):
    return render(request, "honours.html")