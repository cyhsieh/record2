from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class testmodel(models.Model):
    testdate = models.DateField(_("Date"), max_length=10)
    testmail = models.EmailField(_("Testmail"), max_length=30)
    testtext = models.CharField(_("Testtext"), max_length=20, blank=True)
    
    def __str__(self):
        return self.id



