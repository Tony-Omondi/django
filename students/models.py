from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    date_of_admission = models.DateField()
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
