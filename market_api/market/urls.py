from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import OziqlistApiView


router=SimpleRouter()

router.register("oziq",OziqlistApiView,basename='product')
urlpatterns=router.urls

