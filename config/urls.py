"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# ad_2: importação da função de inclusão
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # ad_3: Inclusão da aplicação (o que é passado aqui como parâmetro, não existe ainda, mas existirá)
    path('', include('_app.urls'))
]

# as_2: Var que referencia o local do template que trata templates inexistentes
handler404 = '_app.views.handler404'
