from django.urls import path

from . import views

urlpatterns = [

    path(""), #/challengs/
    path("<int:month>", views.monthly_challengs_by_number),
    path("<str:month>", views.monthly_challengs, name="month_challeng")


]
