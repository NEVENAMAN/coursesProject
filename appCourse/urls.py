from django.urls import path
from . import views

urlpatterns = [
    path('',views.Course_page),
    path('add_course',views.add_course),
    path('del_course',views.del_course),
    path('confirm_delete',views.confirm_delete),
    path('comment_on_course_page',views.comment_on_course_page),
    path('comment_on_course_process',views.comment_on_course_process),
    path('view_comment_page',views.view_comment_page),
]