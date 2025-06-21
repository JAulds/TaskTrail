from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from TrailApp import views
from django.contrib import admin
from django.views.decorators.cache import cache_page

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task')

urlpatterns = [
    path('', cache_page(300)(views.TaskList.as_view()), name='home'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', cache_page(300)(views.TaskDetail.as_view()), name='task_detail'),
    path('api/v1/', include(router.urls)),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('task/<int:pk>/update_status/', views.update_task_status, name='update_task_status'),
]
