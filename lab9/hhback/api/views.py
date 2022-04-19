from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
# Create your views here.
from api.models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(vacancy.to_json())

def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(company.to_json())

def vacancies_with_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    vacancies = company.vacancies.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def top_ten_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary', 'name')[:10]
    vacancies_json = [vacancy.top_ten() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)