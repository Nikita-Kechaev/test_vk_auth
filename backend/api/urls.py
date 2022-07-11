from django.urls import include, path

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
]