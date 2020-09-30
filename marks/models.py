from django.db import models

# Create your models her
class student(models.Model):
    student1 = models.CharField(max_length=20, default=None)
    marks_maths=models.IntegerField()
    marks_science=models.IntegerField()
    marks_english=models.IntegerField()

    def __str__(self):
        return self.student1

class Employee(models.Model):
    name=models.CharField(max_length=20)
    Designation=models.CharField(max_length=20)
    Employee_id=models.IntegerField()
    DOB= models.DateField()


    def __str__(self):
        return self.name


