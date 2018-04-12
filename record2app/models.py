from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _
# Create your models here.

TYPE_CHOICES = (
    ('searching', _("Searching")),
    ('offering', _("Offering")),
)

MONEY_FLOW = (
    ('支出', _("支出")), ('收入', _("收入"))
)

COST_TYPE = (
        ('')
)

class Bulletin(models.Model):
    bulletin_type = models.CharField(_("Type"), max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"), max_length=300)
    contact_person = models.CharField(_("Contact person"), max_length=255)
    phone = models.CharField(_("Phone"), max_length=200, blank=True)
    email = models.EmailField(_("Email"), blank=True)
    image = models.ImageField(_("Image"), max_length=255, upload_to="image/", blank=True)
    class Meta:
        verbose_name = _("Bulletin")
        verbose_name_plural = _("Bulletins")
        ordering = ("title",)

    def __str__(self):
        return self.title

class Costtype(models.Model):
    typecode = models.CharField(_("類別代碼"), max_length=5)
    typename = models.CharField(_("類別"), max_length=20)

    def __str__(self):
        return self.typename

class Record(models.Model):
    flow_type = models.CharField(_("流向"), max_length=10, choices=MONEY_FLOW, default=MONEY_FLOW[0][0])
    item = models.CharField(_("項目"), max_length=50)
    amount = models.IntegerField(_("金額"))
    purch_date = models.DateField(_("日期"), default=datetime.date.today())
    create_date = models.DateTimeField(_("建立時間"), auto_now_add=True)

    def __str__(self):
        return self.item

class testClass(models.Model):
    typea = models.CharField(_("屬性A"), max_length=10)
    typeb = models.CharField(_("attrB"), max_length=20)

    #def __str__(self):
    #    return self.typea





