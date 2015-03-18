from django.conf.urls import patterns, include, url
from django.contrib import admin

import notifications


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^inbox/notifications/',
                           include(notifications.urls)),
                       url(r'', include(
                           'user_sessions.urls', 'user_sessions')),
                       )
