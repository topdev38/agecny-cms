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
# from blog.models import BlogDetailPage

class ProjectsPage(Page):
    template = "projects/projects.html"
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
        all_posts = ProjectDetailPage.objects.live().public()
        
        recent_works = ProjectDetailPage.objects.live().public()[:6]
        paginator = Paginator(all_posts, 9) # Show 9 resources per page
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
        context['projects'] = resources
        # context['latest_posts'] = latest_posts
        context['recent_works'] = recent_works
        return context
    content_panels = Page.content_panels + [
        SnippetChooserPanel('banner'),
        SnippetChooserPanel('navigation_bar'),
    ]
    class Meta:
        verbose_name = "Projects page"
        verbose_name_plural = "Projects pages"

class ProjectDetailPage(Page):
    template = "projects/projects_detail.html"
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
    images = StreamField(
        [
            ("images", blocks.ImageSliderBlock())
        ],
        null=True,
        blank=True
    )
    tech_stack = models.CharField(max_length=30, null=True, blank=True)
    project_description = RichTextField()
    project_information = RichTextField()

    content_panels = Page.content_panels + [
        SnippetChooserPanel('banner'),
        SnippetChooserPanel('navigation_bar'),
        StreamFieldPanel('images'),
        FieldPanel('tech_stack'),
        FieldPanel('project_description'),
        FieldPanel('project_information'),
    ]
    class Meta:
        verbose_name = "ProjectDetail page"
        verbose_name_plural = "ProjectDetail pages"
    
    def __str__(self):
        return self.title
  