from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length = 300)
    slug = models.SlugField(unique = True, blank = True, null = True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length = 300)
    slug = models.SlugField(unique = True, blank = True, null = True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Blog(models.Model):
    status = [
        (0, 'Draft'),
        (1, 'Published')
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique = True, blank = True, null = True)
    content = RichTextField()
    post_status = models.IntegerField(choices = status, default = 0)
    tags = models.ManyToManyField(Tag, null = True, blank = True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    # Featured image

    def __str__ (self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
