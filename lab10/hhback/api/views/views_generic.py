from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from api.models import Company
from api.serializers import CompanySerializer2


class CompanyListAPIView(UpdateAPIView):
    company = Company.objects.all()
    serializer_class = CompanySerializer2
    permission_classes = [IsAuthenticated,]