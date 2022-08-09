"""cloud_upload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from userapp import views as user_views
from cloudapp import views as cloud_views
from pkgapp import views as pkg_views
from tpaapp import views as tpa_views

urlpatterns = [
    # home
    
    
    path('admin/', admin.site.urls),
    path('', user_views.home,name='home'),
    path('about', user_views.about,name='about'),
    path('contact', user_views.contact,name='contact'),
    
    # user
    
    path('user_dashboard', user_views.user_dashboard,name='user_dashboard'),
    path('user_file_audit', user_views.user_file_audit,name='user_file_audit'),
    path('user_myprofile', user_views.user_myprofile,name='user_myprofile'),
    path('user_upload', user_views.user_upload,name='user_upload'),
    path('user_myfile', user_views.user_myfile,name='user_myfile'),
    path('user_signup', user_views.user_signup,name='user_signup'),
    path('user_login', user_views.user_login,name='user_login'),
    # path('', user_views.,name=''),
    # path('', user_views.,name=''),
    # path('', user_views.,name=''),
    path('user_download_pending/<int:id>/', user_views.user_download_pending,name='user_download_pending'),
    path('user_audit_request/<int:id>/', user_views.user_audit_request,name='user_audit_request'),
    path('user_dynamic_operations/<int:id>/', user_views.user_dynamic_operations,name='user_dynamic_operations'),
    path('user_dycreption_download_key/<int:id>/', user_views.user_dycreption_download_key,name='user_dycreption_download_key'),
   
    
    path('cloud_dashboard', cloud_views.cloud_dashboard,name='cloud_dashboard'),
    path('cloud_crbt_details', cloud_views.cloud_crbt_details,name='cloud_crbt_details'),
    path('cloud_audit_certificate', cloud_views.cloud_audit_certificate,name='cloud_audit_certificate'),
    path('cloud_signin', cloud_views.cloud_signin,name='cloud_signin'),
    path('cloud_audit_request/<int:id>/', cloud_views.cloud_audit_request,name='cloud_audit_request'),
    
    
    path('pkg_dashboard', pkg_views.pkg_dashboard,name='pkg_dashboard'),
    path('pkg_user_details', pkg_views.pkg_user_details,name='pkg_user_details'),
    path('pkg_user_genrating_key/<int:id>/', pkg_views.pkg_user_genrating_key,name='pkg_user_genrating_key'),
    path('pkg_user_Rejected/<int:id>/', pkg_views.pkg_user_Rejected,name='pkg_user_Rejected'),
    path('pkg_user_request', pkg_views.pkg_user_request,name='pkg_user_request'),
    path('pkg_signin', pkg_views.pkg_signin,name='pkg_signin'),
    
    path('tpa_audit_request_to_cloud/<int:id>/', tpa_views.tpa_audit_request_to_cloud,name='tpa_audit_request_to_cloud'),
    path('tpa_audit_sent_to_user/<int:id>/', tpa_views.tpa_audit_sent_to_user,name='tpa_audit_sent_to_user'),
    path('tpa_dashboard', tpa_views.tpa_dashboard,name='tpa_dashboard'),
    path('tpa_audit_challenge', tpa_views.tpa_audit_challenge,name='tpa_audit_challenge'),
    path('tpa_audit_view_challenge/<int:id>/', tpa_views.tpa_audit_view_challenge,name='tpa_audit_view_challenge'),
    path('tpa_user_details', tpa_views.tpa_user_details,name='tpa_user_details'),
    path('tpa_login', tpa_views.tpa_login,name='tpa_login'),
    path('download_request_accept/<int:id>/', tpa_views.download_request_accept,name='download_request_accept'),
    path('user_download_Rejected/<int:id>/', tpa_views.user_download_Rejected,name='user_download_Rejected'),
    path('user_download_request', tpa_views.user_download_request,name='user_download_request'),


      

    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)