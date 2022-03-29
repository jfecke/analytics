from django.contrib import admin
from regression.models import AccessRecord, WebPage, Topic, User

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(User)
# admin.site.register(UserProfileInfo)