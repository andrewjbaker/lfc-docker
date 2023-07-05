from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

User = get_user_model()

# Create your views here.
def member_login(request):
    if request.user.is_authenticated:
        return(overview(request))
    else:
        return render(request, 'membership/login.html')
    
def register(request):
    if request.user.is_authenticated:
        return(overview(request))
    else:
        return render(request, 'membership/register.html')

def overview(request):
    return render(request, 'membership/overview.html', {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "telephone": request.user.telephone,
            "membership_number": request.user.membership_number,
            "address1": request.user.address1,
            "address2": request.user.address2,
            "city": request.user.city,
            "postcode": request.user.postcode
        }
    )

def authenticate_member(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is None:
        return render(request, 'membership/login.html', {
                'error_message': "Your email address and/or password are incorrect."
            })
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('membership:overview')
        )

def registration(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    telephone = request.POST.get('telephone')
    address1 = request.POST.get('address1')
    address2 = request.POST.get('address2')
    city = request.POST.get('city')
    postcode = request.POST.get('postcode')

    try:
        User.objects.get(email=email)
        return render(request, 'membership/register.html', {
            'error_message': "Sorry, a user with this email address already exists."
        })
    except User.DoesNotExist:
        # Create new user
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            telephone=telephone,
            address1=address1,
            address2=address2,
            city=city,
            postcode=postcode
        )

        if user is None:
            return HttpResponseRedirect( 
                reverse('membership:member_login')
            )
        else:
            login(request, user)
            return HttpResponseRedirect(
                reverse('membership:overview')
            )

def logout_member(request):
    logout(request)
    return HttpResponseRedirect(
        reverse('membership:member_login')
    )