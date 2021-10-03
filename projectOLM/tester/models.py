from django.db import models
from django.contrib.auth.models import User
class TypeQuestion(models.Model):
    type_name = models.CharField('type_name', max_length=64)
    def __str__(self):
        return self.type_name
class Olimpiada(models.Model):
    olimp_name = models.CharField('Olimp_name', max_length= 64)
    def __str__(self):
        return self.olimp_name
class Group(models.Model):
    name_group = models.CharField('name_group',max_length=64)
    def __str__(self):
        return self.name_group
class Question(models.Model):
    text_question = models.CharField('question', max_length=64)
    olimp_name = models.ForeignKey(Olimpiada, on_delete=models.CASCADE)
    type_question = models.ForeignKey(TypeQuestion, on_delete=models.NOT_PROVIDED)
    answer_onq = models.CharField('answer', max_length=64)
    chosing = models.CharField('choose', max_length=128)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def name_view(self):
        return self.text_question
    def list_choosing(self):
        #print(str(self.chosing).split(';'))
        return ((self.chosing).split(';'))

    def __str__(self):
        a = str(self.type_question)
        return a
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    olimp = models.ForeignKey(Olimpiada, on_delete=models.CASCADE)
    points = models.BigIntegerField()
    def __str__(self):
        return self.points




