from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    fullname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    # employee_id = models.CharField(
    #     verbose_name="Employee ID", max_length=20, unique=True
    # )
    designation = models.CharField(max_length=200, blank=True, null=True)

    salary = models.IntegerField(default=0, blank=True, null=True)
    """amount detucted from salary"""
    deducted_salary = models.IntegerField(default=0, blank=True, null=True)
    """salary remaining after nessecary deductions"""
    final_salary = models.IntegerField(default=0, blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["fullname", "designation"]

    def __str__(self):
        return self.email


class EmployeeID(models.Model):
    unique_id = models.CharField(verbose_name="Employee ID", max_length=20, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
