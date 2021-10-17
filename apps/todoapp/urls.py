from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    
    path('cls_home/', views.TaskListView.as_view(), name='cls_home'),
    
    path('cls_details/<int:pk>/', views.TaskDetailView.as_view(), name='cls_details'),
    
    path('cls_update/<int:pk>/', views.TaskUpdateView.as_view(), name='cls_update'),
    path('cls_delete/<int:pk>/', views.TaskDeleteView.as_view(), name='cls_delete'),
]
