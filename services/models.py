from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel, RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from stream import blocks
from blog.models import BlogDetailPage
from projects.models import ProjectDetailPage


class ServicesPage(Page):
    template = "services/services.html"
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
    image_slider = StreamField(
        [
            ("img", blocks.ImageSliderBlock())
        ],
        null=True,
        blank=True
    )
    brochure = StreamField(
        [
            ("brochure", blocks.BrochureBlock())
        ],
        null=True,
        blank=True
    )
    text = RichTextField(default="text")
    quotes = StreamField(
        [
            ("quotes", blocks.QuoteBlock())
        ],
        null=True,
        blank=True
    )
    tabs = models.ForeignKey(
        'services.ProductInfoSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    content_panels = Page.content_panels + [
        SnippetChooserPanel('banner'),
        SnippetChooserPanel('navigation_bar'),
        StreamFieldPanel('image_slider'),
        StreamFieldPanel('brochure'),
        FieldPanel('text'),
        StreamFieldPanel('quotes'),
        SnippetChooserPanel('tabs'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        latest_posts = BlogDetailPage.objects.live().public()[:2]
        recent_works = ProjectDetailPage.objects.live().public()[:6]
        context['latest_posts'] = latest_posts
        context['recent_works'] = recent_works
        return context

    class Meta:
        verbose_name = "Services page"
        verbose_name_plural = "Services pages"

@register_snippet
class ProductInfoSnippet(models.Model):
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    tabs = StreamField(
        [
            ("tabs", blocks.ProjectsProductInfoBlock())
        ],
        null=True,
        blank=True
    )
    panels = [
        FieldPanel('title'),
        StreamFieldPanel('tabs')
    ]

    def __str__(self):
        return self.title