from django.test import TestCase

from company.models import Company
from company.models import Employee
from notice.models import Notice


class ModelTests(TestCase):

    def test_model_str_notice(self):
        sample_company1 = Company.objects.create(name="AWS")
        sample_company2 = Company.objects.create(name="Optus")
        sample_employee1 = Employee.objects.create(
            name="John Adams",
            email="jon.adams@optus.com",
            company=sample_company2)
        sample_employee2 = Employee.objects.create(
            name="Mat Oram",
            email="mat.oram@aws.com",
            company=sample_company1)
        sample_notice = Notice.objects.create(
            receiver_company=sample_company1,
            sender_company=sample_company2,
            service_id="F23453",
            startTime='2020-05-14T00:15:00+00:00',
            endTime='2020-05-14T02:30:00+00:00',
            work_description="Updating the route configurations",
            sender_employee=sample_employee1,
            receiver_employee=sample_employee2
        )

        self.assertEqual(sample_notice.id, Notice.objects
                         .get(service_id="F23453").id)
