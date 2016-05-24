# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cms.models import CMSPlugin


class RolloverPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Image rollover")
    render_template = 'image_rollover/plugins/image_rollover.html'
    allow_children = True
    child_classes = ['Bootstrap3ImageCMSPlugin']

plugin_pool.register_plugin(RolloverPlugin)
