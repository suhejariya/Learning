from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(QuesAns)
class QuesAnsAdmin(admin.ModelAdmin):
    list_display = ('ques','ans')