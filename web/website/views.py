from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from website.models import employee
from website.forms import employeeform
from website.models import Job
from website.models import JobApplication
from website.models import NonJob
from django.contrib.auth import logout



# Create your views here.
def index(request):
    return render(request,'index.html')
def reg(request):
    return render(request,'register.html')
def home(request):
    return render(request,'home.html')
def applyform(request):
    return render(request,'applyform.html')
def success(request):
    return render(request,'success.html')



def sav(request):
    if request.method == "POST":
        form = employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  # Redirect to the user page after saving the details
    else:
        form = employeeform()
    return render(request, "register.html", {'form': form})

def log(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            use = employee.objects.get(username=username)
            if use.password == password:
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
        except employee.DoesNotExist:
            messages.error(request,"Invalid username or password")
    return render(request,"index.html")   



def jobview(request):
    jobs = Job.objects.all()
    return render(request, 'jobview.html', {'jobs': jobs})

def nontech(request):
    jobs = NonJob.objects.all()
    return render(request, 'nonjob.html', {'jobs': jobs})


def applyform(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        resume = request.FILES['resume']
        cover_letter = request.POST['cover-letter']

        # Create a new instance of the JobApplication model and save the data
        application = JobApplication(
            name=name,
            email=email,
            phone=phone,
            resume=resume,
            cover_letter=cover_letter
        )
        application.save()

        # Redirect the user to a success page or any other desired URL
        return redirect("success")

    return render(request, 'applyform.html')


def signout(request):
    logout(request)
    return redirect('index')



