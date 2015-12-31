from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^adddmin/', include(admin.site.urls)),
	url(r'^teams/(?P<team_name>.*)/$', 'matches.views.team'),
	url(r'^teams/$', 'matches.views.teams'),
    url(r'^$', 'matches.views.teams'),
	url(r'^tourn/(?P<tourn_name>.*)/$', 'matches.views.tourn'),
    url(r'^matches/$', 'matches.views.matches'),
    url(r'^new_match/$', 'matches.views.new_match'),
    url(r'^rating/$', 'matches.views.rating'),
    url(r'^all_tourn/$', 'matches.views.tourns'),
    url(r'^.+$', 'matches.views._404'),
)
