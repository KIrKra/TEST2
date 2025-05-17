from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная странциа',
        'values':['some','hello','blya']
    }
    return render(request,'main/index.html', data)

def lovenik(request):
    return render(request,'main/lovnik.html')
def onkrut(request):
    return render(request,'main/onkrut.html')
