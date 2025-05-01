# energy_prediction/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from prediction import views as prediction_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Autenticação
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html',
        redirect_authenticated_user=True,
        next_page='dashboard'  # Redireciona para o dashboard após login
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    # Usuários
    path('profile/', user_views.profile, name='profile'),
    path('users/', user_views.user_list, name='user_list'),
    path('users/<int:pk>/', user_views.user_detail, name='user_detail'),
    path('users/new/', user_views.user_create, name='user_create'),
    path('users/<int:pk>/update/', user_views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', user_views.user_delete, name='user_delete'),
    
    # Predições
    path('', prediction_views.dashboard, name='dashboard'),
    path('predict/', prediction_views.predict, name='predict'),
    path('predictions/', prediction_views.prediction_list, name='prediction_list'),
    path('predictions/<int:pk>/', prediction_views.prediction_detail, name='prediction_detail'),
    path('predictions/<int:pk>/delete/', prediction_views.prediction_delete, name='prediction_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



