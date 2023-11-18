from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# class Category(models.Model):
class Category(MPTTModel):
    STATUS = ( ('True', 'Evet'),('False', 'Hayir') )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = TreeForeignKey('self', blank=True, null=True,
                            related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title
    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('categoryProducts', kwargs={'slug': self.slug})

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join((full_path[::-1]))








class Product(models.Model):
    STATUS = (('True', 'Evet'),
        ('False', 'Hayir'), )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Category
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=True, upload_to='images/')
    # price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    price= models.FloatField()
    amount=models.IntegerField(default=0)
    detail=RichTextUploadingField()
    detail = models.TextField()
    status=models.CharField(max_length=10,choices=STATUS)

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('categoryProducts', kwargs={'slug': self.slug})

    def category_tag(self):
        return self.category
    category_tag.short_description = "Kategori"

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']