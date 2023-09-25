# Create your views here.
from django.shortcuts import render
import pandas as pd
import requests

def display_variants(request):
    excel_data = pd.read_excel('lynx/data/disease.xlsx')
    data = excel_data.to_dict(orient='records')

    query = request.GET.get('q')
    filtered_data = data

    if query:
        # Filter the data based on the query
        filtered_data = [item for item in data if query in str(item)]

    return render(request, 'lynx/display_variants.html', {'data': filtered_data, 'query': query})


from django.shortcuts import render
import pandas as pd

def home(request):
    return render(request,'lynx/home.html')

def login(request):
    return render(request,'lynx/login.html')

def loginIN(request):
    return render(request,'lynx/loginIN.html')

def search(request):
    return render(request,'lynx/search.html')


def searchnew(request):
    return render(request,'lynx/searchnew.html')

def searchgene(request):
    return render(request,'lynx/searchgene.html')

def dhdds(request):
    return render(request,'lynx/dhdds.html')

def prpf3(request):
    return render(request,'lynx/prpf3.html')

def samd11(request):
    return render(request,'lynx/samd11.html')

def crb1(request):
    return render(request,'lynx/crb1.html')

def searchapi(request):
    return render(request,'lynx/searchapi.html')

from django.shortcuts import render
import pandas as pd

def filter_data(data, query):
    if query:
        return [item for item in data if query in str(item)]
    return data

def search(request):
    excel_data = pd.read_excel('lynx/data/disease.xlsx')
    data = excel_data.to_dict(orient='records')
    query = request.GET.get('q')
    filtered_data = filter_data(data, query)
    return render(request, 'lynx/search.html', {'data': filtered_data, 'query': query})

def search_results(request):
    query = request.GET.get('q')
    excel_data = pd.read_excel('lynx/data/disease.xlsx')
    data = excel_data.to_dict(orient='records')
    filtered_data = filter_data(data, query)
    return render(request, 'lynx/search_results.html', {'data': filtered_data, 'query': query})




    


