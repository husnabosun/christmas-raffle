from django.db import models


class ApplicantProfile(models.Model):
    applicant_name = models.CharField(max_length=128)
    applicant_email = models.EmailField()
