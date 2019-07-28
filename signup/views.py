from django.shortcuts import render
from .models import User
from django.http import JsonResponse 

# Create your views here.
def signup(request):
    return render(request,'signup/signup.html')

#아이디 중복 검사
def id_overlap_check(request):
    username = request.GET.get('user_id')
    try:
        # 중복 검사 실패
        user = User.objects.get(user_id=username)
    except:
        # 중복 검사 성공
        user = None
    if user is None:
        overlap = "pass"
    else:
        overlap = "fail"
    context = {'overlap': overlap}
    return JsonResponse(context)  

def registerSuccess(request):
    if request.method == 'POST':
        user_pw = request.POST.get('user_pw')
        user = User (
            user_id = request.POST.get('user_id'),
            user_pw = request.POST.get('user_pw'),
            email = request.POST.get('email')
        )
        user.save()
    return render(request, 'login/login.html')
