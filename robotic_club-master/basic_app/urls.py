from django.conf.urls import url
from basic_app import views
from store import views as views2
from django.conf import settings
from django.conf.urls import url
from django.urls import path

app_name='basic_app'

urlpatterns=[
   url(r'^signup/$',views.signup, name="signup"),
   url(r'^user_login/$',views.user_login, name="login"),
   url(r'^user_logout/$',views.user_logout, name="logout"),
   path("add_item/",views2.add_item,name="add_item"),
   path("item_view/",views2.item_view,name="item_view"),
   path("item_view/<int:pk>/", views2.item_detail, name="item_detail"),
   path("item_view/<int:pk>/delete/", views2.delete_item, name="delete_item"),
   path("request_mentor/<int:pk>/delete/", views2.delete_item, name="delete_item"),
   path("announcements/",views.announcements,name="announcements"),
   path("achievements/",views.achievements,name="achievements"),
   path("gallery/",views.gallery,name="gallery"),
   path("team/",views.team,name="team"),
   path("donate/",views.donate,name="donate"),
   path("request_mentor/",views2.request_mentor,name="request_mentor"),
   url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
   path("notification",views.notifications,name="create_notification"),
   path("view_announcements/",views.view_announcements,name="view_announcements"),
   path("view_announcements/<int:pk>",views.view_announcements_detail,name="view_announcements_detail"),
   path("delete_announcement/<int:pk>",views.delete_announcement,name="delete_announcement")
]
