from django.db import models
from django.core.mail import send_mail
from django.conf import settings

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from blog.models import BlogDetailPage
from projects.models import ProjectDetailPage

class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )
    
class ContactPage(AbstractEmailForm):

    template = "contact/contact.html"

    banner = models.ForeignKey(
        'about.BannerSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    navigation_bar = models.ForeignKey(
        'home.NavigationSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )  
    thank_you_text = RichTextField(blank=True)
    content_panels = AbstractEmailForm.content_panels + [
        SnippetChooserPanel('banner'),
        SnippetChooserPanel('navigation_bar'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
         FieldPanel("subject"),
        ], heading="Email Settings"),       
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        latest_posts = BlogDetailPage.objects.live().public()[:2]
        recent_works = ProjectDetailPage.objects.live().public()[:6]
        context['latest_posts'] = latest_posts
        context['recent_works'] = recent_works
        return context

    def send_mail(self, form):
        recipient_list = [x.strip() for x in self.to_address.split(',')]
        content = []
        for field in form:
            label = ''.join(e for e in field.label if e.isalnum())
            value = field.value()
            if isinstance(value, list):
                value = ', '.join(value)
            content.append('{} : {}'.format(label, value))
        content = '\n'.join(content)
        send_mail(self.subject, content, self.from_address, recipient_list, fail_silently=False) 
