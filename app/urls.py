from django.urls import path
from . views import home,login,signup,add_todo,signout,delete_todo,change_status



urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('signout/',signout,name='signout'),
    path('signup/',signup,name='signup'),
    path('add-todo/',add_todo,name='add_todo'),
    path('delete-todo/<int:id>/',delete_todo,name='delete_todo'),
    path('delete-todo/<int:id>/',delete_todo,name='delete_todo'),
    path('change-status/<int:id>/<str:status>',change_status,name='change_status'),
   
]


