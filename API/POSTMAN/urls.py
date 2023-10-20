from django.urls import path
from .views import AlumnosView

urlpatterns = [
    path('alumnos/', AlumnosView.as_view(), name='alumnos_list'),
    path('alumnos/<int:idAlumno>',AlumnosView.as_view(), name='alumnos_process')
]