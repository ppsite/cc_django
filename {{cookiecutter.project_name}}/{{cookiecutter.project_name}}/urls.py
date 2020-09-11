"""{{cookiecutter.project_name}} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
{%- if cookiecutter.use_grappelli.lower() == 'y' %}
from filebrowser.sites import site
{%- endif %}
from django.conf import settings
from django.conf.urls.static import static

# 系统及第三方依赖路由
urlpatterns = [
    {%- if cookiecutter.use_drf.lower() == 'y' %}
    path('api-auth/', include('rest_framework.urls')),
    {%- endif %}
    {%- if cookiecutter.use_grappelli.lower() == 'y' %}
    path('admin/filebrowser/', site.urls),
    {%- endif %}
    {%- if cookiecutter.use_grappelli.lower() == 'y' %}
    path('grappelli/', include('grappelli.urls')),
    {%- endif %}
    path('admin/', admin.site.urls),
    {%- if cookiecutter.use_mdeditor.lower() == 'y' %}
    path('mdeditor/', include('mdeditor.urls')),
    {%- endif %}
]

# 自研 APP 路由
urlpatterns += [
    {%- if cookiecutter.use_account.lower() == 'y' %}
    path('<version>/account/', include('account.urls')),
    {%- endif %}
    {%- if cookiecutter.use_demo.lower() == 'y' %}
    path('<version>/project/', include('project.urls')),
    {%- endif %}
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
