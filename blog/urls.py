from django.urls import path
from . import views

urlpatterns =[
	# path('', views.index, name='index'),
	path('', views.post_list, name='post_list'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('post/', views.post_rev, name='post_rev'),
	path('post/<int:pk>/', views.post, name='post'),
]