from django.contrib import admin
from .models import User ,AutismRecord,Clinic,FeedBack
# Register your models here.

admin.site.register(User)
admin.site.register(AutismRecord)
admin.site.register(Clinic)
admin.site.register(FeedBack)

