from django.urls import path
from users.views import CustomUserCreate, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='register_user'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist')
]
