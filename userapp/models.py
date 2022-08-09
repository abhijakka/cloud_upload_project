from django.db import models

# Create your models here.
class UserRegistrationModel(models.Model):
    
    user_id=models.AutoField(primary_key=True)
    user_name=models.TextField(help_text='Enter Your username' , max_length=50)
    user_email=models.EmailField(help_text='Enter email', max_length=50)
    user_password=models.CharField(help_text='user_password',max_length=200,null=True)
    user_gender=models.CharField(help_text='user_gender',max_length=200,null=True)
    user_key=models.CharField(help_text='user_key',max_length=200,null=True)
    user_reg_date=models.DateField(auto_now_add=True,null=True)
    user_status=models.CharField(help_text='user_status' ,default='Pending',max_length=200)
    user_upload_image=models.ImageField(help_text='user_upload_image ' , max_length=50,null=True)
    
    class Meta:
        db_table='user_registration_details' 

class UserUploadFile(models.Model):
       
    file_id=models.AutoField(primary_key=True) 
    user_creator=models.ForeignKey(UserRegistrationModel,models.CASCADE)
    file_name=models.CharField(help_text='upload_post_name',max_length=200,null=True)
    file_post_name=models.CharField(help_text='upload_post_name',max_length=200,null=True)  
    file_describition=models.TextField(help_text='upload describtion' , max_length=500)
    file_type=models.CharField(help_text='upload_type',max_length=200,null=True)
    file_size=models.CharField(help_text='upload_file',max_length=200,null=True)
    view_rank=models.CharField(help_text='view_rank',max_length=200,default=0)
    search_rank=models.CharField(help_text='view_rank',max_length=200,default=0)
    update_rank=models.CharField(help_text='view_rank',max_length=200,default=0)
    download_rank=models.CharField(help_text='view_rank',max_length=200,default=0)
    user_download_status=models.CharField(help_text='user_download_status',max_length=200,null=True)
    download_genrate_key=models.CharField(help_text='view_rank',max_length=200,null=True)
    upload_file=models.FileField(help_text='user_upload_image ' , max_length=50,null=True)
    User_audit_request_status=models.CharField(help_text='User_audit_request_status',max_length=200,default='Pending')
    # tpa_audit_request_status=models.CharField(help_text='tpa_audit_request_status',max_length=200,null=True)
    cloud_audit_request_status=models.CharField(help_text='cloud_audit_request_status',max_length=200,default='Pending')

    class Meta:
        db_table='user_upload_files_details'
        
