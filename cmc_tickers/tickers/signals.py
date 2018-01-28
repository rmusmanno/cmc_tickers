from django.dispatch import Signal
from django.db import models

post_update = Signal()


class UpateCustomQuerySet(models.query.QuerySet):

    def update(self, kwargs):
        super(UpateCustomQuerySet, self).update(kwargs)
        post_update.send(sender=self.model)


class UpdateCustomManager(models.Manager):

    def getqueryset(self):
        return UpateCustomQuerySet(self.model, using=self._db)
