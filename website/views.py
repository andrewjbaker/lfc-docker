from django.shortcuts import render

# Create your views here.
def index(request):
    """Returns a rendered view of the website home page
    :param request: HTTP request initiated by the user
    :type request: HTTP request
    :return: The website home page, index.html
    :rtype: HTTP response
    """
    return render(request, "index.html")

def honours(request):
    """Returns a rendered view of the requested club honours page
    :param request: HTTP request initiated by the user
    :type request: HTTP request
    :return: The honours.html webpage containing the history of the club's trophy successes
    :rtype: HTTP response
    """
    return render(request, "honours.html")