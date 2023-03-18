from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import Quiz_Game
from django.contrib import messages
import random

# Create your views here.
name = ''
def home(request):
    if request.method == 'GET':
        global name 
        name = request.GET.get('name')

    return render(request, 'home.html')

def quizPage(request):
    numbering = range(1, len(Quiz_Game.questions)+1)
    # random.shuffle(Quiz_Game.questions)
    lst = zip(numbering, Quiz_Game.questions)
    return render(request, 'quiz.html', {'name' : name, 'questions' : lst})

score = 0
def answerCheck(request):
    if request.method == 'POST':
        global score
        for i in range(len(Quiz_Game.questions)):
            # print(request.POST[f'answer{i+1}'], Quiz_Game.questions[i]['correct_ans'])
            if str(request.POST.get(f'answer{i+1}')) == str(Quiz_Game.questions[i]['correct_ans']):
                # print(request.POST[f'answer{i+1}'], Quiz_Game.questions[i]['correct_ans'])
                score += 1
        messages.success(request, f'You scored {score}')
        return HttpResponseRedirect('/quizPage')

    # return render(request, 'quiz.html', {'name' : name, 'questions' : lst})

