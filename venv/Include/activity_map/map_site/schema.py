from django.conf import settings
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
import graphene

from . import models


class EventType(DjangoObjectType):
    class Meta:
        model = models.Event
        fields = '__all__'


class EventImgType(DjangoObjectType):
    class Meta:
        model = models.EventImg


class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)


    def resolve_all_events(root, info, **kwargs):
        return (
            models.Event.objects.filter(dt_of_start__month='05')
        )

schema = graphene.Schema(query=Query)