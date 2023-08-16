from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.utils import timezone
from hitcount.models import HitCount

from users.models import CustomUser
from ckeditor.fields import RichTextField

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = RichTextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    # hit countni tartiblashga kerak
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic')

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish_time',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_page", args=[self.slug])


class Comment(models.Model):
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    text = RichTextField()
    created_time = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return f'{self.name} by comments'