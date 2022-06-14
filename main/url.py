from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name="home"),
    path('pagedetail/<int:id>', views.page_detail, name="pagedetail"),
    path('faq', views.faq_list, name="faq"),
    path('contact', views.contact_page, name="contact"),
    path('enquiry', views.enquiry, name="enquiry"),
    path('Gallery', views.news, name="Gallery"),
    path('Gallerydetail/<int:id>', views.news_detail, name="news_detail"),
    path('service_detail/<int:id>', views.service_detail, name="service_detail"),
    path('pricing',views.pricing,name="pricing"),
    path('accounts/signup',views.signup,name="signup"),
    path('checkout/<int:plan_id>',views.checkout,name="checkout"),
    path('checkout_session/<int:plan_id>',views.checkout_session,name="checkout_session"),
    path('pay_success',views.pay_success,name='pay_success'),
	path('pay_cancel',views.pay_cancel,name='pay_cancel'),
    #user dashboard section start
    path('user-dashboard',views.user_dashboard,name='user_dashboard'),
    path('update-profile',views.update_profile,name='update_profile'),
    #trainerlogin
    path('trainerlogin',views.trainerlogin,name='trainerlogin'),
    path('trainerlogout',views.trainerlogout,name='trainerlogout'),
    path('trainer_dashboard',views.trainer_dashboard,name='trainer_dashboard'),
    path('trainer_profile',views.trainer_profile,name='trainer_profile'),
    path('trainer_subscribers',views.trainer_subscribers,name='trainer_subscribers'),
    path('trainer_payments',views.trainer_payments,name='trainer_payments'),
    path('trainer_changepassword',views.trainer_changepassword,name='trainer_changepassword'),
    path('trainer_notifs',views.trainer_notifs,name='trainer_notifs'),
    #notification
    path('notifs',views.notifs,name='notifs'),
    path('get_notifs',views.get_notifs,name='get_notifs'),
    path('mark_read_notif',views.mark_read_notif,name='mark_read_notif'),
    #messages
    path('trainer_task',views.trainer_task,name='trainer_task'),
    path('mark_read_trainer_notif',views.mark_read_trainer_notif,name='mark_read_trainer_notif'),
    path('report_for_user',views.report_for_user,name='report_for_user'),
    path('report_for_trainer',views.report_for_trainer,name='report_for_trainer'),

    #pass
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "registration/reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/reset_password_complete.html"), name ='password_reset_complete')
    


]   
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 