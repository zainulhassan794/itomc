from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ceo-hsn/', admin.site.urls),
    path('', include('web.urls')),
    path('student/' , include("django.contrib.auth.urls")),
    path('student/' , include("members.urls"))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "I2MC"
admin.site.site_title = "Admin"
admin.site.index_title = "I2MC Administration Area"

