from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from projectOLM.forms import UserRegisterForm, UserAuthForm, EduForm
from django.contrib.auth import login, authenticate, logout
#from . forms import EduForm
def register(request):
    if request.method == "POST":
        #form = UserRegisterForm()
        form1 = UserAuthForm(request, data = request.POST)
        form2 = UserRegisterForm(request.POST)
        edu = EduForm(request.POST)
    #   print('sadsad')
        if form1.is_valid():

            if True:
                user = authenticate(username=form1.cleaned_data['username'], password=form1.cleaned_data['password'])

                #edu.user_id = user.id
                #print('---------------------')

                #print('---------------------')
                #edu.save()
            else:
                pass
                #print('Nono req')
                #user = None
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/accounts/register')
        else:

            if form2.is_valid():

                if edu.is_valid():
                    instances = form2.save(commit=False)

                    instances.save()
                    place = edu.save(commit=False)
                    place.user = instances
                    place.save()

                    login(request, instances)
                else:
                    #print(edu)
                    return HttpResponseRedirect('/accounts/register')
            else:
                return HttpResponse('404')
        context = {'form': form1, 'edu': edu}

        return HttpResponseRedirect('/accounts/register')
    else:
        #edu = EduForm()
        #print(edu)
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            form1 = UserAuthForm()
            form2 = UserRegisterForm()
            edu = EduForm()
            print(edu)

            c = {'form1': form1, 'form2': form2, 'edu': edu}
            return render(request, 'index2.html', c)
def logoutU(request):
    logout(request)
    return HttpResponseRedirect('/')