from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'blogposts', views.BlogPostViewSet)
router.register(r'blogquotes', views.BlogQuoteViewSet)
router.register(r'blogcategories', views.BlogCategoryViewSet)
router.register(r'pages', views.PagesViewSet)
router.register(r'socialmedialinks', views.SocialMediaLinkViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))]