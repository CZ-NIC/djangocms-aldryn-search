from django.dispatch import receiver

from cms.models import Page, PageContent

from djangocms_versioning import constants
from djangocms_versioning.signals import post_version_operation

from .signals import add_to_index, remove_from_index


@receiver(post_version_operation, sender=PageContent)
def publish_or_unpublish_cms_page(sender, instance, language, *args, **kwargs):
    """Publish or unpublish cms page."""
    title = instance.get_title(language)
    if kwargs['operation'] == constants.OPERATION_PUBLISH:
        add_to_index.send(sender=Page, instance=title, object_action='publish')
    if kwargs['operation'] == constants.OPERATION_UNPUBLISH:
        remove_from_index.send(sender=Page, instance=title, object_action='unpublish')
