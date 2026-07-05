from django.contrib import admin

from .models import Course, Major   


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'credit', 'type', 'major', 'created_at')
    list_filter = ('type','major')
    search_fields = ('name',)


class MajorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','created_at')
    search_fields = ('name',)


admin.site.register(Course,CourseAdmin)
admin.site.register(Major,MajorAdmin)