from django.db import models
from django.contrib.auth.models import User  # Assuming you want to link to the User model

class Books(models.Model):
    book_name = models.CharField(max_length=1000, null=True, blank=True)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    book_file = models.FileField(upload_to='books/', null=True, blank=True)  # Field for book content

    def __str__(self):
        return self.book_name