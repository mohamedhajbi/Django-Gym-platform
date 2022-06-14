from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from froala_editor.fields import FroalaField
from phonenumber_field.modelfields import PhoneNumberField


import json


#banners
class Banners(models.Model):
    img=models.ImageField(upload_to="banners/")
    alt_text=models.CharField(max_length=100)

    class Meta:
	    verbose_name_plural='Banners'

    def __str__(self):
        return self.alt_text

    def image_tag(self):    
     return mark_safe('<img src ="%s" width="80" />'% (self.img.url))

     

class Service(models.Model):
    title=models.CharField(max_length=150)
    detail=FroalaField()
    img=models.ImageField(upload_to="services/",null=True)

    def __str__(self):
        return self.title

    def image_tag(self):    
     return mark_safe('<img src ="%s" width="80" />'% (self.img.url))

#pages
class Page(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()

    def __str__(self):
        return self.title

#FAQ
class Faq(models.Model):
	quest=models.TextField()
	ans=models.TextField()

	def __str__(self):
		return self.quest

#enquiry model
class Enquiry(models.Model):
	full_name=models.CharField(max_length=150)
	email=models.EmailField()
	detail=models.TextField()
	send_time=models.DateTimeField(auto_now_add=True)
        
	def __str__(self):
		return self.full_name  



#News model
class News(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField(max_length=500)
    img=models.ImageField(upload_to="news/",null=True)
    class Meta:
	    verbose_name_plural='Gallery'

    def __str__(self):
        return self.title

    def image_tag(self):    
     return mark_safe('<img src ="%s" width="80" />'% (self.img.url))

#News img
class NewsImage(models.Model):
    news=models.ForeignKey(News, on_delete=models.CASCADE,null=True)
    alt_text=models.CharField(max_length=150)
    img=models.ImageField(upload_to="news_imgs/",null=True)
    class Meta:
	    verbose_name_plural='Gallery Image'
    def __str__(self):
        return self.alt_text

    def image_tag(self):    
     return mark_safe('<img src ="%s" width="80" />'% (self.img.url))   
#subscription plan 
class SubPlan(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    max_member=models.IntegerField(null=True)
    highlight_status=models.BooleanField(default=False,null=True)
    validity_days=models.IntegerField(null=True)


    def __str__(self):
        return self.title

#subscription plan features
class SubPlanFeature(models.Model):
    #subplan=models.ForeignKey(SubPlan, on_delete=models.CASCADE)
    subplan=models.ManyToManyField(SubPlan)
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title


#package Discount
class PlanDiscount(models.Model):
    subplan=models.ForeignKey(SubPlan, on_delete=models.CASCADE,null=True)
    total_months=models.BigIntegerField()
    total_discount=models.BigIntegerField()
    def __str__(self):
        return str(self.total_months)       


#subscriber 
class Subscriber(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    mobile=PhoneNumberField()
    adress=models.TextField()
    img=models.ImageField(upload_to="subs/")

    def __str__(self):
        return str(self.user) 

    def image_tag(self):   
        if self.img: 
            return mark_safe('<img src ="%s" width="80" />'% (self.img.url))
        else:
            return 'no-image'


@receiver(post_save,sender=User)
def create_subscriber(sender,instance,created,**kwrags):
    if created :
        Subscriber.objects.create(user=instance)

#subscription 
class Subscription(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    plan=models.ForeignKey(SubPlan, on_delete=models.CASCADE,null=True)
    price=models.CharField(max_length=50)
    reg_date=models.DateField(auto_now_add=True,null=True)
    

#trainer
class Trainer(models.Model):
    full_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20,null=True)
    pwd=models.CharField(max_length=50,null=True)
    mobile=PhoneNumberField()
    adress=models.TextField()
    is_active=models.BooleanField(default=False)
    detail=models.TextField()
    img=models.ImageField(upload_to="trainers/")
    salary=models.IntegerField(default=0)

    Facebook=models.CharField(max_length=100,null=True,blank=True)
    Instagram=models.CharField(max_length=100,null=True,blank=True)
    Twitter=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.full_name) 
    def image_tag(self):   
        if self.img: 
            return mark_safe('<img src ="%s" width="80" />'% (self.img.url))
        else:
            return 'no-image'
# Notifications Json Response Via Ajax
class Notify(models.Model):
	notify_detail=models.TextField()
	def __str__(self):
		return str(self.notify_detail)

# Markas Read Notification By User
class NotifUserStatus(models.Model):
	notif=models.ForeignKey(Notify, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	status=models.BooleanField(default=False)

	class Meta:
		verbose_name_plural='Notification Status'

# assign sub to trainer
class AssignSubscriber(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)        

#trainer achivements
class TrainerAchivement(models.Model):
	trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True)
	title=models.CharField(max_length=100,null=True)
	detail=models.TextField(null=True)
	img=models.ImageField(upload_to="trainers_achivements/",null=True)

	def __str__(self):
		return str(self.title)

	def image_tag(self):
		if self.img:
			return mark_safe('<img src="%s" width="80" />' % (self.img.url))
		else:
			return 'no-image'

#trainer salary model 
class TrainerSalary(models.Model):
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
    amt=models.IntegerField()
    amt_date=models.DateField()
    remarks=models.TextField(blank=True)

    class Meta:
            verbose_name_plural='trainer salary'
    def __str__(self):
	    return str(self.trainer.full_name)   

#trainer notifications
class TrainerNotifications(models.Model):
    notif_msg=models.TextField()
    class Meta:
        verbose_name_plural='trainer notifs'
    def __str__(self):
	    return str(self.notif_msg)     
            
    def save(self,*args,**kwargs):
        super(TrainerNotifications, self).save(*args,**kwargs)
        channel_layer=get_channel_layer()
        notif=self.notif_msg
        total=TrainerNotifications.objects.all().count()
        async_to_sync(channel_layer.group_send)(
            'noti_group_name',{
            'type':'send_notification',
            'value':json.dumps({'notif':notif,'total':total})
            }
        )
        

# Markas Read Notification By trainer
class NotifTrainerStatus(models.Model):
	notif=models.ForeignKey(TrainerNotifications, on_delete=models.CASCADE)
	trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
	status=models.BooleanField(default=False)

	class Meta:
		verbose_name_plural='trainer Notification Status'



#task
class TrainerTask(models.Model):
        user_ts=models.ForeignKey(AssignSubscriber, on_delete=models.CASCADE,null=True,related_name='user_ts')
        trainer_ts=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,related_name='trainer_ts')
        task=FroalaField()
        

# Reports
class TrainerSubscriberReport(models.Model):
	report_for_trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,related_name='report_for_trainer')
	report_for_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='report_for_user')
	report_from_trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,related_name='report_from_trainer',blank=True)
	report_from_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='report_from_user',blank=True)
	report_msg=models.TextField()


class AppSetting(models.Model):
	logo_img=models.ImageField(upload_to='app_logos/')

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.logo_img.url))    





    

    

