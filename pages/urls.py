from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    # when using Class-Based Views, you always add 'as_view()' at the end of views
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
