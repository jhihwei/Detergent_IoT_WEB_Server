from django.shortcuts import render, HttpResponse
from .models import sales
from django.db import connection

# Create your views here.
def root(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT terminal_id, max(gross_income) FROM sales GROUP BY terminal_id')
        row = cursor.fetchall()
        print(row)
    return render(request, 'index.html', {})

def maintain(request):
    return render(request, 'maintain.html')