from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

# Importamos nuestro método
from .utils import run_code


@api_view(['POST'])
def main(request):
    try:
        # Obtenemos el cuerpo de la petición
        body = request.body.decode('utf-8') if request.body else ""
        data = json.loads(body) if body else {}
    except Exception:
        return Response(
            {'code': 'Json Invalido'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Del JSON obtenemos el campo "text"
    code = data.get("text", "")

    # Ejecutamos instrucciones
    output = run_code(code)

    # Respuesta JSON
    return Response(
        {"output": output},
        status=status.HTTP_200_OK
    )
