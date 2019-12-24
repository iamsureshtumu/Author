from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel

# Create your models here.

### Quote ###
class QuotePage(Page):

    template="quote/quote_page.html"

    # @todo add streamfields
    # content=streamfields()

    heading=models.CharField(max_length=100,null=True,blank=True)

    quote1=models.CharField(max_length=200,null=True,blank=True)
    quote2=models.CharField(max_length=200,null=True,blank=True)
    quote3=models.CharField(max_length=200,null=True,blank=True)

    content_panels=Page.content_panels + [
        FieldPanel("heading"),
        FieldPanel("quote1"),
        FieldPanel("quote2"),
        FieldPanel("quote3"),
    ]

    class Meta:
    
        verbose_name="Quote Page"
        verbose_name_plural="Quote Pages"

## contact ##

class ContactPage(Page):
    
    template="contact/contact_page.html"

    # @todo add streamfields
    # content=streamfields()

    contact=models.CharField(max_length=100,null=True,blank=True)

    address=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    call=models.CharField(max_length=200,null=True,blank=True)

    content_panels=Page.content_panels + [
        FieldPanel("contact"),
        FieldPanel("address"),
        FieldPanel("email"),
        FieldPanel("call"),
        
    ]

    class Meta:
    
        verbose_name="Contact Page"
        verbose_name_plural="Contact Pages"