from django.contrib import admin
from .models import User ,AutismRecord,Clinic,FeedBack,AutismRecordAdult
# Register your models here.

admin.site.register(User)
admin.site.register(AutismRecord)
admin.site.register(Clinic)
admin.site.register(FeedBack)
admin.site.register(AutismRecordAdult)

