from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib import messages
import requests
from .models import Profile  # import the Profile model
from emails.models import Gases
import time

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        state = request.POST.get('state')
        city = request.POST.get('city')
        ward = request.POST.get('ward')
        # pin = request.POST.get('pin')
        # print(request.POST)
        user_obj = User.objects.filter(username = email)
        print("usser object")
        print(user_obj)
        if user_obj.exists():
            messages.warning(request, "User already exists..")
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=email)
        user_obj.set_password(password)
        user_obj.save()

        profile_obj = Profile.objects.create(user=user_obj, phone=phone, state=state, city=city, ward=ward)
        profile_obj.save()
        # print(user_obj.get_full_name())
        print("User created successfully..")
        messages.success(request, "User created successfully..")

        return redirect('login')
        # return HttpResponseRedirect(request.path_info)
    return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(email = email)
        print("*********************")
        if not user_obj.exists():
            messages.warning(request, "User not found..")
            return HttpResponseRedirect(request.path_info)
        
        u = Profile.objects.filter(user = user_obj[0])
        print(u[0].ward)

        user_obj = authenticate(request, username = email, password = password)

        if user_obj :
            login(request, user_obj)
            # if email == 'yash@gmail.com' and password == 'yash':
            #     return redirect('home')
                # return redirect('admin-dashboard')
            # return redirect('dashboard')

            # return render(request,'dashboard.html', {'user':user_obj, 'profile':u[0]})
            return redirect('home')
        
        messages.warning(request, "Invalid credentials..")
        return HttpResponseRedirect(request.path_info)
        
    return render(request,'login.html')

def user_logout(request):
    if request.user:
        logout(request)
    return redirect('/')


def dashboard(request):
    email = 'yashhguptaa.917@gmail.com'

    all_data = Gases.objects.all()
    # result = requests.get("https://api.thingspeak.com/channels/2509489/feeds.json?api_key=246K3ARFKVT42S7O&results=7").json()
    result = requests.get("https://api.thingspeak.com/channels/2509489/feeds.json?api_key=246K3ARFKVT42S7O&results=7&timezone=Asia/Kolkata").json()
    if not request.user.is_authenticated:
        messages.warning(request, "Login required")
        return render(request,'login.html')
    u = Profile.objects.filter(user = request.user)
        # list = []
    
    

    hydrogensulfide_list = []
    # carbondioxide_list = []
    # ammonia_list = []
    float_level_list = []
    # for i in range(all_data.count()):
    #     # print(all_data[i])
    #     hydrogensulfide_list.append(all_data[i].hydrogensulfide)
    #     # carbondioxide_list.append(all_data[i].carbondioxide)
    #     # ammonia_list.append(all_data[i].ammonia)
    #     float_level_list.append(all_data[i].float_level)
    #     # list.append(
    #     #     {
    #     #         "methane" : all_data[i].methane,
    #     #         "carbondioxide" : all_data[i].carbondioxide,
    #     #         "ammonia" : all_data[i].ammonia,
    #     #         "float_level" : all_data[i].float_level,
    #     #     }
    #     # )

    for i in result['feeds']:
        if(i['field1'] == None or i['field1'] == 'inf'):
            hydrogensulfide_list.append(0.25)
        elif(float(i['field1']) < 0):
            hydrogensulfide_list.append(-float(i['field1']))
        else:
            hydrogensulfide_list.append(float(i['field1']))
        # hydrogensulfide_list.append(float(i['field1']))
        # float_level_list.append(float(i['field2']))


    context = {
        'data': all_data[all_data.count()-1],
        'hydrogensulfide_list' : hydrogensulfide_list,
        # 'carbondioxide_list' : carbondioxide_list,
        # 'ammonia_list' : ammonia_list,
        'float_level_list' : float_level_list,
        'last_hs': hydrogensulfide_list[-1],
        # 'last_fl': float_level_list[-1],
        'user':request.user, 
        'profile':u[0],

    }
    if hydrogensulfide_list[-1] > 60:
        messages.warning(request, "Danger ahead. Level is more than 60 ppm")


    return render(request,"dashboard.html", context)
    # return render(request,'dashboard.html', {'user':request.user, 'profile':u[0]})

def home(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login required")
        return render(request,'login.html')
    users = User.objects.all()
    return render(request,"home.html", {'users':users})

def zone_list(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login required")
        return render(request,'login.html')
    # users = User.objects.all()
    return render(request,"zonelist.html")

def admin_dashboard(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login required")
        return render(request,'login.html')
    users = User.objects.all()
    return render(request,"admindashboard.html", {'users':users})

def show_city_plan(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login required")
        return render(request,'login.html')
    return render(request,"cityplan.html")