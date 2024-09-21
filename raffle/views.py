from django.shortcuts import render, redirect
import pandas as pd
import random
from .models import ApplicantProfile
from django.conf import settings
from django.http import HttpResponse
from .forms import UploadFileForm
from django.core.mail import send_mail
from .tasks import send_mail_task
import re


def is_valid_email(email):
    email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(email_regex, email) is not None


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            df = pd.read_excel(request.FILES['file'])
            for index, row in df.iterrows():
                ApplicantProfile.objects.create(
                    applicant_name=row['applicant_name'],
                    applicant_email=row['applicant_email'],

                )

            raffle()
            return redirect('success')
        else:
            return HttpResponse('Form geçersiz', status=400)

    else:
        form = UploadFileForm()
        return render(request, 'upload_file.html', {'form': form})


def raffle():
    users = list(ApplicantProfile.objects.all())
    recipients = users[:]
    while True:
        random.shuffle(recipients)
        if all(user != recipient for user, recipient in zip(users, recipients)):
            assignments = dict(zip(users, recipients))
            for user, recipient in assignments.items():
                if not is_valid_email(recipient.applicant_email):
                    continue
                subject = f"Christmas Raffle Result for {user.applicant_name}"
                message = (
                    f"Hello {user.applicant_name},\nThis christmas, you have to buy a gift for {recipient.applicant_name}!"
                    f"\n\n HAVE FUN !")
                recipient_email = user.applicant_email
                send_mail_task.delay(subject, message,recipient_email)
        break


def success(request):
    return render(request, 'success.html')

















