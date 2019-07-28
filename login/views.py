from django.shortcuts import render,redirect
from signup.models import User
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.contrib import auth

# Create your views here.
def login(reqeust):
    return render(reqeust,'login/login.html')

def loginSucess(request):
    user_id = request.POST.get('user_id')
    user_pw = request.POST.get('user_pw')

    if request.session.get('id',False):
        erroMsg = request.session.get('id')+'님 반갑습니다.'
    elif User.objects.filter(user_id = user_id, user_pw = user_pw):
        request.session['id'] = user_id
        id = request.session.get('id')
        return render(request,'main/index.html',{'id':id})
    else:
        return redirect('home')


def logout(request):
    auth.logout(request)
    return render(request,'main/index.html')