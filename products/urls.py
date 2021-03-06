"""langatlas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from .views import ProductViewSet, DownloadViewSet, ProceessSentenceView

urlpatterns = [
    path('download/<slug:category>/<str:subject>/<str:subcategory>/<slug:contrast>', DownloadViewSet.as_view({
        'get': 'download_individual'
    })),

    path('download/<slug:category>', DownloadViewSet.as_view({
        'get': 'download_category'
    })),

    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),

    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    path('products/sentence_space/', ProceessSentenceView.as_view({
        'put': 'process_sentences',
    }))
]
