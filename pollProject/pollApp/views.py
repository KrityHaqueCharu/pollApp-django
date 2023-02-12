from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import Question
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Vote
import django.utils.datetime_safe
from django.db import migrations, models
from datetime import datetime


# Create your views here.

@login_required(login_url="signin/")
def index(request):
    
    latest = Question.objects.order_by('-pub_date')[:5] #getting all the questions
    context = {
        'latest':latest,
    }
    return render(request,'pollApp/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #ekta specific question er jonno etar corresponding option gula dekhacche
    return render(request,'pollApp/detail.html',{'question': question})


def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id) 
    # vote_count=get_object_or_404(Question,pk=question_id)
    # Profile=get_object_or_404(user=request.user)
    print(question)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])  #ami ekhane select korsi choice
    except:
        return render(request, 'pollApp/detail.html',{'question':question,'error_message':"Please select a choice"})
    else:
        selected_choice.votes += 1
        # selected_choice.option += selected_choice
        selected_choice.save()
        user=request.user
        record_vote(user=user, question=question, choice=selected_choice)

        return HttpResponseRedirect(reverse('pollApp:results', args=[question_id], ))

# def voted(request):
#     try:
#         # question=get_object_or_404(Question,pk=question_id)
#         Profile=get_object_or_404(user=request.user)
#         # selected_choice=question.choice_set.get(pk=request.POST['choice'])
#     except Exception as e:
#         profile= None
#         print('Exception : ', e)
#         context={
#             'profile': profile,
#         }
#         return render(request,'pollApp/profile.html',context)

def voted(request):
    Profile=Vote.objects.all()
    for a in Profile:
        print(a)
    context={
        'profile': Profile,
    }
    return render(request,'pollApp/profile.html',context) 




# @login_required(login_url="signin/")
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'pollApp/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.user.add(request.user)
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('pollApp:results', args=(question.id,)))



def results(request, question_id):
    question= get_object_or_404(Question,pk=question_id)
    return render(request, 'pollApp/result.html', {'question':question})

def signin(request):
    if(request.method=='GET'):
        return render(request, 'pollApp/login.html')
    elif(request.method=='POST'):
        u=request.POST.get('username','')
        p=request.POST.get('password','')

        res=authenticate(username=u,password=p)
        if(res is None):
            return HttpResponse('<h1>Sign In Failed. You cannot Vote</h2>')
        else:
            login(request,res)
            return redirect('pollApp:index')

def signout(request):
    logout(request)
    return redirect('pollApp:poll-login')

def record_vote(user, question , choice ):
    print(user, question , choice)
    timestamp = models.DateTimeField(auto_now_add=True)
    voted = Vote(user=user,poll=question,option=choice)
    voted.save()
     