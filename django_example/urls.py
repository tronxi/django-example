from django.urls import path, include

urlpatterns = [
    path('api/', include('movies.urls')),
    path('users/', include('users.urls'))
]
