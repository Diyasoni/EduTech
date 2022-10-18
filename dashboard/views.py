from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages
from django.views import generic

from django.http import HttpResponse, JsonResponse
# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')


def room(request, room):
    #username1 = request.GET.get('username')
    username = request.user.username
    room_details = Room.objects.get(name=room)
    return render(request, 'dashboard/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


def notes(request):
    if request.method=="POST":
        form=NotesForm(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes added from {request.user.username} successfully!")
    else:
        form=NotesForm()
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)

def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")

class NotesDetailView(generic.DetailView):
    model=Notes

def todo(request):
    if request.method == "POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            try:
                finished= request.POST["is_finished"]
                if finished == 'on':
                    finished= True
                else:
                    finished= False
            except:
                finished=False
            todos=Todo(
                user=request.user,
                title=request.POST['title'],
                is_finished=finished
            )
            todos.save()
            messages.success(request,f"Todo added from {request.user.username}!!")
    else:
        form=TodoForm()
    todo=Todo.objects.filter(user=request.user)
    if len(todo) == 0:
        todos_done = True
    else:
        todos_done= False
    context={
        'form':form,
        'todos':todo,
        'todos_done':todos_done,
    }
    return render(request,"dashboard/todo.html",context)

def update_todo(request,pk=None):
    todo=Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todo')

def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect("todo")

def register(request):
    if request.method== 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"account created")
    else:
        form = UserRegistrationForm()
    context={
       'form':form
    }
    return render(request,"dashboard/register.html",context)


def prep(request):
    return render(request,'dashboard/prep.html')

def courses(request):
    return render(request,'dashboard/courses.html')


