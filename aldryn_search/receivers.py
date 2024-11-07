"""
Created on Nov 30, 2015
@author: jakob
"""
from django.dispatch.dispatcher import receiver

from cms.models.pagemodel import Page
from cms.signals import post_publish, post_unpublish

from .signals import add_to_index, remove_from_index


@receiver(post_publish, dispatch_uid='publish_cms_page')
def publish_cms_page(sender, instance, language, **kwargs):
    title = instance.get_title(language)
    add_to_index.send(sender=Page, instance=title, object_action='publish')


@receiver(post_unpublish, dispatch_uid='unpublish_cms_page')
def unpublish_cms_page(sender, instance, language, **kwargs):
    title = instance.get_title(language)
    remove_from_index.send(sender=Page, instance=title, object_action='unpublish')
