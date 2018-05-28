from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name="core"

urlpatterns = [

	#path('', index, name='index'),
	path('agenda', TemplateView.as_view(template_name='index.html')),
	#path('muda-status/<int:pk>', change_status, name='change_status'),
]