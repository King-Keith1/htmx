from django.urls import path
from .views import home, user_card

urlpatterns = [
    path('', home, name='home'),  # New default route
    path('user/<int:user_id>/', user_card, name='user_card'),
]


