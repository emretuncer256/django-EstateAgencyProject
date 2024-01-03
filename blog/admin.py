from django.contrib import admin

from .models import Blog, Comment, Category


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
