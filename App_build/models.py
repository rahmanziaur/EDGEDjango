from django.db import models

# Create your models here.
class CsvUpload(models.Model):
    csv_file = models.FileField(upload_to='', verbose_name = 'Upload a CSV file')

class ClassifierInfo(models.Model):
    dataset = models.CharField(max_length=30)
    classifier_model = models.CharField(max_length=30)
    classifier_scaler = models.CharField(max_length=30)
    accuracy = models.CharField(max_length=30)
    f1score = models.CharField(max_length=30)
    precision = models.CharField(max_length=30)
    recall = models.CharField(max_length=30)