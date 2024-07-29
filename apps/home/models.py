from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Element(models.Model):
    ELEMENT_TYPES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('image', 'Image'),
        ('pdf', 'PDF'),
    ]
    title = models.CharField(max_length=100)
    element_type = models.CharField(max_length=10, choices=ELEMENT_TYPES)
    category = models.ForeignKey(Category, related_name='elements', on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, related_name='elements', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Data(models.Model):
    element = models.ForeignKey(Element, related_name='data', on_delete=models.CASCADE)
    value = models.TextField()

    def __str__(self):
        return self.value

# class Meta:
#         permissions = [
#             ("change_element", "Can change element"),
#             ("delete_element", "Can delete element"),
#         ]


class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/', null=True, blank=True)  # Allow null values temporarily
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
