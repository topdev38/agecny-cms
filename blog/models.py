from django.db import models
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    PageChooserPanel, 
    StreamFieldPanel, 
    RichTextField, 
    MultiFieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from stream import blocks
from projects.models import ProjectDetailPage

class BlogPage(Page):
    template = "blog/blog.html"
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
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['latest_posts'] = latest_posts
        context['recent_works'] = recent_works
        return context
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_posts = BlogDetailPage.objects.live().public()
        latest_posts = BlogDetailPage.objects.live().public()[:2]
        recent_works = ProjectDetailPage.objects.live().public()[:6]
        paginator = Paginator(all_posts, 10) # Show 9 resources per page
        page = request.GET.get('page')
        try:
            resources = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            resources = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            resources = paginator.page(paginator.num_pages)

        # make the variable 'resources' available on the template
        context['posts'] = resources
        context['latest_posts'] = latest_posts
        context['recent_works'] = recent_works
        return context
    content_panels = Page.content_panels + [
        SnippetChooserPanel('banner'),
        SnippetChooserPanel('navigation_bar'),
    ]
    class Meta:
        verbose_name = "Blog page"
        verbose_name_plural = "Blog pages"


class BlogDetailPage(Page):
    template = "blog/blog_detail.html"
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
    post_date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    blog_content = RichTextField()

    content_panels = Page.content_panels + [
        SnippetChooserPanel('banner'),
        FieldPanel('post_date'),
        FieldPanel('author'),
        ImageChooserPanel('blog_image'),
        FieldPanel('blog_content'),
    ]

    class Meta:
        verbose_name = "BlogDetail page"
        verbose_name_plural = "BlogDetail pages"
    
    def __str__(self):
        return self.title