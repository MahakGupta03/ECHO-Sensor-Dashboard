from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Gases




def home(request):
    # all_data = Gases.objects.all()
    # print(all_data[all_data.count()-1].methane)
    # return render(request,"home.html")
    return render(request,"register.html")
    

def sent_threshold_mail(request):
    email = 'yashhguptaa.917@gmail.com'
    all_data = Gases.objects.all()
    
    if request.method== 'POST':
        # methane = int(request.POST.get("methane"))
        hydrogensulfide = int(request.POST.get("hydrogensulfide"))
        # carbondioxide = int(request.POST.get("carbondioxide"))
        # ammonia = int(request.POST.get("ammonia"))
        float_level = int(request.POST.get("float_level"))
        context = {
            "hydrogensulfide" : hydrogensulfide,
            # "carbondioxide" : carbondioxide,
            # "ammonia" : ammonia,
            "float_level" : float_level
        }
        gases_obj = Gases.objects.create(hydrogensulfide=hydrogensulfide,float_level=float_level)
        gases_obj.save()

        if(hydrogensulfide>50  or float_level>50):
            subject = "Danger"
            message = f"Be Carefull!! The value of Hydrogen Sulfide is {hydrogensulfide} and Float level is {float_level}"
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [email])
            # return HttpResponse("Mail send successfully")
            messages.warning(request, "Be Carefull!! Please check your mail")
            # return render(request,"dashboard.html", context)
        else:
            messages.success(request, "No Need to Worry")
    # if not request.user.is_authenticated:
    #         return render(request,"Login.html")
        
    
            
    # list = []
    hydrogensulfide_list = []
    # carbondioxide_list = []
    # ammonia_list = []
    float_level_list = []
    for i in range(all_data.count()):
        # print(all_data[i])
        hydrogensulfide_list.append(all_data[i].hydrogensulfide)
        # carbondioxide_list.append(all_data[i].carbondioxide)
        # ammonia_list.append(all_data[i].ammonia)
        float_level_list.append(all_data[i].float_level)
        # list.append(
        #     {
        #         "methane" : all_data[i].methane,
        #         "carbondioxide" : all_data[i].carbondioxide,
        #         "ammonia" : all_data[i].ammonia,
        #         "float_level" : all_data[i].float_level,
        #     }
        # )


    context = {
        'data': all_data[all_data.count()-1],
        'hydrogensulfide_list' : hydrogensulfide_list,
        # 'carbondioxide_list' : carbondioxide_list,
        # 'ammonia_list' : ammonia_list,
        'float_level_list' : float_level_list

    }

    return render(request,"dashboard.html", context)
