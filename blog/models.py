from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog_category', kwargs={'slug': self.slug})


class Tag(models.Model):
    tag_name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name


class Blog(models.Model):
    caption = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption + str(self.publish_time)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog_category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-publish_time']








