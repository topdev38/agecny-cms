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

class AboutPage(Page):
    template = "about/about.html"
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
    about_us = models.ForeignKey(
        'about.AboutUsSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )    
    features = models.ForeignKey(
        'home.FeatureSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    testimonials = models.ForeignKey(
        'about.TestimonialSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    clients = StreamField(
        [
            ("clients", blocks.AboutClientsBlock())
        ],
        null=True,
        blank=True,
    )
    team = models.ForeignKey(
        'about.TeamSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    content_panels = Page.content_panels + [
        SnippetChooserPanel('banner'),
        SnippetChooserPanel('navigation_bar'),
        SnippetChooserPanel('about_us'),
        SnippetChooserPanel('features'),
        SnippetChooserPanel('testimonials'),
        StreamFieldPanel('clients'),
        SnippetChooserPanel('team'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        latest_posts = BlogDetailPage.objects.live().public()[:2]
        recent_works = ProjectDetailPage.objects.live().public()[:6]
        context['latest_posts'] = latest_posts
        context['recent_works'] = recent_works
        return context

    class Meta:
        verbose_name = "About page"
        verbose_name_plural = "About pages"

@register_snippet
class BannerSnippet(models.Model):
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    banner_text = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('banner_image'),
        FieldPanel('banner_text'),
    ]
    
    def __str__(self):
        return self.title

@register_snippet
class AboutUsSnippet(models.Model):
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    bg_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    alphabet_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content_title = RichTextField()
    content_text = RichTextField()
    panels = [
        FieldPanel('title'),
        ImageChooserPanel('bg_image'),
        ImageChooserPanel('alphabet_image'),
        ImageChooserPanel('image'),
        FieldPanel('content_title'),
        FieldPanel('content_text'),
    ]

    def __str__(self):
        return self.title

@register_snippet
class TestimonialSnippet(models.Model):
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    testimonials = StreamField(
        [
            ("testimonials", blocks.AboutTestimonialBlock())
        ],
        null=True,
        blank=True
    )
    panels = [
        FieldPanel('title'),
        StreamFieldPanel('testimonials')
    ]

    def __str__(self):
        return self.title

@register_snippet
class TeamSnippet(models.Model):
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    member = StreamField(
        [
            ("member", blocks.AboutTeamBlock())
        ],
        null=True,
        blank=True
    )
    panels = [
        FieldPanel('title'),
        StreamFieldPanel('member')
    ]

    def __str__(self):
        return self.title