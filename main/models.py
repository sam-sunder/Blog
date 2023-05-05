from django.db import models
from django.contrib.auth.models import User

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.blocks import RichTextBlock, RawHTMLBlock
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtailcodeblock.blocks import CodeBlock


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class BlogPage(Page):
    date = models.DateField("Post date")
    image = models.ImageField(upload_to="blog/")
    card_intro = models.CharField(max_length=300)
    body = StreamField([
        ("content", RichTextBlock()),
        ("code", CodeBlock(label='Code')),
        ('html', RawHTMLBlock(),)
    ])

    search_fields = Page.search_fields + [
        index.SearchField('date'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('image'),
        FieldPanel('card_intro'),
        FieldPanel('body'),
    ]
