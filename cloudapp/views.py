from django.shortcuts import render,redirect,get_object_or_404
from cloudapp import *
from pkgapp import *
from tpaapp import *
from userapp.models import *
from cloud_upload.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q,F

# Create your views here.


def cloud_dashboard(request):
    data=UserUploadFile.objects.filter(cloud_audit_request_status='RequestPending').count()
    data2=UserUploadFile.objects.filter(cloud_audit_request_status='Accepted').count()
    data5=UserUploadFile.objects.filter(cloud_audit_request_status='RequestPending')|UserUploadFile.objects.filter(cloud_audit_request_status='Accepted')
    if request.method=="POST" and 'btn2'in request.POST :
            
            
        search=request.POST.get('search')
            
        print(search)
        data5=(UserUploadFile.objects.filter(cloud_audit_request_status='RequestPending')|UserUploadFile.objects.filter(cloud_audit_request_status='Accepted')).filter(Q(file_type__icontains=search)|Q(file_name__icontains=search)|Q(user_creator__user_email__icontains=search)|Q(user_creator__user_name__icontains=search))
        
        
    return render(request,'cloud/cloud-dashboard.html',{'data1':data,'data5':data2,'data':data5})

def cloud_crbt_details(request):
    data=UserUploadFile.objects.filter(cloud_audit_request_status='Accepted').all()
    if request.method=="POST" and 'btn2'in request.POST :
            
            
        search=request.POST.get('search')
            
        print(search)
        data=(UserUploadFile.objects.filter(cloud_audit_request_status='Accepted')).filter(Q(file_type__icontains=search)|Q(file_name__icontains=search)|Q(user_creator__user_email__icontains=search)|Q(user_creator__user_name__icontains=search))
        
        
    return render(request,'cloud/cloud-crbt-details.html',{'data':data})

def cloud_audit_request(request,id):
    data = get_object_or_404(UserUploadFile,file_id=id)
    data.cloud_audit_request_status = 'Accepted'
    data.save(update_fields=['cloud_audit_request_status'])
    data.save()
    print("this is accept")
    
    return redirect('cloud_audit_certificate')

def cloud_audit_certificate(request):
    # data=UserUploadFile.objects.all()
    data=UserUploadFile.objects.filter(cloud_audit_request_status='RequestPending').all()
    if request.method=="POST" and 'btn2'in request.POST :
            
            
        search=request.POST.get('search')
            
        print(search)
        data=(UserUploadFile.objects.filter(cloud_audit_request_status='RequestPending')).filter(Q(file_type__icontains=search)|Q(file_name__icontains=search)|Q(user_creator__user_email__icontains=search)|Q(user_creator__user_name__icontains=search))
        
    return render(request,'cloud/cloud-audit-certificate.html',{'data':data})

def cloud_signin(request):
    if request.method=='POST':
        name=request.POST.get('email') 
        password=request.POST.get('password') 
        if name=='cloud@gmail.com' and password=='cloud123':
           return redirect('cloud_dashboard')
    return render(request,'user/cloud-login.html')



