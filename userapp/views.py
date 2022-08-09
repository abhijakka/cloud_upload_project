from ast import Not
from ntpath import join
from tkinter.filedialog import SaveAs
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404,HttpResponseRedirect
from cloudapp.models import *
from pkgapp.models import *
from tpaapp.models import *
from userapp.models import *
from django.contrib import messages
import re
from django.db.models import Q,F

from cloud_upload.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.core.files.storage import FileSystemStorage

# Create your views here.


# home
def home(request):
  
    return render(request,'user/index.html')

def about(request):
    return render(request,'user/about.html')

def contact(request):
    return render(request,'user/contact.html')

# user

def user_dashboard(request):
    
    user= request.session['user_id']
    data=UserUploadFile.objects.filter(user_creator=user).all()
    
 

    if request.method=="POST" and 'btn2'in request.POST :
        print('abhi5555')
        search=request.POST.get('search')
        
        print(search)
         
       
      
        data2=UserUploadFile.objects.filter(user_creator=user).filter(Q(file_type__icontains=search)|Q(file_name__icontains=search))
        print(data2)
        
            
    
        return render(request,'user/user-dashboard.html' ,{'data':data2,'search':search})   
       
    
    
    return render(request,'user/user-dashboard.html')

def user_file_audit(request):
    user= request.session['user_id']
    data=UserUploadFile.objects.filter(user_creator=user).filter(User_audit_request_status='Accepted')
    return render(request,'user/file-audit.html',{'data':data})

def user_dycreption_download_key(request,id):
    print(id)
    
   
   
    
    
    if request.method=="POST" and 'button-download'in request.POST :   
            data2= UserUploadFile.objects.filter(file_id=id).update(download_rank=F('download_rank')+1)
            print(data2)
            
            
            
    data = UserUploadFile.objects.get(file_id = id)
    
    
    print(data.download_genrate_key)
    if request.method == "POST" and 'button-check'  in request.POST:
        security_key = request.POST['security']
        print(security_key)
        print("llllppppppwewrweqrqtwerwtw")
       
        if data.download_genrate_key == security_key:
            download = True
            print("Trueee")
        else:
            download = False
            print("Falseeee")
        return render(request,'user/user-download-encription.html',{'d':download,'data':data})
    elif request.method == "POST" and 'button-download'  in request.POST:
        print("asasasasas")
        download = True
        print("table create successfully!!")
        return render(request,'user/user-download-encription.html',{'d':download,'data':data})
    
    return render(request,'user/user-download-encription.html')

def user_dynamic_operations(request,id):
    # user= request.session['user_id']
        
                  
        user1=UserUploadFile.objects.filter(file_id=id).update(view_rank=F('view_rank')+1)
        
        print(user1)
        
        
        if request.method=="POST" and 'btn2'in request.POST :
              
            search=request.POST.get('text')
            
            print(search)
           
            data1= UserUploadFile.objects.filter(file_id=id).update(update_rank=F('update_rank')+1)
            print(data1)
        
       
        if request.method=="POST" and 'btn5'in request.POST :   
            data2= UserUploadFile.objects.filter(file_id=id).update(download_rank=F('download_rank')+1)
            print(data2)
        
    
        data=UserUploadFile.objects.filter(file_id=id)
    # text=get_object_or_404(UserUploadFile,file_id=id)
       
    
    
    
        for i in data:
            a=i.upload_file 
            path='media/'+ str(a)
            print(path)
            # file = open(path,'r')
            # file_data=str(file.read())
            file = open(path,'r')    
            file_data=str(file.read())
            print(file_data)
            
            file.close()
            if request.method =='POST':
            
               text = request.POST.get("text")
               f = open( path, 'w')
               f.write (re.sub('\n' ,'',text))
               f.close()
               file = open(path,'r')    
               file_data=str(file.read())
               file_data= re.sub('\n+\r+', '', text)
               print(file_data)
               file.close()
               file=messages.success(request,"Your File Is Successfully Updated")  
               return redirect('user_dynamic_operations',id=id)     
        else:
            pass
        # try:
            #    h = open( path, 'r+')
            #    j=str(h.read())
            #    j= re.sub('\n+\r+', '', text)
            #    print(j)
            #    j.close()
                
                
            # return redirect('user_dynamic_operations')
        #    if request.method =='POST':
        #         text = request.POST.get("text",None)
        #         if text is not None:
        #             f = open( path, 'w+')
        #             f.write(text)
        #             f.close()
                # return redirect('user_dynamic_operations')
                
                #   file = open(path,'w+')
                #   file_data=str(file.write())
                #   print(file_data)
            #   file = open(path,'w')    
            #   file_data=str(file.write())
        
            #   file.close()
            
        # except :
        #     pass 
            
    
        return render(request,'user/dynamic.html',{'data':data,'data2':file_data})
    
    
def user_download_pending(request,id):
        
    data = get_object_or_404(UserUploadFile,file_id=id)
     #file encryption start
   
    
    data.user_download_status = 'PendingRequest'
    data.save(update_fields=['user_download_status',])
    data.save()
    print("this is accept")
    
    
            
    
   
    return redirect('user_myfile')

