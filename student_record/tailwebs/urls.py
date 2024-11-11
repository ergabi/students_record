from django.urls import path
from .views import register_view, login_view,Dashboard_view,home,Record_create,Records_update,Record_delete,logout

urlpatterns = [
    path('',home,name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/',Dashboard_view, name='dashboard'),
    path('create/',Record_create,name='Record_create'),
    path('update/<int:id>/',Records_update,name='Records_update'),
    path('delete/<int:id>/',Record_delete,name='Record_delete'),
    path('logout/', logout, name='logout'),
]
