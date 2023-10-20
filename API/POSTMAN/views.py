from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Alumno
import json
# Create your views here.


class AlumnosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, idAlumno=0):
        if(idAlumno > 0):
            alumnos=list(Alumno.objects.filter(idAlumno=idAlumno).values())
            if len(alumnos) > 0:
                alumno=alumnos[0]
                datos={'message':"Success","alumnos":alumno}

            else:
                datos={'message':"alumnos not found..."}
            return JsonResponse(datos)
        else:
            alumnos=list(Alumno.objects.values())
            if len(alumnos)>0:
                datos={'message':"Success","alumnos":alumnos}
            else :
                datos={'message':"alumnos not found..."}
            return JsonResponse(datos)

    def post(self,request):
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,idAlumno):
        jd = json.loads(request.body)
        alumnos=list(Alumno.objects.filter(idAlumno=idAlumno).values())
        if len(alumnos) > 0:
            alumno=Alumno.objects.get(idAlumno=idAlumno)
            alumno.idAlumno=jd['idAlumno']
            alumno.Gmail=jd['Gmail']
            alumno.Contrasena=jd['Contrasena']
            alumno.nombreAlumno=jd['nombreAlumno']
            alumno.save()
            datos={'message':"Success"}
        else :
            datos={'message':"alumnos not found..."}
        return JsonResponse(datos)

    def delete(self,request,idAlumno):
        alumnos = list(Alumno.objects.filter(idAlumno=idAlumno).values())
        if len(alumnos) > 0:
            Alumno.objects.filter(idAlumno=idAlumno).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)

