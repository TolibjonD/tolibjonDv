from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class Comments(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    date_send = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="posts/", default="posts/default.jpg")
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return f"{self.id} - { self.title }"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Posts, self).save(*args, **kwargs)


class PostComments(models.Model):
    ismingiz = models.CharField(max_length=200)
    fikringiz = models.TextField(blank=True, null=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="reviews")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ismingiz
