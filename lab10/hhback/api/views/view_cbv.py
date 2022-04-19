from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer,CompanySerializer2


class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompanyDetailAPIView(APIView):
    def get_company(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, id):
        company = self.get_company(id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, id):
        company = self.get_company(id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, id):
        company = self.get_company(id)
        company.delete()
        return Response({'deleted': True})


class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VacancyDetailAPIView(APIView):
    def get_vacancy(self, id):
        try:
            return Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, id):
        vacancy = self.get_vacancy(id)
        serializer = CompanySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, id):
        vacancy = self.get_vacancy(id)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, id):
        vacancy = self.get_vacancy(id)
        vacancy.delete()
        return Response({'deleted': True})