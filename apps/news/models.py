from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    """
    Post
    """
    title = models.CharField('News', max_length=100)
    image = models.FileField(upload_to='media/news/%Y/%m/%d')
    description = RichTextUploadingField()

    class Meta:
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title


# class Comment(models.Model):
#     """
#     Comment
#     """
