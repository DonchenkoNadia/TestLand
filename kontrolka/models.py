from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Kontrolka(models.Model):
	"""Table with the most important information about Test"""
	ktr_name = models.CharField(max_length=150)
	pub_date = models.DateTimeField('Date published')
	sphere = models.CharField('Sphere of knowledge', max_length=150)
	complexity = models.DecimalField(max_digits=5, decimal_places=2)
	creator = models.CharField(max_length=300) 	
	description = models.TextField 
	def __str__(self):
		return self.ktr_name

class Ktr_Question(models.Model):
	"""The set of problems for each Test to be solved"""
	kontrolka = models.ForeignKey(Kontrolka, on_delete=models.CASCADE)
	question_text = models.CharField(max_length=200)
	def __str__(self):
		return self.question_text

class Ktr_Choice(models.Model):
	"""Variants to choice for each question in Test"""
	ktr_question = models.ForeignKey(Ktr_Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	iscorrect = models.BooleanField(default=False)
	votes = models.IntegerField(default=0)
	comment = models.TextField
	def __str__(self):
		return self.choice_text