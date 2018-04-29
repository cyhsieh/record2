from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Create your models here.

TYPE_CHOICES = (
    ('searching', _("Searching")),
    ('offering', _("Offering")),
)

MONEY_FLOW = (
    ('in', _("收入")), ('out', _("支出"))
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
    # purch_date = models.DateField(_("日期"), default=timezone.now().date)
    create_date = models.DateTimeField(_("建立時間"), auto_now_add=True)

    def __str__(self):
        return self.item

class testClass(models.Model):
    typea = models.CharField(_("屬性A"), max_length=10)
    typeb = models.CharField(_("attrB"), max_length=20)

    #def __str__(self):
    #    return self.typea
TOBUY_TYPE_CHOICE = (
        ('want','想要'),('need','需要')
        )
class TobuyItem(models.Model):
    itemname = models.CharField(max_length=20, verbose_name="名稱")
    budget = models.IntegerField(verbose_name="預算")
    tobuy_type = models.CharField(max_length=10,choices=TOBUY_TYPE_CHOICE, verbose_name="需要/想要", default=TOBUY_TYPE_CHOICE[0][0])
    tobuy_date = models.DateField(verbose_name="預定購買日期", null=True, blank=True)
    addtime = models.DateTimeField(verbose_name="加入時間", auto_now_add=True)

    def __str__(self):
        return self.itemname
