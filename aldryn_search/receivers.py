from django.dispatch import receiver

from cms.models import PageContent

from djangocms_versioning import constants
from djangocms_versioning.signals import post_version_operation

from .signals import add_to_index, remove_from_index


@receiver(post_version_operation, sender=PageContent)
def publish_or_unpublish_cms_page(*args, **kwargs):
    if kwargs['operation'] == constants.OPERATION_PUBLISH:
        add_to_index.send(sender=kwargs["sender"], instance=kwargs["obj"].content, object_action='publish')

    if kwargs['operation'] == constants.OPERATION_UNPUBLISH:
        remove_from_index.send(sender=kwargs["sender"], instance=kwargs["obj"].content, object_action='unpublish')
