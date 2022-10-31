from django.urls import path
from . import views

urlpatterns = [
    path('insert',views.makeCreate),
    path('home',views.makeList),
    path('show/<int:seriel>',views.makeRead),
    path('change/<int:num>',views.makeEdit),
    path('del/<int:unique>',views.makeDelete),
    path('person/<int:key>',views.makeViewParts),
    path('adding/<int:pos>',views.makeAddParts),
    path('rem/<int:key>/<str:name>',views.makeRemove),
    path('win/<int:key>/<str:name>',views.makeAnnounce),
    path('shortlist',views.makeShort),
    path('',views.makeLogin),
    path('out',views.makeLogout),
    path('page',views.makePage)
 
 

]