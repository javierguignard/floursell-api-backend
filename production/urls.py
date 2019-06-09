from django.urls import path
from production import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'api/product', views.ProductListCreate,'products')
router.register(r'api/report', views.ProducedReportListCreate,'products')

urlpatterns = router.urls