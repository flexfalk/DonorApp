from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Donor, Sample, Deadline, Price

admin.site.register(Donor)
admin.site.register(Sample)
admin.site.register(Deadline)
admin.site.register(Price)
