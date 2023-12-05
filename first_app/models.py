from django.db import models

# Create your models here.

class StudentModel(models.Model):
    # roll = models.IntegerField(primary_key = True)
    # name = models.CharField(max_length = 10)
    # address = models.TextField()
    # auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    email_field = models.EmailField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    slug_field = models.SlugField()
    url_field = models.URLField()







    def __str__(self):
        return f"Roll: {self.roll} - {self.name}"