from django.contrib import admin

from .models import Question,Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldssets=[
        (None,              {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']}),
        #'pub_date','question_text']
    ]
admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)