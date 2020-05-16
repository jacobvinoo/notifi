from django.contrib import admin

from company.models import Company, Employee
from notice.models import Notice

# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Notice)
