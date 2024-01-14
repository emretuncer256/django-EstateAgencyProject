from django.contrib import admin

from .models import Blog, Comment, Category


class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    inlines = [CommentsInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["blog", "name", "message", "is_parent", "created_at"]
    search_fields = ["name", "message"]
    list_filter = ["blog", "created_at"]

    @admin.display(boolean=True)
    def is_parent(self, obj):
        return not obj.has_parent()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
