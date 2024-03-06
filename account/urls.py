from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', singup_view),
    path('sigin/<int:pk>/', singin_view),
    path('logoout/', logout),
]