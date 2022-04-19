from django.urls import path
from api.views.views_fbv import company_list, company_detail, vacancy_list, vacancy_detail, company_vacancies
from api.views.view_cbv import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, VacancyDetailAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:id>/', CompanyDetailAPIView.as_view()),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:id>/', VacancyDetailAPIView.as_view()),
    path('companies/<int:id>/vacancies/', company_vacancies)
]

# from django.urls import path
# from api.views.fbv_view import company_list, company_detail, company_vacancies,VacancyListAPIView, VacancyDetailAPIView
#
# from rest_framework_jwt.views import obtain_jwt_token
#
# urlpatterns = [
#     path('login/', obtain_jwt_token),
#
#     path('companies/',company_list),
#     path('companies/<int:company_id>/', company_detail),
#     path('companies/<int:pk>/vacancies/', company_vacancies),
#     path('vacancies/',VacancyListAPIView.as_view()),
#     path('vacancies/<int:vacancy_id>/',VacancyDetailAPIView.as_view()),
#     #path('vacancies/top_ten/',vacancies_top_ten)
# ]
