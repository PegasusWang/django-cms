# -*- coding: utf-8 -*-
from cms.exceptions import LanguageError
from cms.utils import get_language_from_request
from cms.utils.i18n import get_language_object
from django.contrib.sites.models import Site


class CMSToolbar(object):
    supported_apps = None

    def __init__(self, request, toolbar, is_current_app, app_path):
        self.request = request
        self.toolbar = toolbar
        self.is_current_app = is_current_app
        self.app_path = app_path
        self.current_site = Site.objects.get_current()
        try:
            self.current_lang = get_language_object(get_language_from_request(self.request), self.current_site.pk)['code']
        except LanguageError:
            self.current_lang = None

    def populate(self):
        pass

    def post_template_populate(self):
        pass

    def request_hook(self):
        pass

    @classmethod
    def check_current_app(cls, key, app_name):
        if cls.supported_apps is None:
            local_apps = ".".join(key.split(".")[:-2]),
        else:
            local_apps = cls.supported_apps
        for local_app in local_apps:
            if app_name and local_app and app_name.startswith(local_app):
                return True
        return False

    def render_addons(self, context):
        return []
