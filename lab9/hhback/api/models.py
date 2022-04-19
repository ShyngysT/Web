from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='company description')
    city = models.CharField(max_length=200, default='Almaty')
    address = models.TextField(default='company address')

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    def to_short_json(self):
        return{
            'id': self.id,
            'name': self.name
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='vacancy description')
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company_id': self.company.id
        }

    def top_ten(self):
        return{
            'name': self.name,
            'salary': self.salary
        }