from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
     path('dashboard/', views.dashboard, name="dashboard"),
    path('view_student/', views.students_views, name="students_views"),
    path('add_student/', views.students_add, name="students_add"),
    path('details_student/<int:id>/', views.student_details, name="student_details"),
    path('edit_student/<int:id>/', views.students_edit, name="student_edit") ,
    path('student_delete/<int:id>/',views.students_delete,name="students_delete"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
