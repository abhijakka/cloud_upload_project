from django.shortcuts import render,redirect,get_object_or_404
from cloudapp.models import *
from pkgapp.models import *
from tpaapp.models import *
from userapp.models import *
from cryptography.fernet import Fernet
from cloud_upload.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from cloud_upload import check_internet
from cloud_upload.check_internet import *
from django.db.models import Q,F
# Create your views here.


def tpa_dashboard(request):
    data5=UserUploadFile.objects.filter(User_audit_request_status='RequestPending') | UserUploadFile.objects.filter(User_audit_request_status='Accepted')
    if request.method=="POST" and 'btn2'in request.POST :
              
        search=request.POST.get('search')
            
        print(search)
        data5=(UserUploadFile.objects.filter(User_audit_request_status='RequestPending')|UserUploadFile.objects.filter(User_audit_request_status='Accepted')).filter(Q(file_name__icontains=search)|Q(user_creator__user_email__icontains=search)|Q(user_creator__user_name__icontains=search))
    data=UserUploadFile.objects.filter(User_audit_request_status='RequestPending').count()
    data2=UserUploadFile.objects.filter(User_audit_request_status='Accepted').count()
    pendingdownloads=UserUploadFile.objects.filter(user_download_status='PendingRequest').count()
    accepteddownloads=UserUploadFile.objects.filter(user_download_status='Accepted').count()
        
    return render(request,'tpa/tpa-dashboard.html',{'data1':data,'data5':data2,'data':data5,'pendingdownloads':pendingdownloads,'accepteddownloads':accepteddownloads})

def tpa_audit_challenge(request):
   
    data=UserUploadFile.objects.filter(User_audit_request_status='RequestPending')|UserUploadFile.objects.filter(User_audit_request_status='Accepted')
    if request.method=="POST" and 'btn2'in request.POST :
        
            
        search=request.POST.get('search')
            
        print(search)
        data=(UserUploadFile.objects.filter(User_audit_request_status='RequestPending')|UserUploadFile.objects.filter(User_audit_request_status='Accepted')).filter(Q(file_name__icontains=search)|Q(user_creator__user_email__icontains=search)|Q(user_creator__user_name__icontains=search))
        print(data)
    return render(request,'tpa/tpa-audit-challenges.html',{'data':data})

def tpa_audit_request_to_cloud(request,id):
    data = get_object_or_404(UserUploadFile,file_id=id)
    data.cloud_audit_request_status = 'RequestPending'
    data.save(update_fields=['cloud_audit_request_status'])
    data.save()
    print("this is accept")
    return redirect('tpa_audit_challenge')

def tpa_audit_view_challenge(request,id):
    data=UserUploadFile.objects.filter(file_id=id).all()
    
    if request.method == 'POST':
       print('abhi')
       User_audit_request_status = ('Accepted')
       user=UserUploadFile.objects.filter(file_id=id).update(User_audit_request_status=User_audit_request_status)
       for i in data:
            c=str(i.user_creator.user_email)
            print(c)
            
       #email message
       if connect():
        html_content = "<br/> <p>   Your Audit Application has been Accepted.Please check your Audit history section  .</p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [c]

            # if send_mail (subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Cloud Storage Application Status",html_content,from_mail,to_mail)
        msg.attach_alternative(html_content,"text/html")
        try:
                if msg.send():
                    print(msg)
                    return redirect('tpa_audit_view_challenge')
        except:
                pass
    # data=UserUploadFile.objects.filter(file_id=id).filter(cloud_audit_request_status='Accepted').all()
    return render(request,'tpa/tpa-audit-challange-view.html',{'data':data})

def tpa_audit_sent_to_user(request,id):
    data = get_object_or_404(UserUploadFile,file_id=id)
    data.User_audit_request_status = 'Accepted'
    data.save(update_fields=['User_audit_request_status'])
    data.save()
    print("this is accept")
    
   
    
    
    return redirect('tpa_audit_view_challenge')

def user_download_request(request):
    
    data=UserUploadFile.objects.filter(user_download_status='Pending')| UserUploadFile.objects.filter(user_download_status='Accepted')| UserUploadFile.objects.filter(user_download_status='Rejected')|UserUploadFile.objects.filter(user_download_status='PendingRequest')
    if request.method=="POST" and 'btn2'in request.POST :
        
            
        search=request.POST.get('search')
            
        print(search)
        data=(UserUploadFile.objects.filter(user_download_status='Pending')| UserUploadFile.objects.filter(user_download_status='Accepted')| UserUploadFile.objects.filter(user_download_status='Rejected')|UserUploadFile.objects.filter(user_download_status='PendingRequest')).filter(Q(file_type__icontains=search)|Q(file_name__icontains=search)|Q(user_creator__user_email__icontains=search)|Q(user_creator__user_name__icontains=search))
        print(data)
    return render(request,'tpa/tpa-download-request.html',{'data':data})
    

def download_request_accept(request,id):
    
    data5 = get_object_or_404(UserUploadFile,file_id=id)
    

    c=str(data5.user_creator.user_email)
    print(c)
     #file encryption start
    key_1 = Fernet.generate_key().decode()
    print(key_1)
    data5.download_genrate_key = key_1
    data5.user_download_status = 'Accepted'
    data5.save(update_fields=['user_download_status','download_genrate_key'])
    data5.save()
    print("this is accept")
    
     #email message
    if connect(): 
        html_content = "Your Key :" +data5.download_genrate_key +"<br/> <p>   Your Application has been Accepted .</p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [c]
        
        # if send_mail (subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Cloud Storage Application Status",html_content,from_mail,to_mail)
        msg.attach_alternative(html_content,"text/html")
        try:
            if msg.send():
                print(msg)
                return redirect('user_download_request')
        except:
            pass
            return redirect('user_download_request')

def user_download_Rejected(request,id):
    
    data = get_object_or_404(UserUploadFile,file_id=id)
     #file encryption start
    c=str(data.user_creator.user_email)
    print(c)
   
    data.download_genrate_key = 'Not genrated'
    data.user_download_status = 'Rejected'
    data.save(update_fields=['user_download_status','download_genrate_key'])
    data.save()
    print("this is accept")
    
     #email message
    if connect(): 
        html_content = "Your Key :" +data.download_genrate_key +"<br/> <p>   Your Application has been Rejected.Please Reapply it .</p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [c]
        
        # if send_mail (subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Cloud Storage Application Status",html_content,from_mail,to_mail)
        msg.attach_alternative(html_content,"text/html")
        try:
            if msg.send():
                print(msg)
                return redirect('user_download_request')
        except:
            pass
            
    
   
    return redirect('user_download_request')

def tpa_user_details(request):
    data=UserUploadFile.objects.filter(User_audit_request_status='Accepted').all()
    if request.method=="POST" and 'btn2'in request.POST :
            
            
        search=request.POST.get('search')
            
        print(search)
        data=(UserUploadFile.objects.filter(User_audit_request_status='Accepted')).filter(Q(file_type__icontains=search)|Q(file_name__icontains=search)|Q(user_creator__user_email__icontains=search)|Q(user_creator__user_name__icontains=search))
        print(data)
    
    return render(request,'tpa/tpa-user-details.html',{'data':data})

def tpa_login(request):
    if request.method=='POST':
        name=request.POST.get('email') 
        password=request.POST.get('password') 
        if name=='tpa@gmail.com' and password=='tpa123':
           return redirect('tpa_dashboard')
    return render(request,'user/tpa-login.html')
