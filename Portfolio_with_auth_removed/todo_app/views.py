from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer

from .ProjectScripts import whatsapp_control as wac

from .models import *

from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/todo-list/',
        'Detail View': '/todo-detail/<str:pk>/',
        'Create': '/todo-create/',
        'Update': '/todo-update/<str:pk>/',
        'Delete': '/todo-delete/<str:pk>/',
    }
    return Response(api_urls)

@csrf_exempt
@api_view(['POST', 'GET'])
def mobile_grabber(request):
    if request.is_ajax:
        request.session['mobnum'] = wac.to_whatsapp_number(number=request.POST.get('mobileNumber'))
        request.session.save()
    return HttpResponse('test')


@api_view(['POST', 'GET'])
def pincode(request):
    islocked = 'true'
    if request.is_ajax:
        pin_given = request.POST.get('Numlock')
        set_pin = '452'
        if set_pin == pin_given:
            islocked = 'false'

    data = {'islocked': islocked}
    return JsonResponse(data)

def todo_view(request):
    key = "123"
    testsession = SessionStore(session_key=key)
    testsession.save()
    sess = Session.objects.all()
    for s in sess:
        #print(dir(s))
        if s.get_decoded:
            print(s.get_decoded())

    #print("testsession:", sess.get_decoded())
    print("test0", request.session.session_key)
    context = {}
    return render(request, 'todo_list.html', context)

@api_view(['GET'])
def todoList(request):
    todo = Todo_list.objects.all().order_by('-id')
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
    todo = Todo_list.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def todoUpdate(request, pk):
    todo = Todo_list.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = Todo_list.objects.get(id=pk)
    todo.delete()
    return Response('deleted')


'''here be the sms section'''

def testsend_sms(request, mobile_number):
    wac.send_mssg("\u3053\u3093\u306B\u3061", mobile_number)
    return Response()

@api_view(['GET', 'POST'])
def todoList_sms(request, mobile_number):
    todo_request = sms_controller.request_data
    todo_list = [entry for entry in Todo_list.objects.values('list_item')]
    smscom_show = wac.WACom(todo_request, todo_list, mobile_number)
    smscom_show.show_Com()
    return Response()

@csrf_exempt
@api_view(['POST', 'GET'])
def todoCreate_sms(request, mobile_number):
    todo_request = sms_controller.request_data
    todo_list = []
    if Todo_list.objects.count() > 0:# This if statement stops the 'Nothing in list error'
        todo_list = [entry for entry in Todo_list.objects.values('list_item')]
        new_data = wac.WACom(todo_request, todo_list, mobile_number)
        serializer = TodoSerializer(data=new_data.add_Com())
        if serializer.is_valid():
            serializer.save()
            wac.send_mssg("item added", mobile_number)
        return Response(serializer.data)
    else:
        new_data = wac.WACom(todo_request, todo_list, mobile_number)
        serializer = TodoSerializer(data=new_data.add_Com())
        if serializer.is_valid():
            serializer.save()
            wac.send_mssg("item added", mobile_number)
        return Response(serializer.data)

@api_view(['POST', 'GET'])
def todoDelete_sms(request, mobile_number):
    todo_list = [entry for entry in Todo_list.objects.values('list_item')]
    todo_request = sms_controller.request_data
    remove_data = wac.WACom(todo_request, todo_list, mobile_number).remove_Com()
    try:
        todoremove = Todo_list.objects.get(list_item=remove_data)
        todoremove.delete()
        wac.send_mssg("Item Removed", mobile_number)
    except:
        wac.send_mssg(f"Item: does not exists", mobile_number)
    return Response('deleted')

@api_view(['POST', 'GET'])
def todoUpdate_sms(request, mobile_number):
    todo_list = [entry for entry in Todo_list.objects.values('list_item')]
    todo_request = sms_controller.request_data
    update_data = wac.WACom(todo_request, todo_list, mobile_number).update_Com()
    current_item = Todo_list.objects.get(list_item=update_data[0])
    serializer = TodoSerializer(instance=current_item, data=update_data[1])
    if serializer.is_valid():
        serializer.save()
        wac.send_mssg(f"*{update_data[0]}* has been changed to *{update_data[1]['list_item']}*", mobile_number)
    return Response(serializer.data)

commands = {"Testsend:":testsend_sms,
            "Add:": todoCreate_sms,
            "Show:": todoList_sms,
            "Remove:": todoDelete_sms,
            "Update:": todoUpdate_sms}
# This controls the other sms views
@csrf_exempt
@api_view(['POST', 'GET'])
def sms_controller(request):
    sess = Session.objects.all()
    for s in sess:
        print(s)
    request_request = request._request # This does nothing but stop everything from breaking.
    key = "123"
    sessionstore = SessionStore(session_key=key)
    print("test2", sessionstore.session_key)
    sms_controller.request_data = request.data
    mobile_number = wac.to_whatsapp_number(sessionstore['mobnum'])
    for cmd, func in commands.items():
        if sms_controller.request_data['list_item'].startswith(cmd):
            func(request_request, mobile_number)
            return Response()
        else:
            wac.send_mssg(f"invalid command. Try one of the following: {commands.keys()}", mobile_number)