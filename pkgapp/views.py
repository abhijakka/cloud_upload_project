from django.shortcuts import render,redirect,get_object_or_404
from cloudapp.models import *
from pkgapp.models import *
from tpaapp.models import *
from userapp.models import *
from cryptography.fernet import Fernet
from cloud_upload import check_internet
from cloud_upload.check_internet import *
from cloud_upload.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q,F
# Create your views here.

def pkg_dashboard(request):
    data=UserRegistrationModel.objects.all()
    data2=UserRegistrationModel.objects.filter(user_status='Pending').count()
    data3=UserRegistrationModel.objects.filter(user_status='Accepted').count()
    data6=UserRegistrationModel.objects.filter(user_status='Rejected').count()
    data5=UserRegistrationModel.objects.count()
    
    if request.method=="POST" and 'btn2'in request.POST :
            
            
        search=request.POST.get('search')
            
        print(search)
        data=UserRegistrationModel.objects.filter(Q(user_email__icontains=search)|Q(user_name__icontains=search))
        
        
    
    return render(request,'pkg/pkg-dashboard.html',{'data':data,'pending':data2,'accepted':data3,'data5':data5,'data6':data6})

def pkg_user_details(request):
  
    data3=UserRegistrationModel.objects.filter(user_status='Accepted')
    if request.method=="POST" and 'btn2'in request.POST :
            
            
        search=request.POST.get('search')
            
        print(search)
        data3=(UserRegistrationModel.objects.filter(user_status='Accepted')).filter(Q(user_email__icontains=search)|Q(user_name__icontains=search))

    return render(request,'pkg/pkg-user-details.html',{'data':data3})

def pkg_user_request(request):
   
    data=UserRegistrationModel.objects.all()
    if request.method=="POST" and 'btn2'in request.POST :
            
            
        search=request.POST.get('search')
            
        print(search)
        data=UserRegistrationModel.objects.filter(Q(user_email__icontains=search)|Q(user_name__icontains=search))
    return render(request,'pkg/pkg-user-request.html',{'data':data})
def pkg_user_genrating_key(request,id):
    
    data = get_object_or_404(UserRegistrationModel,user_id=id)
     #file encryption start
   
   
    data.user_status = 'Accepted'
    data.save(update_fields=['user_status'])
    data.save()
    print("this is accept")
    
     #email message
    if connect(): 
        html_content = "<br/> <p>   Your Application has been Accepted .</p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [data.user_email]
        
        # if send_mail (subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Cloud Storage Application Status",html_content,from_mail,to_mail)
        msg.attach_alternative(html_content,"text/html")
        try:
            if msg.send():
                print(msg)
                return redirect('pkg_user_request')
        except:
            pass
        #file encryption start
    # key_1 = Fernet.generate_key().decode()
    # print(key_1)
    
    # fernet = Fernet(key_1)
    # print(fernet)
   
    return redirect('pkg_user_request')

def pkg_user_Rejected(request,id):
    
    data = get_object_or_404(UserRegistrationModel,user_id=id)
     #file encryption start
   
  
    data.user_status = 'Rejected'
    data.save(update_fields=['user_status'])
    data.save()
    print("this is accept")
    
     #email message
    html_content =  "<br/> <p>   Your Application has been Rejected.Please Reapply it .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.user_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Cloud Storage Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    try:
        if msg.send():
            print(msg)
            return redirect('pkg_user_request')
    except:
        pass
            
    
   
    return redirect('pkg_user_request')

def pkg_signin(request):
    if request.method=='POST':
        name=request.POST.get('email') 
        password=request.POST.get('password') 
        if name=='pkg@gmail.com' and password=='pkg123':
           return redirect('pkg_dashboard')
    return render(request,'user/pkg-login.html')


