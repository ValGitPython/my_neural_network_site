from django.contrib import admin
from django.urls import path
from app import views  # Убедитесь, что вы импортировали views из вашего приложения

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('applications/', views.applications, name='applications'),
    path('prompts/', views.prompts, name='prompts'),
    path('future/', views.future, name='future'),
    path('posts/', views.posts, name='posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]