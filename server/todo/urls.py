from django.urls import path, include

from django.conf.urls import url
from .views import TodoAPIView

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', TodoAPIView, basename="todo")
urlpatterns = router.urls