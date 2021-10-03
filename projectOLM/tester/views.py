import sqlite3

from django.db.backends.sqlite3.base import _sqlite_time_extract
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Question, Profile
from accounts.models import Group, EducationsUser
#from django.db import models
def index(request):
   #Если пользователь АВТОРИЗОВАН, то идёт поиск ответов этого пользователя, иначе - ***
   if request.user.is_authenticated:
      userGroup = EducationsUser.objects.get(user_id = request.user.id)
      if userGroup:
         #print(userGroup)
         #group_id = getattr(userGroup,'group')
         group_id = userGroup.group_id
      else:
         group_id = 1

      print(userGroup)
      alpha = Profile.objects.filter(user_id = request.user.id)
      if len(alpha) == 0:
         a = Question.objects.filter(group=group_id)
         b = []
         for i in a:

            b.append(i)
      else: #*** -
         b  = []
         #render(request, 'index1.html')
         alpha = Profile.objects.get(user_id=request.user.id)
         if alpha:
            h = {'g': alpha.points}
         else: pass
         return render(request, 'olimp.html', context=h)
   else: #*** - если не авторизован, то переход на регистрацию
      return HttpResponseRedirect('/accounts/register')
   return render(request, 'olimp.html', ({'b': b}))
def check(request):
   if request.user.is_authenticated:

      gr = EducationsUser.objects.get(user_id=request.user.id)
      if gr: pass
      else: gr = 1
      if request.method == "POST":
         a = Question.objects.filter(group=gr.group)
         b = len(a)
         s = 0
         for i in range(0, b):
            if a[i].answer_onq == request.POST.get(str(i+1)):
               s = s + 1
            #print(a[i].answer_onq)
            #print(request.POST.get(str(i+1)))
            #print('-----')
         alpha = Profile(user_id=request.user.id, olimp_id=1, points=s)
         alpha.save()
         return HttpResponseRedirect('/')
      else: s = 's'
   else: s = 's'
         #print(request['gender'])
   return HttpResponse(s)