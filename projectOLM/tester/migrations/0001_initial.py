# Generated by Django 3.2.6 on 2021-09-30 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_group', models.CharField(max_length=64, verbose_name='name_group')),
            ],
        ),
        migrations.CreateModel(
            name='Olimpiada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olimp_name', models.CharField(max_length=64, verbose_name='Olimp_name')),
            ],
        ),
        migrations.CreateModel(
            name='TypeQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=64, verbose_name='type_name')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_question', models.CharField(max_length=64, verbose_name='question')),
                ('answer_onq', models.CharField(max_length=64, verbose_name='answer')),
                ('chosing', models.CharField(max_length=128, verbose_name='choose')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tester.group')),
                ('olimp_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tester.olimpiada')),
                ('type_question', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='tester.typequestion')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.BigIntegerField()),
                ('olimp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tester.olimpiada')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
