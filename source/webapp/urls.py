from django.urls import path
from webapp.views import main_view, info_view

urlpatterns = [
    path('', main_view),
    path('info/', info_view, name='info'),
]