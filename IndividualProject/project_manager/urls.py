from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.project, name='project'),
    path('<int:id>/task/', views.task_list, name='task_list'),
    path('<int:id>/feature/', views.feature_list, name='feature_list'),
    path('<int:id>/bug/', views.bug_list, name='bug_list')

]
