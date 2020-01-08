from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .views import *
# from .models import Post, PostPicture
# from .models import Projects

admin.site.site_header = "Personal Portfolio"
admin.site.unregister(Group)


class DetailsAdmin(admin.ModelAdmin):
    list_display = ('first_name','short_description','user_email')

admin.site.register(About, DetailsAdmin)
admin.site.register(Skills)

def copy_project(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.title = object.title + ' (copy)'
        object.save()
    copy_project.short_description = "Duplicate selected projects"


class Project_Options_Admin(admin.ModelAdmin):
    actions = [copy_project]
    list_display = ('title','project_link')


    
admin.site.register(Projects, Project_Options_Admin)



