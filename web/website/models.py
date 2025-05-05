from django.db import models
from django.utils.deconstruct import deconstructible
from django.db.models import JSONField

# Create your models here.
class employee(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    password1=models.CharField(max_length=8)
    city=models.CharField(max_length=200)
    class Meta:
        db_table="register"



@deconstructible
class UniqueFileName:
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        return self.path

get_file_name = UniqueFileName('job_images/{uuid}_{filename}')


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads')  # Use the corrected function name and set null=True for optional field
    created_at = models.DateTimeField(auto_now_add=True)
    job_vacancies = JSONField(default=list)  # Use auto_now_add=True to set the field automatically upon creation

    def __str__(self):
        return self.title

class NonJob(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    job_vacancies = JSONField(default=list)

    def __str__(self):
        return self.title
    


class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
         
    