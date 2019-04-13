from django.urls import path
from sells import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'api/customer', views.CustomerListCreate,'sells')
router.register(r'api/order', views.OrderListCreate,'sells')

urlpatterns = router.urls

