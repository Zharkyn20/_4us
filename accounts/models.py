from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True)
    description = RichTextUploadingField()
