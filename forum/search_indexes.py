from haystack import indexes
import datetime
from django.utils import timezone
#from haystack import site
from .models import Thread

class ThreadIndex (indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    body = indexes.CharField(model_attr='text')

    def get_model(self):
        return Thread

    def get_queryset(self, using=None):
        """Used when the entire index for model is updated."""
       # return BlogEntry.objects.filter(publication_date__lte=datetime.datetime.now(), status=BlogEntry.LIVE_STATUS)
        return Thread.objects.filter(time_posted__lte=datetime.datetime.now())

#site.register(Thread, ThreadIndex)