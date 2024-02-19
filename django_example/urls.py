from django.urls import path, include

urlpatterns = [
    path('api/', include('django_example.movies.urls')),
    path('users/', include('django_example.users.urls'))
]
