from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('accounts.urls')),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('accounts.urls')),  # ← Isso está faltando?
    path('api/', include('accounts.urls')),
]
