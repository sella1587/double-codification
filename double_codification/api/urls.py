from django.urls import path
from .views import ConsolidatedDataView
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
app_name = 'accounts'
urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('getDataConsolided/', ConsolidatedDataView.as_view(), name='getDataConsolided'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),       
    
]
#npx tailwindcss -i ./static/ihm/css/input.css -o ./static/ihm/css/tailwind.css --watch

