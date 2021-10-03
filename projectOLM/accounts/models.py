from django.db import models
from django.contrib.auth.models import User
from tester.models import Group
class Town(models.Model):
    town_name = models.CharField('town_name', max_length=64)
    def __str__(self): return self.town_name


class EducationPlace(models.Model):
    name = models.CharField('name', max_length=64)
    town = models.ForeignKey(Town,on_delete=models.CASCADE)
    def __str__(self): return self.name

class EducationsUser(models.Model):
    #EduPlace_name = models.ForeignKey(EducationPlace)
    education_place = models.ForeignKey(EducationPlace, on_delete=models.CASCADE)
    town_name_of_EduPlace = models.ForeignKey(Town, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    #EduPlace_name = models.ForeignKey(EduPlace, on_delete=models.CASCADE)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)