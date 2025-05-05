from django.contrib import admin
from website.models import*
from website.models import Job
from website.models import JobApplication
from website.models import NonJob


# Register your models here.
admin.site.register(employee)

admin.site.register(Job)


admin.site.register(JobApplication)


admin.site.register(NonJob)