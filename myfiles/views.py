import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import Portfolio,Type,Services,Team,Murojaat,Obunamail
# Create your views here.

def index(malumot):
    if 'ObunaMail' in malumot.POST:
        email = malumot.POST.get('ObunaMail')
        Obunamail(mail=email).save()

    if 'subject' in malumot.POST:
        ismi = malumot.POST.get('name')
        mail = malumot.POST.get('email')
        mavzu = malumot.POST.get('subject')
        xabar = malumot.POST.get('message')
        vaqt = datetime.datetime.now()
        Murojaat(name=ismi,mail=mail,title=mavzu,text=xabar,date=vaqt).save()

    if 'search' in malumot.POST:
        text = str(malumot.POST.get('search'))
        text = text.strip()
        qidirish1 = Q(nomi__startswith = text)| Q(company_name__startswith=text)|\
                    Q(date__startswith=text)| Q(url__startswith=text)|\
                    Q(malumot__startswith=text)
        works = Portfolio.objects.filter(qidirish1)
        # * * *  * * * * * * * *
        qidirish2 = Q(nomi__startswith=text)
        turlar = Type.objects.filter(qidirish2)
        qidirish3 = Q(ismi__startswith=text)| Q(lavozimi__startswith=text)|\
                    Q(malumot__startswith=text)| Q(link1__startswith=text)|\
                    Q(link2__startswith=text)| Q(link3__startswith=text)| \
                    Q(link4__startswith=text)
        team = Team.objects.filter(qidirish3)
        qidirish4 = Q(nomi__startswith=text)| Q(malumot__startswith=text)
        servise = Services.objects.filter(qidirish4)
        return render(malumot, 'index.html', {'works': works, 'types': turlar, 'servise': servise, 'team': team})
    else:
        works = Portfolio.objects.all()
        servise = Services.objects.all()
        team = Team.objects.all()
        turlar = Type.objects.all()
    return render(malumot,'index.html',{'works':works,'types':turlar,'servise':servise,'team':team})

def filter_index(malumot,id):
    works = Portfolio.objects.filter(tur_id=id)
    return render(malumot,'index.html',{'works':works})

def portfolio_details(malumot):
    if 'ObunaMail' in malumot.POST:
        email = malumot.POST.get('ObunaMail')
        Obunamail(mail=email).save()
    return render(malumot,'portfolio-details.html')

def single_portfolio(malumot,id):
    work = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{'work':work})