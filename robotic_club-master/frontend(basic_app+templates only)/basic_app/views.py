from django.shortcuts import render,redirect
# from django.views.generic import DetialView
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .forms import SignUpForm,UserProfileForm
from .models import Tokens,Notification
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

class Index_page(TemplateView):
	template_name="index.html"




def signup(request):
    registered = False
    if request.method == 'POST':
        print(request.POST['branch'])
        form = SignUpForm(request.POST)
        
        form3 = UserProfileForm(request.POST)
        if User.objects.filter(email=request.POST['email']).exists():
            data ={
            "message":'email already exists',
            }
            return JsonResponse(data)
        
        if form.is_valid() and form3.is_valid():
            if Tokens.objects.filter(token_code = request.POST['token_got']).exists():
                Tokens.objects.filter(token_code = request.POST['token_got']).delete()

                
                profile1 = form.save(commit=False)
                profile = form3.save(commit=False)
                profile.user = profile1.username
                
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                registered = True
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                form3.save()
                            
                data = {
                       "loged_in":True
                       }
            


                return JsonResponse(data)
            else:
                data = {
            "loged_in":False,
            
            "message":"token not valid please contact club mentors"
            }
                return JsonResponse(data)
        data = {
            "loged_in":False,
            
            "message":"form not valid please refresh and try again <br>if some problem please contact kanishk"
            }
        # return HttpResponseRedirect()
        return JsonResponse(data)
        
    else:
        form = SignUpForm()
        
        form3 = UserProfileForm()
        data ={
        "message":form.email.errors,
        }
        return JsonResponse(data)





def user_login(request):
    
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            print("no user")
            print("someone tried to login and failed")
            data = {
            "loged_in":False,
            
            "message":"username and password combination not valid"
            }
            
        elif user.is_authenticated:
            print("authenticated")
            login(request,user)
            print("loged_in")

            data = {
            "loged_in":True
            }
            
            
        # return HttpResponseRedirect()
        return JsonResponse(data)

    else:
         return render(request,'login.html',{})



def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    print("java is fine")
    return JsonResponse(data)


@login_required
def user_logout(request):
    logout(request)
    print("logout")
    return redirect('/')   

def announcements(request):
    return render(request,"announcement.html",{})

def achievements(request):
    return render(request,"achievements.html",{})

def gallery(request):
    return render(request,"gallery.html",{})

def team(request):
    return render(request,"team.html",{})

def donate(request):
    return render(request,"donate.html",{})


def notifications(request):
    if request.method == "POST":
        print(request.POST)
        notifi = Notification.objects.filter(send_by = request.user.username,user = request.user).count()
        
        for user in User.objects.all():
            Notification.objects.create(user = user,subject= request.POST["subject"],text=request.POST["txt"],send_by=request.user,unique_code=notifi+1)
        messages.add_message(request, messages.INFO, 'announcement made successful')
        return HttpResponseRedirect('/index/announcements/')
        return HttpResponse("send_notification successful")

def view_announcements(request):
    notifications = Notification.objects.filter(user=request.user).reverse()[:]
    
    print(notifications)
    for x in notifications:
        print(x.subject)
        print("  ")
    return render(request,"view_announcement.html",{"notifications":notifications})

def view_announcements_detail(request,pk):
    announcement = Notification.objects.get(pk = pk)
    announcement.read = True
    announcement.save()
    print(announcement.text)
    return render (request,"view_announcement_detail.html",{"announcement":announcement})

def delete_announcement(request,pk):
    announcement = Notification.objects.filter(unique_code = pk)
    for x in announcement:
        x.delete()
    return HttpResponse("done")


