from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    path('', views.article_report, name='home'),
    path('api/', include(router.urls)),
    # We will add other URLs here
    path('fetch-articles/', views.fetch_external_articles, name='fetch-articles'),
    path('report/', views.article_report, name='article-report'),
]