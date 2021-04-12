from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from Student.models import Student
from django.db.models import Q
import pandas as pd

@login_required
def homepage(request):

    return render(request,'blog/home.html')

@login_required
def send_email_page(request):
    subject = 'CSE 309 - Fall 2020 - Section A'
    body = render_to_string('user/email_body.html')
    students = Student.objects.filter(Q(section='A1') | Q(section='A2'))

    for student in students:
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [student.student_id + '@uap-bd.edu']
        )

    return render(request,'blog/send_email.html',{'students':students})
