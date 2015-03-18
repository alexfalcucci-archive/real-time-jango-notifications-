import notifications

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url('^inbox/notifications/',
                           include(notifications.urls)),
                       url(r'', include(
                           'user_sessions.urls', 'user_sessions')),

                       url(r'^$', 'realtime_notifications.rn.views.home', name='home'),
                       url(r'^send_notification/$', 'realtime_notifications.rn.views.send_notification',
                           name='send_notification'),
                       url(r'^mark_as_read/$', 'realtime_notifications.rn.views.mark_as_read',
                           name='mark_as_read'),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'admin/login.html'}, name='login'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
                           {'next_page': '/'}, name='logout')
                       )
