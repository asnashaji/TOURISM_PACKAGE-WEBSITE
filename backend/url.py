from django.urls import path
from backend import views

urlpatterns=[
    path('index/',views.index,name="index"),
    path('category/',views.category,name="category"),
    path('cat/',views.cat,name="cat"),
    path('pack/', views.pack, name="pack"),
    path('packages/', views.packages, name="packages"),
    path('viewcat/', views.viewcat, name="viewcat"),
    path('viewpack/', views.viewpack, name="viewpack"),
    path('viewcont/', views.viewcont, name="viewcont"),
    path('viewpay/', views.viewpay, name="viewpay"),
    path('viewcustamize/', views.viewcustamize, name="viewcustamize"),

    path('deletepage/<int:dataid>/', views.deletepage, name="deletepage"),
    path('deleteconct/<int:dataid>/', views.deleteconct, name="deleteconct"),
    path('deletecat/<int:dataid>/', views.deletecat, name="deletecat"),
    path('packedit/<int:dataid>/', views.packedit, name="packedit"),
    path('packupdate/<int:dataid>/', views.packupdate, name="packupdate"),
    path('catedit/<int:dataid>/', views.catedit, name="catedit"),
    path('catupdate/<int:dataid>/', views.catupdate, name="catupdate"),
    path('days/', views.days, name="days"),
    path('day/', views.day, name="day"),

]