from django.db import models

from company.models import Company
from company.models import Employee


class Notice(models.Model):
    receiver_company = models.ForeignKey(
                Company,
                related_name='receiver',
                on_delete=models.DO_NOTHING)
    sender_company = models.ForeignKey(
                Company,
                related_name='sender',
                on_delete=models.DO_NOTHING)
    service_id = models.CharField(max_length=50)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    work_description = models.CharField(max_length=500)
    sender_employee = models.ForeignKey(
                Employee,
                related_name='sender',
                on_delete=models.DO_NOTHING)
    receiver_employee = models.ForeignKey(
            Employee,
            related_name='receiver',
            on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{}".format(self.service_id)
