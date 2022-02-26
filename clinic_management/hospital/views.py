from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout ,login ,authenticate

from hospital.models import Doctor, Patient
# Create your views here.
def home(request): 
    if request.user.is_staff :
        # Doctor.objects.filter(user = request.user).exists():
        data = Doctor.objects.get(user = request.user)
        image = data.image.url
        doctors = Doctor.objects.all
        return render(request, 'index.html', {'image': image ,'doctors': doctors })
        # return redirect('add_details')
        # user_id = request.user.id
        # data = Doctor.objects.get(pk=user_id)
        # return render(request, 'profile.html', {'data': data})
    elif request.user.is_authenticated:
        data = Patient.objects.get(user = request.user)
        image = data.image.url
        doctors = Doctor.objects.all
        return render(request, 'index.html', {'image': image ,'doctors': doctors })
    else:
        doctors = Doctor.objects.all
        return render(request, 'index.html', { 'doctors': doctors})      

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        user_type = request.POST['user_type']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        if user_type == "patient":
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            Patient.first_name = fname
            Patient.last_name = lname
            myuser.is_active = True
            myuser.save()
            messages.success(request, "Your Account has been created succesfully!! Please Signin")
            return redirect('signup')
        if user_type == "doctor":
            myuser = User.objects.create_user(username, email, pass1)
            Doctor.first_name = fname
            Doctor.last_name = lname
            myuser.first_name = fname
            myuser.last_name = lname
            # myuser.is_active = False
            myuser.is_staff = True
            myuser.save()
            messages.success(request, "Your Account has been created succesfully!! Please Signin")
            return redirect('signup')
        else:
            return HttpResponse("An error occourse!! Please try again")   
    else:
         return render(request, 'signup.html')

def signin(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username = username , password=password)
        
        if user is not None:
            login(request, user)
            return redirect ('home')
        # elif User.is_authenticated:
        #     return HttpResponse('You have already sign in')         
        else:
            messages.error(request, "wrong credentials")
            return redirect ("signin")
           
    return render(request, 'signin.html')
    


def signout(request):
    logout(request)
    return redirect("home")

def details_doctors(request):
    return HttpResponse(request.user.id)

def doctors_dashboard(request):
    pass

def profile(request):
    if request.user.is_staff :
        if  Doctor.objects.filter(user = request.user).exists():
            data = Doctor.objects.get(user = request.user)
            return render(request, 'profile.html', {'data': data})
        else:
            return redirect('add_details')
        # user_id = request.user.id
        # data = Doctor.objects.get(pk=user_id)
        # return render(request, 'profile.html', {'data': data})
    elif request.user.is_authenticated:
        # user_id = request.user.id
        # try:
        #     data = Patient.objects.get(id=user_id).first()
        #     return render(request, 'profile.html', {'data': data})
        # except Patient.objects.get(id=user_id).first() is None:
        #     return redirect('add_details')
        if  Patient.objects.filter(user = request.user).exists():
            data = Patient.objects.get(user = request.user)
            return render(request, 'profile.html', {'data': data})
        else:
            return redirect('add_details')

    else:
        return render(request, 'index.html')

def add_details(request):
    if request.user.is_authenticated:
        if request.method =='POST' and request.user.is_staff:
            user = request.user.id
            image =request.FILES['image']
            first_name = request.user.first_name
            last_name = request.user.last_name
            qualification_higest = request.POST['qualification_higest']
            specilization = request.POST['specilization']
            about = request.POST['about']
            phone_no = request.POST['phone_no']
            add_line_1 = request.POST['add_line_1']
            add_city = request.POST['add_city']
            add_state = request.POST['add_state']
            add_Pincode = request.POST['add_Pincode']
            if len(phone_no)!=10:
                messages.error(request, "Phone no. must be 10 digits!!")
                return redirect('add_details')
            if len(add_Pincode)!=6:
                messages.error(request, "Pin Code must be 6 digits!!")
                return redirect('add_details')
            Doctor(first_name=first_name, last_name=last_name, user_id=user, image= image , qualification_higest=qualification_higest, specilization=specilization, about=about, phone_no=phone_no, add_line_1=add_line_1, add_city=add_city, add_state=add_state, add_Pincode=add_Pincode).save()
            messages.success(request, "Your details has been added succesfully!")
            return redirect('add_details')

        elif request.method =='POST':
            user = request.user.id
            first_name = request.user.first_name
            last_name = request.user.last_name
            image = request.FILES['image']
            phone_no = request.POST['phone_no']
            add_line_1 = request.POST['add_line_1']
            add_city = request.POST['add_city']
            add_state = request.POST['add_state']
            add_Pincode = request.POST['add_Pincode']
            
            Patient(first_name=first_name, last_name=last_name , user_id=user, image=image, phone_no=phone_no, add_line_1=add_line_1, add_city=add_city, add_state=add_state, add_Pincode=add_Pincode).save()
            messages.success(request, "Your details has been added succesfully!")
            return redirect('add_details')

        elif request.method =='GET':
            return render (request, 'add-details.html')

        else:
            return HttpResponse("An error occoured!!! Please try again")

    else:
        return render(request,'index.html')


def edit_details(request):
        pass