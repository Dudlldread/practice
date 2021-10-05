from django.contrib import admin

from .models import Question,Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model= Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldssets=[
        (None,              {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['colapse']}),
        #'pub_date','question_text']
    ]
    inlines=[ChoiceInline]
    list_display=('question_text','pub_date', 'was_published_recently')
    list_filter=['pub_date']
    search_fields=['question_text']

admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)