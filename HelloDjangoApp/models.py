from django.db import models
from django.utils import timezone


class Student(models.Model):
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_day = models.DateTimeField('Birthday')

    def __unicode__(self):
        return self.forename + ' ' + self.surname

    def approximate_age(self):
        return timezone.now().year - self.birth_day.year

    approximate_age.admin_order_field = 'birth_day'
    approximate_age.short_description = 'Age'
    #approximate_age.boolean = True     #this is for boolean type result


class Subject(models.Model):
    student = models.ForeignKey(Student)
    name = models.CharField(max_length=50)
    mark = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name + ': ' + str(self.mark)
