from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.home, name ="home"),
    path("about/",views.about, name="about"),
    path("contact/", views.contact, name ="contact"),
    path("product/",views.product, name="product"),
    path("register/",views.register, name="register"),
    path("dashboard/",views.dashboard, name ="dashboard"),
    path("update/<int:pk>",views.update,name="update"),
    path("student/",views.StudentList.as_view(),name="student"),
    path("student_details/<int:id>/",views.StudentDetail.as_view(),name="student_details")
]
