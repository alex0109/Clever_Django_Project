from django.contrib import admin
from blog.models import Post, Comment
# from markdownx.admin import MarkdownxModelAdmin

from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
	list_display = ('title', 'status', 'author', 'created_date')
	list_filter = ('status',)
	search_fields = ['title', 'text']
	summernote_fields = ('description', 'text',)

# class PostAdmin(SummernoteModelAdmin):
# 	summernote_fields = ('description', 'text',)
	
admin.site.register(Post, PostAdmin)
# admin.site.register(Post, PostAdmin, PostSummerAdmin)

# admin.site.register(Post, MarkdownxModelAdmin)


# class PostAdmin(MarkdownxModelAdmin):
# 	list_display = ('title', 'created_date', 'published_date')
# 	list_filter = ('created_date', 'published_date')
# 	search_filter = ('title')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'body', 'post', 'created_on', 'active')
	list_filter = ('active', 'created_on')
	search_fields = ['name', 'email', 'body']
	actions = ['approve_comments']

	def approve_comments(self, request, queryset):
		queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)
