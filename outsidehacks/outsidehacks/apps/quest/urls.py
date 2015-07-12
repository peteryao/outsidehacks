from django.conf.urls import url, include
from outsidehacks.apps.quest import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'zones', views.ZoneViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'badges', views.BadgeViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'quests', views.QuestViewSet)
router.register(r'user_quests', views.UserQuestViewSet)
router.register(r'user_badges', views.UserBadgeViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]