from django.contrib import admin

from .models import Blog, Comment, Category


class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "comments", "created_at", "if_updated_at"]

    search_fields = ("title",)
    readonly_fields = ("slug",)
    list_filter = ("category", "created_at")
    inlines = [CommentsInline]

    def comments(self, obj):
        count = Comment.comment_count_by_blog(obj)
        return count

    @admin.display(description="Updated At")
    def if_updated_at(self, obj):
        return obj.updated_at if obj.updated_at != obj.created_at else "-"


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
