from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import post_save
from django.dispatch import receiver


INV_TYPES = (
    ('invited', _('Invited')),
    ('speaker', _('Speaker')),
    ('student', _('Student'))
)


class Event(models.Model):
    name = models.CharField(_('name'), max_length=200, unique=True)
    start = models.DateTimeField(_('start date'))
    end = models.DateTimeField(_('end date'))
    price = models.IntegerField(_('ticket price'), default=25)
    price_student = models.IntegerField(_('student price'), default=25)
    price_speaker = models.IntegerField(_('speaker price'), default=0)
    price_invited = models.IntegerField(_('invited price'), default=0)
    info = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    admin = models.EmailField(_('admin email'), blank=True, null=True)
    max = models.IntegerField(_('max tickets'), default=300)
    tshirt_img = models.ImageField(_('t-shirt img'), upload_to='tshirts',
                                   blank=True, null=True)

    class Meta:
        ordering = ['-start']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('register', kwargs={'id': self.id})

    def get_email(self):
        try:
            return self.email
        except:
            return None

    def sold(self):
        sold = self.tickets.filter(confirmed=True).count()
        return sold

    def get_type(self, t):
        from django.utils.translation import ugettext as _
        if t == 'invited':
            if not self.price_invited:
                return _('Invited (FREE, you need an invitation code)')
            return _('Invited (EUR %s, you need an invitation code)') % self.price_invited
        elif t == 'speaker':
            if not self.price_speaker:
                return _('Speaker (FREE, you need an invitation code)')
            return _('Speaker (EUR %s, you need an invitation code)') % self.price_speaker
        elif t == 'student':
            if not self.price_student:
                return _('Student (FREE, you need an invitation code)')
            return _('Student (EUR %s, you need an invitation code)') % self.price_student
        return _('Regular (EUR %s)') % self.price


class ConfirmEmail(models.Model):
    event = models.OneToOneField(Event, related_name='email')
    subject = models.CharField(_('subject'), max_length=300)
    body = models.TextField(_('body'))

    def __str__(self):
        return "ConfirmEmail - %s" % self.event


class EmailAttachment(models.Model):
    email = models.ForeignKey(ConfirmEmail, related_name='attachs')
    attach = models.FileField(_('attach'), upload_to='attachments')


class InvCode(models.Model):
    event = models.ForeignKey(Event, related_name='codes')
    code = models.CharField(_('code'), max_length=10, blank=True, null=True)
    person = models.CharField(_('for person'), max_length=100, blank=True, null=True)
    used = models.BooleanField(_('used'), default=False)
    type = models.CharField(_('type'), choices=INV_TYPES, default='invited', max_length=15)

    def __str__(self):
        return "%s - %s" % (self.code, self.type)


@receiver(post_save, sender=InvCode)
def gencode(sender, instance, created, raw, using, update_fields, **kwargs):
    if not instance.code:
        chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        instance.code = ''.join(random.choice(chars) for _ in range(10))
        instance.save()
