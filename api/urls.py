from django.urls import path
from rest_framework.authtoken import views as restviews
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'audio-book', views.AudioBookViewSet)

urlpatterns = [
    path('api-auth-token', views.CustomAuthToken.as_view()),

]

urlpatterns += router.urls