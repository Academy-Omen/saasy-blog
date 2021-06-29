from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField



class Profile(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile")
    bio = models.TextField(null=True, blank=True)
    twitter = models.URLField(max_length=200,null=True, blank=True)

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += ' ' + str(self.last_name)
        return name


class ArticleManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):

    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='author')

    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="article", default="placeholder.png")
    body = RichTextUploadingField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)


    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    
    status = models.CharField(max_length=10, choices=options, default='draft')

    objects = models.Manager()  # default manager
    articlemanager = ArticleManager()  # custom manager

    def get_absolute_url(self):
        return reverse('blog:article', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.headline
