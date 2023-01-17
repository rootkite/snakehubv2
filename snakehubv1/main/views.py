from django.shortcuts import render
# moedels
from django.contrib.auth.models import User
from main.models import NewsLetterUser
# forms
from main.forms import NewsLetterUserForm , UserForm , UserProfileInfoForm

#login
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, 'main/index.html')



def registernl(request):
    form = NewsLetterUserForm()
    if request.method == 'POST':
        form = NewsLetterUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'main/index.html')
        else:
            print('Error : Form invalid')
    return render(request, 'main/registernl.html',{'form':form})

         



def newsletter_users(request):
    users_list = NewsLetterUser.objects.order_by('name')
    return render(request, 'main/users.html',{'userdict':users_list})


def about(request):
    return render(request, 'main/about.html')


def mainregister(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    

    return render(request , 'main/mainregister.html',
        {'user_form':user_form, 'profile_form':profile_form,'registered':registered}
        )


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password= password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('main:index'))

            else:
                HttpResponse('account not active')
        else:
            print('somone tried to login and failed')
            print('username {} and password {}'.format(username,password))
            return HttpResponse('invalid login details supplied!')

    else:

        return render(request, 'main/login.html' , {})







    # return render(request , 'main/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


@login_required
def specialcontent(request):
    return HttpResponse('youre logged in , Nice !')






