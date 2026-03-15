from django.urls import path

from .views import *


urlpatterns = [

    path('', inicio, name="inicio"),

    path('about/', about, name="about"),

    path('pages/', PageList.as_view(), name="pages"),

    path('pages/<int:pk>/', PageDetail.as_view(), name="page_detail"),

    path('pages/create/', PageCreate.as_view(), name="page_create"),

    path('pages/<int:pk>/update/', PageUpdate.as_view(), name="page_update"),

    path('pages/<int:pk>/delete/', PageDelete.as_view(), name="page_delete"),

]