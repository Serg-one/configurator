from django.urls import path
from src import views

urlpatterns = [
    path('', views.platform, name="platform"),
    path('configurator/', views.configurator, name="configurator"),
    path('checkout/', views.update_current_config, name="checkout"),
    path('update_current_config/', views.update_current_config, name="update_current_config"),
]
