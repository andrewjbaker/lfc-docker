from django.shortcuts import render, get_object_or_404
from .models import Competition, Entry
from datetime import datetime

# Create your views here.
def competition_page(request):
    competitions = Competition.objects.all().order_by("-date")[:25]
    context = {'competition_list': competitions}
    return render(request, 'competitions/competition_page.html', context)

def view_competition(request, competition_id):
    competition = get_object_or_404(Competition, pk=competition_id)
    return render(request, 'competitions/competition.html', {'competition': competition})

def enter(request, competition_id):
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