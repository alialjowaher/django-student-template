from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Major

def home(request):
    courses_qs = Course.objects.all()
    return HttpResponse(f"List of courses: {',<br> '.join(course.name for course in courses_qs)}")    



