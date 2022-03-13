from django.urls import path,include
import helloworld.views

urlpatterns = [
    path('helloworld', helloworld.views.hello),
    path('rtjson', helloworld.views.rtjson),
    path('login', helloworld.views.post),
    path('get', helloworld.views.get)






]