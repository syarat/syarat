from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


action = (
    ('Publish', 'Publish'),
    ('Draft', 'Save as a draft')
)


class Category(models.Model):
    category_url = models.SlugField(unique=True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'categorie'


class Tag(models.Model):
    tag_url = models.SlugField(unique=True)
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name


class Blog(models.Model):
    url = models.SlugField(unique=True, max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=150)
    thumbnail = models.ImageField(upload_to='media/thumbnails/', blank=True)
    article = RichTextUploadingField()
    action = models.CharField(choices=action, max_length=50, default='Draft')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     db_table = 'Blog'
