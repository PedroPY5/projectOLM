from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from accounts.models import EducationsUser,EducationPlace, Town
from tester.models import Group
class EduForm(forms.ModelForm):
    class Meta:
        model = EducationsUser

        town_name_of_EduPlace = forms.ModelChoiceField(queryset=Town.objects.all(),
                                                        empty_label=None,
                                                        to_field_name="town_name_of_EduPlace_name")
        education_place = forms.ModelChoiceField(queryset=EducationPlace.objects.filter(id=0),
                                          empty_label=None,
                                          to_field_name="eduPlace_name")
        group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                                 empty_label=None,
                                                 to_field_name="group")

        fields = ['town_name_of_EduPlace', 'education_place', 'group']
        widgets = {

            'town_name_of_EduPlace': forms.Select(attrs={'onchange':'f()'})
            #'town_name_of_EduPlace': forms.ChoiceField(choices=TownChoices)
        }

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        email = forms.EmailField(required=True)
        fields = ['username', 'email','password1','password2', 'last_name']
        #username = forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-input'})
        widgets = {
            'last_name': forms.TextInput(attrs={'placeholder': 'ФИО'}),
            'username' : forms.TextInput(attrs={'placeholder':'Введите ваш логин'}),
            'email': forms.TextInput({'placeholder':'Введите вашу почту'}),
            'password1': forms.PasswordInput(attrs={'placeholder': "Введите пароль"}),
            'password2': forms.PasswordInput(attrs={'placeholder': "Повторите пароль"})
        }
class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'email']