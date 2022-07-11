from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from datetime import datetime
from Billing.models import Cust_Detals
# Create your views here.
x=0

def test(request):
    
    now = datetime.now()
    Today=now.strftime("%Y-%m-%d %H:%M:%S")
    # print(autoNumber)
    print("************"*4)
    print("Main Today: ",date.today())
    shopname="LAXMI DIE CUTTING CENTER"
    RECIVING="RECIVING"
    # x=0
    if request.method=='POST':
        global x
        x+=1
        
        print("form value")
        sr_no=request.POST.get("SRNO")
        Date=request.POST.get("Date")
        Cust_name=request.POST.get("Cust_name")
        number=request.POST.get("number")
        WK=request.POST.get("Kilo")
        WG=request.POST.get("Gram")
        Response=Cust_Detals(SR_No=sr_no,Date=Date,Cust_name=Cust_name,Mobile=number,WeightK=WK,WeightG=WG)
        Response.save()
        print(request.POST.get("SRNO"))
        print(request.POST.get("Date"))
        print(request.POST.get("Cust_name"))
        print(request.POST.get("number"))
        print(request.POST.get("Kilo"))
        print(request.POST.get("Gram"))

        print("form Submited")
    context={'ShopName':shopname,'RECIVING':RECIVING,'Today':Today,'autoNumber':"LDC-"+str(x)}
    
    return render(request,"home.html",context)