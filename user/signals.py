from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Readers, DeletedReaders


@receiver(post_delete, sender=Readers)
def save_deleted_reader(sender, instance, **kwargs):
    deleted_reader = DeletedReaders(
        username=instance.username,
        first_name=instance.first_name,
        last_name=instance.last_name,
        email=instance.email,
        phone_number=instance.phone_number,
        reputation=instance.reputation
    )
    deleted_reader.save()
