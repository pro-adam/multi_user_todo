from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login as loginUser,logout
from django.contrib.auth.forms import AuthenticationForm
from . forms import TodoForm
from . models import Todo
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm()
        todos = Todo.objects.filter(user=user).order_by('priority')
        context = {
            'form':form,
            'todos':todos
        }
        return render(request,'app/index.html',context)        
     

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #messages.success(request,f'{username} registered succesfully')
            return redirect('login')
    else:            
        form = UserCreationForm()
    return render(request,'app/signup.html',{'form':form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                #loginUser maintains session for login
                loginUser(request,user)
                return redirect('home')
    else :
        form = AuthenticationForm()    
    return render(request,'app/login.html',{'form':form})


@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
                return redirect('home')
        else:
            form = TodoForm()        
        return render(request,'app/index.html',{'form':form})          
      
def signout(request):
    logout(request)
    return redirect('login')


def delete_todo(request,id):
    Todo.objects.get(pk=id).delete()
    return redirect('home')


def change_status(reqest,id,status):
    todo = Todo.objects.get(pk=id)
    todo.status  = status
    todo.save()
    return redirect('home')

