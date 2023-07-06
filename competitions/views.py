from django.shortcuts import render, get_object_or_404
from .models import Competition, Entry
from datetime import datetime

# Create your views here.
def competition_page(request):
    """Returns a rendered view of the requested competitions page
    
    :param request: HTTP request initiated by the user
    :type request: HTTP request
    :return: The competition_page.html webpage containing a view of the competitions
    :rtype: HTTP response
    """
    competitions = Competition.objects.all().order_by("-date")[:25]
    context = {'competition_list': competitions}
    return render(request, 'competitions/competition_page.html', context)

def view_competition(request, competition_id):
    """Returns a rendered view of a page linked to a specific competition
    
    :param request: HTTP request initiated by the user
    :type request: HTTP request
    :param competition_id: The identifier for the selected competition (primary key, title)
    :type competition_id: str
    :return: The competition.html webpage containing a view of the specific competition
    :rtype: HTTP response
    """
    competition = get_object_or_404(Competition, pk=competition_id)
    return render(request, 'competitions/competition.html', {'competition': competition})

def enter(request, competition_id):
    """Returns a success message if the user successfully enters the competition, or an error
    message asking the user to log in if they are not authenticated
    
    :param request: HTTP request initiated by the user
    :type request: HTTP request
    :param competition_id: The identifier for the selected competition (primary key, title)
    :type competition_id: str
    :return: The post_entry.html page with a success message if the user is authenticated and
    successfully enters, or the membership/login.html page with an error message if the user
    is not logged in and authenticated
    :rtype: HTTP response
    """
    competition = get_object_or_404(Competition, pk=competition_id)
    
    if request.user.is_authenticated:
        try:
            Entry.objects.get(competition_id=competition_id, email=request.user.email)
            return render(request, 'competitions/post_entry.html', {
                'error_message': "Sorry, you have already entered this competition.",
                'competition': competition
            })
        except Entry.DoesNotExist:
            Entry.objects.create(
                competition=competition, 
                member_id = request.user.membership_number,
                email = request.user.email,
                entry_date_time = datetime.now()
            )
            return render(request, 'competitions/post_entry.html', {
                'success_message': "Congratulations, you have entered the competition. Good luck!",
                'competition': competition
            })
    else:
        return render(request, 'membership/login.html', {
            'error_message': "You must be logged in to enter the members' competition."
        })