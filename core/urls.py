from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import HomeTemplateView
from . import views 

urlpatterns = [
    # path('', home.as_view(), name='home'),
    # path('', views.home, name='home'),
    path('about/', views.about, name='about-page'),
    path('projects/', views.projects, name='projects-page'),
    path('', HomeTemplateView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
