# from django.urls import path, include
# from rest_framework import routers

# from tutorial.quickstart import views


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
from django.urls import path, include

urlpatterns = [
    path('', include('snippets.urls')),
]