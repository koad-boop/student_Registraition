from django.contrib import admin
from students.models import student

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','email','age','gender','qualification','img')
admin.site.register(student,StudentAdmin)    

# Register your models here.
