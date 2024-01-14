from ckeditor.fields import RichTextField
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    thumbnail = models.ImageField(upload_to='blog/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="subcomments")
    email = models.EmailField()
    website = models.URLField(blank=True)
    message = models.TextField(max_length=500)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    @classmethod
    def comment_count_by_blog(cls, blog_id: int):
        return len(Comment.objects.filter(blog_id=blog_id))

    def has_parent(self):
        return True if self.parent else False

    def __str__(self):
        return self.name
