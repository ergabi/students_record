from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import RegisterForm, LoginForm ,StudentsReportForm
from .models import Reports

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
def home(request):
    return render (request,'home.html')

def Dashboard_view (request):
    records = Reports.objects.all()
    form = StudentsReportForm()
    return render(request,'dashboard.html',{'records':records, 'form': form})

def Record_create(request):
    if request.method == "POST":
        form = StudentsReportForm(request.POST)
        if form.is_valid():
            student_name =form.cleaned_data.get('student_name')
            subject = form.cleaned_data.get('subject')  
            new_marks = form.cleaned_data.get('mark') 
            existing_record=Reports.objects.filter(student_name=student_name,subject=subject).first()
            if existing_record:
                existing_record.mark = new_marks
                existing_record.save()
                return redirect('dashboard')                
            else:
                form.save()
            return redirect('dashboard')
    else:
        form = StudentsReportForm()
    return render(request,'records.html',{'form':form})
    
def Records_update(request,id):
    record = Reports.objects.filter(id=id).first()
    if request.method == "POST":
        form = StudentsReportForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentsReportForm(instance=record)
    return render(request, 'record.html', {'form': form})
    
def Record_delete(request,id):
    record = Reports.objects.filter(id = id).first()
    if request.method == "POST":
        record.delete()
        return redirect('dashboard')
    return render(request,'record.html',{'record':record})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    records = Reports.objects.all()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                tokens = get_tokens_for_user(user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request): 
    return render (request,'home.html')
