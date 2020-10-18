from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from stream import blocks
from blog.models import BlogDetailPage
from projects.models import ProjectDetailPage

class HomePage(Page):
    template = "home/home_page.html"
    banner = StreamField(
        [
            ("banner", blocks.HomeBannerSlide())
        ],
        null=True,
        blank=True
    )
    navigation_bar = models.ForeignKey(
        'home.NavigationSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )  
    services = StreamField(
        [
            ("services", blocks.HomeServiceSlide())
        ],
        null=True,
        blank=True
    )
    features = models.ForeignKey(
        'home.FeatureSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    project = StreamField(
        [
            ("project", blocks.HomeProjectSlide())
        ],
        null=True,
        blank=True
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel("banner"),
        SnippetChooserPanel('navigation_bar'),
        StreamFieldPanel("services"),
        SnippetChooserPanel('features'),
        StreamFieldPanel("project"),
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        latest_posts = BlogDetailPage.objects.live().public()[:2]
        recent_works = ProjectDetailPage.objects.live().public()[:6]
        context['latest_posts'] = latest_posts
        context['recent_works'] = recent_works
        return context

    class Meta:
        verbose_name = "Home page"
        verbose_name_plural = "Home pages"

    
@register_snippet
class FeatureSnippet(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    counter_background = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    counter = StreamField(
        [
            ("counter", blocks.HomeCounterSlide())
        ],
        null=True,
        blank=True
    )
    feature = StreamField(
        [
            ("feature", blocks.HomeFeatureSlide())
        ],
        null=True,
        blank=True
    )

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('counter_background'),
        StreamFieldPanel('counter'),
        StreamFieldPanel('feature'),
    ]

    def __str__(self):
        return self.title
    
@register_snippet
class NavigationSnippet(models.Model):
    title = models.CharField(max_length=50, default="Navigation")
    logo = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    footer_text = models.TextField()
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    google = models.URLField(null=True, blank=True)

    panels = [
        ImageChooserPanel('logo'),
        FieldPanel('footer_text'),
        FieldPanel('facebook'),
        FieldPanel('linkedin'),
        FieldPanel('instagram'),
        FieldPanel('google'),
    ]
    def __str__(self):
        return self.title