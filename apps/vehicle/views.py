from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status

from .models import Vehicle
from .serializers import VehicleSerializer, ReportSerializer


class VehicleViewset(GenericViewSet):
    serializer_class = VehicleSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, email: str = None):
        return Vehicle.objects.all().values(
            'licence_plate',
            'branch',
            'color',
            'comment',
            'person'
            )

    def list(self, request):
        vehicle_serializer = self.serializer_class(
            self.get_queryset(),
            many=True
            )
        return Response(vehicle_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {'message': 'infraction created!'},
                    status=status.HTTP_200_OK
                    )
            return Response(
                {'error': serializer.errors},
                status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                {'error': e.__str__()},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


@extend_schema(responses=ReportSerializer)
@api_view(['GET'])
def generate_report(request, *args, **kwargs):
    email = kwargs['email']
    report = (Vehicle.objects.select_related('person').
              values('created_date', 'licence_plate', 'comment').
              filter(person__email=email))
    report_serializer = ReportSerializer(report, many=True)
    return Response(report_serializer.data, status=status.HTTP_200_OK)
