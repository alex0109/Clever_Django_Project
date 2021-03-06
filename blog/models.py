from django.db import models
from django.conf import settings
from django.utils import timezone

# from markdownx.models import MarkdownxField
# from markdownx.utils import markdownify

STATUS = (
	(0, "Draft"),
	(1, "Publish"),
	)


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	# slug -> urls
	description = models.TextField(max_length=200)
	text = models.TextField()
	# text = MarkdownxField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	status = models.IntegerField(choices=STATUS, default=0)

	# @property
	# def formatted_markdown(self):
	# 	return markdownify(self.text)

	# def body_summary(self):
	# 	return Markdownify(self.body[:300] + "...")

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title



class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return 'Comment {0} by {1}'.format(self.body, self.name)
