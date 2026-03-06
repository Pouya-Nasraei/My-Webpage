
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.post_list, name='home'),
    path('tag/<slug:tag_slug>/', views.post_list, name='index_tag'),
    path('<str:slug>/',views.post_detail, name='post_detail'),
    path('contact-me/',views.contact_me, name='contact_me'),

]