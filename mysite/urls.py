# encoding:utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', views.hello),
    url(r'^$', views.home),
    url(r'^time/$', views.current_time),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^display_meta/$', views.display_meta),
    url(r'^books/', include('books.urls')),
    url(r'^contact/$', views.contact)
]

# the URL /debuginfo will only be available if your DEBUG setting is set to True
# if settings.DEBUG:
#      urlpatterns += [url(r'^debuginfo/$', views.debug), ]

# Named Groups
urlpatterns += [
    url(r'^reviews/2003/12$', views.ng_special_case_2003),
    url(r'^reviews/\d+/\d{1,2}/$', views.ng_month_archive),
    url(r'^reviews/(?P<year>\d+)/(?P<month>[1-9]|1[0-2])/(?P<day>[1-9]|1[0-9]|2[0-9]|3[0-1])/$', views.ng_day_archive),
    url(r'^reviews/$', views.ng_page),
    url(r'^reviews/page(?P<num>\d+)/$', views.ng_page),
]

# urlpatterns += [
#     url(r'^community/',include('django_website.contact.urls'))
# ]

urlpatterns += [
    # 传前缀参数
    url(r'^(?P<username>\w+)/books/', include('books.urls')),
]

# extra_patterns = [
#     url(r'^reports/(?P<id>[0-9]+)/$', credit_views.report),
# ]
# urlpatterns += [
#     url(r'^credit/', include(extra_patterns)),
# ]

# urlpatterns = [
#     url(r'^(?P<page_slug>\w+)-(?P<page_id>\w+)/',
#         include([
#         url(r'^history/$', views.history),
#         url(r'^edit/$', views.edit),
#         url(r'^discuss/$', views.discuss),
#         url(r'^permissions/$', views.permissions),
#         ])),
# ]

