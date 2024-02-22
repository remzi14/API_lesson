from .views import NewsViewSet
from rest_framework.routers import SimpleRouter
from django.urls import path

router=SimpleRouter()
router.register("new",NewsViewSet,basename='yangiliklar')

urlpatterns=router.urls

