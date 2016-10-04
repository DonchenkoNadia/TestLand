from django.contrib import admin

# Register your models here.

from .models import Kontrolka, Ktr_Question, Ktr_Choice

class ChoiceInLine(admin.StackedInline):
	model = Ktr_Choice
	extra = 1

class Question_Admin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question_text']}),
	]
	inlines = [ChoiceInLine]

admin.site.register(Kontrolka)
admin.site.register(Ktr_Question, Question_Admin)