from rest_framework.routers import DefaultRouter
from inventario.api.views import ProductosViewSet

router = DefaultRouter()
router.register('productos',ProductosViewSet,basename='producto')

urlpatterns = router.urls
