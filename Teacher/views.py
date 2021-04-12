from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def showTeacherPage(request):
    return HttpResponse("<H1>I am a teacher</H1>")

@login_required
def showTeacherInfoPage(request):
    return render(request,'Teacher/teacherInfoPage.html')

@login_required
def teacher_register(request):
    print(request.user.teacher)
    if request.method == "POST":
        print('request post')
        teacher_form = TeacherForm(request.POST,instance=request.user.teacher)
        if teacher_form.is_valid():
            print(teacher_form.instance.user.id)
            print(teacher_form.instance.id)
            teacher_form.save()

            return redirect('home')
        else:
            context = {
                'form' : teacher_form,
            }
            return render(request,'Teacher/teacher_register.html',context)

    else:
        print('request ---')
        teacher_form = TeacherForm()
        context = {
            'form' : teacher_form,
        }
        return render(request,'Teacher/teacher_register.html',context )

