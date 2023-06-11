from django.urls import path
from . import views

urlpatterns=[
    path('studentinfo_get',views.studentinfo_get,name='studentinfo'),
    path('student_view',views.student_view,name='student_view'),
    path('student_update',views.student_update,name='student_update'),
    path('student_delete',views.student_delete,name='student_delete'),
    path('getstudentList',views.getstudentList,name='getstudentList')
    # path('student_update',views.student_update,name='student_update')
]