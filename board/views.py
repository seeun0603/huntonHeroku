from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from main.models import Keyword
from .models import Board, Comment, Like, User
from .forms import CommentForm, BoardForm

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'board/home.html', {'boards':boards})

def new(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit = False)
            board.date = timezone.now()
            board.save()
            return redirect('board/')
        else:
            form = BoardForm()
            return render(request, 'board/new.html', {'board' : board})
    else:
        return render(request, 'board/new.html')

def detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'board/detail.html', {'board' : board})

def delete(request, board_id):
    board = Board.objects.get(pk=board_id)
    board.delete()
    return redirect('/board/')  

def edit(request, board_id):
    board = Board.objects.get(pk = board_id)
    
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('/board/detail/' + str(board.id))
    else:
        form = BoardForm(instance=board)
        return render(request, 'board/edit.html', {'board':board, 'form':form})

def comment_create(request, board_id, user_id):
    if request.method == 'POST':
        board = get_object_or_404(Board, pk=board_id)
        user = get_object_or_404(User, pk=user_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.board = board
            comment.user_id = user_id
            comment.save()
        return redirect('board/' + str(board.id))
    else:
        form = CommentForm()
        return render(request, 'board/detail.html', {'form' : form})

def comment_edit(request, board_id, comment_id):
    board = Board.objects.get(pk = board_id)
    comment = Comment.objects.get(pk = comment_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('board/' + str(board.id))
        else:
            form = CommentForm(instance=comment)
            return render(request, 'board/edit.html', {'board':board, 'form':form})

def comment_delete(request, board_id, comment_id):
    board = get_object_or_404(Board, pk=board_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
        
    return redirect('board/' + str(board.id))    