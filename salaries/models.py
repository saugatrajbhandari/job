from django.db import models


class Salary(models.Model):
    POSITION_JUNIOR = 'jr'
    POSITION_SENIOR = 'sr'
    POSITION_ASSOCIATE = 'as'
    POSITION_MANAGER = 'mgr'
    POSITION_LEAD = 'ld'

    POSITION_CHOICES = (
        (POSITION_JUNIOR, 'Junior'),
        (POSITION_SENIOR, 'Senior'),
        (POSITION_ASSOCIATE, 'Associate'),
        (POSITION_MANAGER, 'Manager'),
        (POSITION_LEAD, 'Lead')
    )

    EMPLOYEE_STATUS_CURRENT = 'crnt'
    EMPLOYEE_STATUS_EX = 'ex'

    EMPLOYEE_STATUS_CHOICES = (
        (EMPLOYEE_STATUS_CURRENT, 'Current Employee'),
        (EMPLOYEE_STATUS_EX, 'Ex Employee')
    )

    EXPERIENCE_ZERO = '0'
    EXPERIENCE_ONE = '1'
    EXPERIENCE_TWO = '2'
    EXPERIENCE_THREE = '3'
    EXPERIENCE_FOUR = '4'
    EXPERIENCE_FIVE = '5'
    EXPERIENCE_SIX = '6'
    EXPERIENCE_SEVEN = '7'
    EXPERIENCE_EIGHT = '8'
    EXPERIENCE_NINE = '9'
    EXPERIENCE_TEN = '10'
    EXPERIENCE_TEN_PLUS = '10+'

    YEAR_OF_EXPERIENCE_CHOICES = (
        (EXPERIENCE_ZERO, '0'),
        (EXPERIENCE_ONE, '1'),
        (EXPERIENCE_TWO, '2'),
        (EXPERIENCE_THREE, '3'),
        (EXPERIENCE_FOUR, '4'),
        (EXPERIENCE_FIVE, '5'),
        (EXPERIENCE_SIX, '6'),
        (EXPERIENCE_SEVEN, '7'),
        (EXPERIENCE_EIGHT, '8'),
        (EXPERIENCE_NINE, '9'),
        (EXPERIENCE_TEN, '10'),
        (EXPERIENCE_TEN_PLUS, '10+')
    )

    GENDER_MALE = 'ml'
    GENDER_FEMALE = 'fml'
    GENDER_OTHER = 'othr'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other')
    )
    role = models.CharField(max_length=255)
    salary = models.IntegerField()
    company_name = models.CharField(verbose_name='Company', max_length=255)
    company_website = models.URLField(verbose_name='Company Website')
    position = models.CharField(choices=POSITION_CHOICES, max_length=3)
    employee_status = models.CharField(verbose_name='Employee Status', choices=EMPLOYEE_STATUS_CHOICES, max_length=4)
    experience = models.CharField(verbose_name='Years Of Experience', choices=YEAR_OF_EXPERIENCE_CHOICES, max_length=3)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=4)

    def __str__(self):
        return f'Salary Info {self.id}'

    class Meta:
        ordering = ('-id',)



