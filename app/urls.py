from rest_framework import routers
from .views import CatViewSets

router = routers.DefaultRouter()
router.register('cat', CatViewSets, basename='cat')

urlpatterns = router.urls