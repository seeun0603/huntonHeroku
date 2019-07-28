from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from board.models import Board
from .models import Keyword
from django.http import JsonResponse
from signup.models import User

# Create your views here.
def main(request):
    return render(request, 'main/index.html')

def detail(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'post' : post})

def searchKeyword(request):
    keyword = request.GET.get('keyword')
    try:
        keyword_list = Keyword.objects.filter(key_name=keyword)
    except:
        keyword_list = None

    if keyword_list is None:
        overlap = "fail"
    else: 
        overlap = keyword_list
    context ={'overlap':overlap}
    return JsonResponse(context)

def mypage(request):
    return render(request, 'main/mypage.html', {'user' : user})