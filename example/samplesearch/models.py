from django.db import models
from cms.models.pluginmodel import CMSPlugin

class Search(CMSPlugin):
    search_label = models.CharField()
    search_category = models.CharField()
