from django.urls import path
from . import views

urlpatterns = [
    path('insert',views.makeCreate),
    path('inserts',views.makeList),
    path('page',views.makePage)
 
 

]