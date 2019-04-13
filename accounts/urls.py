from django.urls import path
from accounts import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'api/user_type', views.GetMyUserType)

urlpatterns = router.urls