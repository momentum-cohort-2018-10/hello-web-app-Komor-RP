from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(Timestamp):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True)

    def get_absolute_url(self):
        return "/books/%s/" % self.slug

    def __str__(self):
        return self.name


class Social(models.Model):
    class Meta:
        verbose_name_plural = "Social Media Links"
    SOCIAL_TYPES = (
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('pinterest', 'Pinterest'),
        ('instagram', 'Instagram'),
    )
    network = models.CharField(
        max_length=255,
        choices=SOCIAL_TYPES)

    username = models.CharField(max_length=255)

    user = models.ForeignKey(
                             settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="social_acounts")


def get_image_path(instance, filename):
    return '/'.join(['book_images', instance.book.slug, filename])


class Upload(Timestamp):
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name="uploads")

    image = models.ImageField(upload_to=get_image_path)

    def save(self, *args, **kwargs):
        super(Upload, self).save(*args, **kwargs)
        if self.image:
            image = Image.open(self.image)
            i_width, i_height = image.size
            max_size = (1000, 1000)
            
            if i_width > 1000:
                image.thumbnail(max_size, Image.ANTIALIAS)
                image.save(self.image.path)
