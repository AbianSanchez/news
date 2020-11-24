from django.contrib import admin

from .models import Article, Comment

'''class CommentInline(admin.StackedInline): # List of comments
    model = Comment
    extra = 0  # Number of empty comments that appears after the comments'''

class CommentInline(admin.TabularInline): # List of comments simplified
    model = Comment
    extra = 0  # Number of empty comments that appears after the comments

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
