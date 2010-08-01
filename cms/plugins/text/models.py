from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from django.conf import settings
from django.utils.html import strip_tags
from django.utils.text import truncate_words
from cms.plugins.text.utils import plugin_admin_html_to_tags,\
    plugin_tags_to_admin_html, plugin_tags_to_id_list
from cms.models.pluginmodel import PluginModelBase
from cms.plugin_base import PluginMediaDefiningClass
from django.db.models.base import ModelBase

class AbstractText(CMSPlugin):
    """Abstract Text Plugin Class"""
    body = models.TextField(_("body"))
    
    class Meta:
        abstract = True
    
    def _set_body_admin(self, text):
        self.body = plugin_admin_html_to_tags(text)

    def _get_body_admin(self):
        return plugin_tags_to_admin_html(self.body)

    body_for_admin = property(_get_body_admin, _set_body_admin, None,
                              """
                              body attribute, but with transformations
                              applied to allow editing in the
                              admin. Read/write.
                              """)

    search_fields = ('body',)
    
    def __unicode__(self):
        return u"%s" % (truncate_words(strip_tags(self.body), 3)[:30]+"...")
    
    def clean_plugins(self):
        ids = plugin_tags_to_id_list(self.body)
        plugins = CMSPlugin.objects.filter(parent=self)
        for plugin in plugins:
            if not str(plugin.pk) in ids:
                plugin.delete() #delete plugins that are not referenced in the text anymore

    
class Text(AbstractText):
    """
    Actual Text Class
    """
    