def user_myprofile(request):
    user= request.session['user_id']
    data=UserRegistrationModel.objects.filter(user_id=user)
    user=get_object_or_404(UserRegistrationModel,user_id=user)
    if request.method =='POST' :
          
        user_name=request.POST.get('user_name')
        user_password=request.POST.get('user_location')

        user_gender=request.POST.get('user_gender')
        user.user_name=user_name
        user.user_password=user_password

        user.user_gender=user_gender
        user.save(update_fields=['user_name','user_password','user_gender'])
        user.save()
        if user:
                messages.success(request,"Your Profile is Updated")       
        else:
            pass
        
    return render(request,'user/user-profile.html',{'data':data})



def user_upload(request):
    user= request.session['user_id']
    data=UserRegistrationModel.objects.get(user_id=user)
    supported_extensions= {'py':'py','txt':'txt','css':'css','html':'html','js':'js','java':'java'}
    if request.method =='POST' and request.FILES['file_image']:
          
        file_name=request.POST.get('file_name')
        file_describition=request.POST.get('file_describition')
        file_type=request.POST.get('file_type')
        print(file_type,'juui')
        # supported_files=['txt','html','css','py']
        upload_file=request.FILES['file_image']
        
        print(upload_file)
        file_size=upload_file.size
        # file_post_name=request.POST.get('file_image')
        file_post_name=upload_file.name
        ff=FileSystemStorage()
        name=ff.save('media/'+file_post_name,upload_file)
        print(name)
        
        file_extension = file_post_name
        print(file_extension)
        #start find index...
        def find(string, char):
            for i, c in enumerate(string):
                if c == char:
                    yield i

        string = file_extension
        char = "."
        indices = list(find(string, char))
        print(indices)
        print(indices[-1]) 

        start_index = indices[-1]
        end_index = len(file_extension)
        x =  file_extension[start_index+1:end_index]
        print("kkkkk")
        print(x,file_type)
        print("jjjj")
        a=(supported_extensions[file_type])
        print(a)
        if a in x:
            print('sucessful')
        else:
            print('fail')

        if a in x:
            print(x,'something')
            
            cloud=UserUploadFile.objects.create(file_post_name=file_post_name,upload_file=upload_file,user_creator=data,file_size=file_size,file_name=file_name,file_describition=file_describition,file_type=file_type)
            cloud.save()
            if cloud:
              messages.success(request,"Your File Is Successfully Uploaded")       
        else:
              messages.info(request,"please check filetype and Upload file type is different ") 
            
         

    
    return render(request,'user/user-uploadfile.html')

def user_myfile(request):
    user= request.session['user_id']
    data=UserUploadFile.objects.filter(user_creator=user)
    if request.method=="POST" and 'btn2'in request.POST :
              
            search=request.POST.get('search')
            
            print(search)
            data=UserUploadFile.objects.filter(user_creator=user).filter(Q(file_name__icontains=search)|Q(file_type__icontains=search))
            data1= UserUploadFile.objects.filter(user_creator=user).filter(Q(file_name__icontains=search)|Q(file_type__icontains=search)).update(search_rank=F('search_rank')+1)
            print(data1)
    if request.method=="POST" and 'btn5'in request.POST :   
            data2= UserUploadFile.objects.filter().update(download_rank=F('download_rank')+1)
            print(data2)
    
    return render(request,'user/user-myfiles.html',{'data':data})
def user_audit_request(request,id):
    data = get_object_or_404(UserUploadFile,file_id=id)
    data.User_audit_request_status = 'RequestPending'
    data.save(update_fields=['User_audit_request_status'])
    data.save()
    print("this is accept")
    if data:
            messages.success(request,"Your Request is Successfully Sent")       
    else:
            pass
    
    
    return redirect('user_myfile')


def user_signup(request):
    if request.method =='POST' and request.FILES['user_upload']:
          
        user_name=request.POST.get('user_name')
        user_email=request.POST.get('user_email')
        user_gender=request.POST.get('user_gender')
        user_password=request.POST.get('user_password')
        user_upload_image=request.FILES['user_upload']
        if UserRegistrationModel.objects.filter(user_email=user_email).exists():
                messages.error(request,"Email Already Existed")
                return redirect("user_signup")
        else:
            user=UserRegistrationModel.objects.create(user_name=user_name,user_email=user_email,user_password=user_password,user_upload_image=user_upload_image,user_gender=user_gender)
            user.save()
        
        if user:
            messages.success(request,"Your Registration Form Is Successfully Uploaded")       
        else:
            pass
    return render(request,'user/user-singup.html')

def user_login(request):
    if request.method == 'POST': 
                email = request.POST.get('user_email') 
                password = request.POST.get('user_password') 
                try: 
                     check = UserRegistrationModel.objects.get(user_email=email,user_password=password) 
                     print('abhi')  
                     request.session['user_id']=check.user_id  
                       
                     user_status = check.user_status 
                     if user_status =='Accepted': 
                         messages.success(request,'login success') 
                         return redirect('user_dashboard')  
                     elif user_status =='Rejected' :  
                         messages.error(request,'Your request is Rejected so you cannot login')   
                     elif user_status == 'Pending': 
                         messages.info(request,'Your request is Pending so cannot login')   
                except: 
                     messages.warning(request,'invalid login') 

                
    return render(request,'user/user-login.html')