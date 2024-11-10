from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo_list, name='todo_list'),  # 添加首页路由
    path('add/', views.add_todo, name='add_todo'),  # 添加新待办事项
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),  # 完成待办事项
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),  # 删除待办事项
]

