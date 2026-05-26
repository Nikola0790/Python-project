"""
URL configuration for nikolaslab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from edu.views import show_number
from django_1.views import (
    hello,
    drawn_number,
    random_max_number,
    random_number,
    hello_name,
    articles,
    bands_albums,
    number_range_view,
    form,
    temp_convert,
    set_session,
    show_session,
    delete_session,
    my_view,
    add_to_session,
    show_all_session,
    set_cookie,
    show_cookie,
    delete_cookie,
    add_to_cookie,
    show_all_cookies,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/<int:number>", show_number),
    path("hello/", hello),
    path("random/", drawn_number),
    path("random/<int:max_num>/", random_max_number),
    path("random/<int:min_number>/<int:max_number>/", random_number),
    path("random/<str:name>/", hello_name),
    path("articles/", articles),
    path("albums/<int:number>", bands_albums),
    path("numbers/", number_range_view),
    path("form/", form),
    path("temp/", temp_convert),
    path("set-session/", set_session),
    path("show-session/", show_session),
    path("delete-session/", delete_session),
    path("login/", my_view),
    path("add-to-session/", add_to_session),
    path("show-all-session/", show_all_session),
    path("set-cookie/", set_cookie),
    path("show-cookie/", show_cookie),
    path("delete-cookie/", delete_cookie),
    path("add-to-cookie/", add_to_cookie),
    path("show-all-cookies/", show_all_cookies),
]
