from django.urls import path
from . import views

urlpatterns = [
    path('insert',views.makeCreate),
    path('',views.makeList),
    path('show/<int:seriel>',views.makeRead),
    path('change/<int:num>',views.makeEdit),
    path('del/<int:unique>',views.makeDelete),
    path('page',views.makePage)
 
 

]