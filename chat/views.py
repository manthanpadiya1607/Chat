from django.shortcuts import render, redirect
from .models import Room, Message, signup
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def home(request):
    return render(request, 'home1.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/chat/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/chat/'+room+'/?username='+username)

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

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['passw']

        user = auth.authenticate(username=username, password=passw)
        if user is not None:
            auth.login(request, user)
            return redirect("/chat")
        else:
            messages.info(request, "invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email_id = request.POST['email_id']
        passw = request.POST['passw']

        if User.objects.filter(username=username).exists():
            messages.info(request, "username taken")
            return redirect('register')
        elif User.objects.filter(email=email_id).exists():
            messages.info(request,"Email-id already registered")
            return redirect('register')

        else:
            signup = User.objects.create_user(username=username, first_name=name, email=email_id, password=passw)
            signup.save()

        print("User Created")
        return redirect('login')

    else:
        return render(request,'register.html')


@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token = AuthToken.objects.create(user)

    return Response({
        'user_info':{
            'username': user.username,
            'passw': user.passw
        },
        'token': token
    })

