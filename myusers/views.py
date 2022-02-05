from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import myusers
# Create your views here.

def register_view(request):
    if request.method == 'GET':
        return render(request, 'html/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        try:
            old_user = myusers.objects.get(username=username)
        except Exception as e:
            if password == repassword:
                user = myusers(username=username, password=password)
                user.save()
                print('注册成功')
                request.session['username'] = username
                request.session['password'] = password
                response = HttpResponseRedirect('/')
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                return response
            else:
                print('密码不一致')
                return render(request, 'html/register.html')
        else:
            print('用户名重复')
            return render(request, 'html/register.html')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'html/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            old_user = myusers.objects.get(username=username)
        except Exception as e:
            print('还未注册')
            return render(request, 'html/register.html')
        else:
            if password == old_user.password:
                print('登录成功')
                request.session['username'] = username
                request.session['password'] = password
                response = HttpResponseRedirect('/')
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                return response
            else:
                print('密码错误')
                return render(request, 'html/login.html')

def logout_view(request):
    if request.method == 'GET':
        request.session.clear()
        response = HttpResponseRedirect('/')
        response.delete_cookie('username')
        response.delete_cookie('password')
        return response
    elif request.method == 'POST':
        return render(request, 'html/init_html.html')