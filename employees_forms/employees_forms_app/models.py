from django.db import models


class Employee(models.Model):
    SOFTWARE_DEVELOPER = 1
    QA = 2
    DEV_OPS_SPECIALIST = 3

    GOOGLE = 'Google'
    SOFTUNI = 'Soft Uni'
    FACEBOOK = 'Facebook'
    COMPANIES = (GOOGLE, FACEBOOK, SOFTUNI)

    first_name = models.CharField(
        max_length=30
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        default='No Name'
    )

    eng = models.CharField(
        max_length=10,
        unique=True,
    )

    job_title = models.IntegerField(
        choices=(
            (SOFTWARE_DEVELOPER, 'Software Developer'),
            (QA, 'QA'),
            (DEV_OPS_SPECIALIST, 'DevOps Specialist'),
        )
    )

    company = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=((c, c) for c in COMPANIES),
    )

    image = models.ImageField(
        null=True,
        blank=True,
    )