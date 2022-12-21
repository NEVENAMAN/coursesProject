from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def Course_page(request):
    course = GetCourses(request)
    context = {
        "courses" :course
    }
    return render(request,'add_course.html',context)

def add_course(request):
    error = Course.objects.basic_validator(request.POST)
    if len(error) > 0:
        for key,value in error.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        if request.method == "POST":
            AddCourse(request)
        return redirect('/')

def del_course(request):
    id = request.POST['del_course_id']
    course = Get_Course_info(id)
    context = {
        "course" : course
    }
    return render(request,'confirm_delete_page.html',context)

def confirm_delete(request):
    id = request.POST['del_course_id']
    Confirm_del_course(id)
    return redirect('/')

def comment_on_course_page(request):
    id = request.POST['comment_course_id']
    course = Get_Course_info(id)
    comment = Get_comment_info(request)
    context = {
        "course": course,
        "comments" : comment,
    }
    return render(request,'comment_course.html',context)

def view_comment_page(request):
    comment = Get_comment_info(request)
    context = {
        "comments" : comment,
    }
    return render(request,'comment_course.html',context)



def comment_on_course_process(request):
    if request.method == "POST":
        id = request.POST['comment_course_id']
        AddComment(request,id)
    return redirect('/view_comment_page')


