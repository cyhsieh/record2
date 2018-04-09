from django.contrib import admin
from record2app import models
from testapp import models as testappmodels
# Register your models here.
admin.site.register(models.Bulletin)
admin.site.register(models.Record)
admin.site.register(models.testClass)
admin.site.register(models.Costtype)
admin.site.register(testappmodels.testmodel)
