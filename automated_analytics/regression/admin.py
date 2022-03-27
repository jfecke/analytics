from django.contrib import admin
from regression.models import AccessRecord, WebPage, Topic

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)