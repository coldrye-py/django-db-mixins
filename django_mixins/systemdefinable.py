

from django.db.models import fields

from .base import MixinBase


class SystemDefinableMixin(MixinBase):

    isSystem = fields.BooleanField(default = None)

    @classmethod
    def _classPrepared(cls, model, **kwargs):

        pass

