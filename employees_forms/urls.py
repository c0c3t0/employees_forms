from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from employees_forms.employees_forms_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('employees/', include('employees_forms.employees_forms_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
