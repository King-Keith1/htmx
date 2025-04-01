from django.urls import path
from . import views

urlpatterns = [
    path('', views.example, name='home'),  # Add this for the root URL
    path('example/', views.example, name='example'),
    path('sample-post/', views.sample_post, name='sample-post'),
    path('edit/<int:message_id>/', views.edit_message, name='edit-message'),
    path('update/<int:message_id>/', views.update_message, name='update-message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete-message'),
]