from django.conf import settings
from graphene_django import DjangoObjectType
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
            models.Event.objects.all()
        )


schema = graphene.Schema(query=Query)