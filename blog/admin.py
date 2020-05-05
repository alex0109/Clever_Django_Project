from django.contrib import admin
from blog.models import Post
from markdownx.admin import MarkdownxModelAdmin

from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
	summernote_fields = ('description', 'text',)

admin.site.register(Post, PostAdmin)

# admin.site.register(Post, MarkdownxModelAdmin)


# class PostAdmin(MarkdownxModelAdmin):
# 	list_display = ('title', 'created_date', 'published_date')
# 	list_filter = ('created_date', 'published_date')
# 	search_filter = ('title')