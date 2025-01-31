# Ghiro - Copyright (C) 2013-2015 Ghiro Developers.
# This file is part of Ghiro.
# See the file 'docs/LICENSE.txt' for license terms.

from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^update/check/", "manage.views.update_check"),
    url(r"^dependencies/$", "manage.views.dependencies_list"),
)