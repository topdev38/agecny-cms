from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class HomeBannerSlide(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100, required=True, help_text='Add additional title')
    text = blocks.CharBlock(max_length=100, required=True, help_text='Add additional text')
    video_link = blocks.URLBlock()
    image = ImageChooserBlock(required=True, help_text='Upload slide image')
    class Meta:
        template = "home/home_banner_slide.html"
        icon = "edit"
        label = "Banner"

class HomeServiceSlide(blocks.StructBlock):
    text = blocks.CharBlock(max_length=100, required=True, help_text='Add additional text')
    image = ImageChooserBlock(required=True, help_text='Upload slide image')
    class Meta:
        template = "home/home_service_slide.html"
        icon = "edit"
        label = "Service"

class HomeCounterSlide(blocks.StructBlock):
    number = blocks.IntegerBlock(required=True)
    text = blocks.RichTextBlock(required=True, help_text='Add additional text')
    delay = blocks.IntegerBlock(required=False, default=0)
    speed = blocks.IntegerBlock(required=True)
    thousand = blocks.BooleanBlock(required=False, default=False)
    class Meta:
        template = "home/home_counter_block.html"
        icon = "edit"
        label = "Counter"

class HomeFeatureSlide(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100, required=True, help_text='Add additional title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')
    icon = blocks.CharBlock(max_length=50, required=True)
    class Meta:
        template = "home/home_feature_slide.html"
        icon = "edit"
        label = "Feature"

class HomeProjectSlide(blocks.StructBlock):
    category = blocks.CharBlock(max_length=100, required=True, help_text='Add additional category')
    title = blocks.CharBlock(max_length=100, required=True, help_text='Add additional title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')
    image = ImageChooserBlock(required=True, help_text='Upload slide image')
    class Meta:
        template = "home/home_project_slide.html"
        icon = "edit"
        label = "Project"

class AboutTestimonialBlock(blocks.StructBlock):
    feedback = blocks.TextBlock(required=True, help_text='Add Client Feedback')
    client_name = blocks.CharBlock(max_length=40, required=True, help_text='Add Client Name')
    date = blocks.DateBlock()
    photo = ImageChooserBlock(required=True, help_text='Upload slide image')
    class Meta:
        template = "about/testimonials.html"
        icon = "edit"
        label = "Testimonial"

class AboutClientsBlock(blocks.StructBlock):
    img = ImageChooserBlock(required=True, help_text='Upload slide image')
    class Meta:
        icon = "edit"
        label = "Clients"

class AboutTeamBlock(blocks.StructBlock):
    photo = ImageChooserBlock(required=True, help_text='Upload slide image')
    name = blocks.CharBlock(max_length=30, required=True)
    position = blocks.CharBlock(max_length=30, required=True)
    facebook = blocks.URLBlock()
    linkedin = blocks.URLBlock()
    instagram = blocks.URLBlock()
    
    class Meta:
        template = "about/team.html"
        icon = "cup"
        label = "Team Members"

#Service Page
class BrochureBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=30, required=True)
    brochure_type = blocks.ChoiceBlock(
        max_length=3,
        choices=(
            ('pdf', 'pdf'),
            ('doc', 'doc'),
            ('docx', 'docx'),
            ('ppt', 'ppt'),
            ('pptx', 'pptx'),
            ('wd', 'wd'),
        ),
        default='pdf',
        icon='cup'
    )
    get_link = DocumentChooserBlock(blank=True, null=True, default=None)
    
    class Meta:
        icon = "cup"
        label = "Brochure"

class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock(required=True)
    author_name = blocks.CharBlock(max_length=30, required=True)
    class Meta:
        icon = "cup"
        label = "Quotes"

class ImageSliderBlock(blocks.StructBlock):
    img = ImageChooserBlock(required=True, help_text='Upload images')
    class Meta:
        icon = "cup"
        label = "Image Block"

class ProjectsProductInfoBlock(blocks.StructBlock):
    tab_title = blocks.CharBlock(max_length=30, required=True, help_text='Add your title')
    tab_content = blocks.TextBlock(required=True)
    class Meta:
        icon = "cup"
        label = "Product Information"

class Faq(blocks.StructBlock):
    category = blocks.CharBlock(max_length=100, required=True, help_text='Add your title')
    content = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("question", blocks.CharBlock(required=True, max_length='200', help_text='Add your title')),
                ("answer", blocks.RichTextBlock()),
            ]
        )
    )
    class Meta:
        template = "streams/faq.html"
        icon = "placeholder"
        label = "FAQ"
