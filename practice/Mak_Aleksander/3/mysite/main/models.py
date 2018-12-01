from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name)


class Poem(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=250, default='incognito')
    date = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='catalog_pic', null=True, blank=True, verbose_name='Фото')
    category = models.ManyToManyField('Category', blank=True, related_name='poems')

    def __str__(self):
        return '%s : %s' % (self.author, self.content)

    # class Meta:
    #     ordering = ['-date_pub']
