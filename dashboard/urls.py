from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('<str:room>/', views.room, name='room'), 
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('notes',views.notes,name="notes"),
    path('delete_note/<int:pk>',views.delete_note,name="delete-note"),
    path('notes_detail/<int:pk>',views.NotesDetailView.as_view(),name="note-detail"),
    path('todo',views.todo,name="todo"),
    path('update_todo/<int:pk>',views.update_todo,name="update_todo"),
    path('delete_todo/<int:pk>',views.delete_todo,name="delete_todo"),
    path('prep',views.prep,name="prep"),
    path('courses',views.courses,name="courses"),



]