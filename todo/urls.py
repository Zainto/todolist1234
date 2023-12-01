from django.urls import path
from . import views

urlpatterns=[

    path('addTask/',views.addTask, name="addTask"),
    path('mark_as_done/<int:pk>',views.mark_as_done, name="mark_as_done"),
    path('mark_as_undone/<int:pk>',views.mark_as_undone, name="mark_as_undone" ),
    path('edit/<int:pk>/',views.edit, name="edit"),
    path('delete_task/<int:pk>/',views.delete_task, name="delete_task")
]