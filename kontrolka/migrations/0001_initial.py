# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kontrolka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ktr_name', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
                ('sphere', models.CharField(max_length=150, verbose_name='Sphere of knowledge')),
                ('complexity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('creator', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Ktr_Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('iscorrect', models.BooleanField(default=False)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ktr_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('kontrolka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kontrolka.Kontrolka')),
            ],
        ),
        migrations.AddField(
            model_name='ktr_choice',
            name='ktr_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kontrolka.Ktr_Question'),
        ),
    ]