from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("root_admin/", include("root_admin.urls")),
    path("seller/", include("seller.urls")),
]
