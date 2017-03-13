from django.conf.urls import url
from imgag import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/(page/(?P<page>[0-9]+)/(?P<ajax>(ajax)?))?$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^account/$', views.account, name='account'),
    url(r'^categories/$', views.show_categories, name='categories'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/((?P<page>[0-9]+)/(?P<ajax>ajax))?$',
        views.show_category, name='category'),
    url(r'^post/(?P<post_hashid>[\w]+)/$', views.show_post, name='post'),
    url(r'^post/(?P<post_hashid>[\w]+)/vote/(?P<users_vote>-?1)/(?P<ajax>ajax)?$', views.vote, name='vote'),
    url(r'^add_comment/(?P<post_hashid>[\w]+)/(comments-count/(?P<comments_count>[0-9]+)/(?P<ajax>ajax))?$',
        views.add_comment, name='add_comment'),
    url(r'^search/(?P<query>[^/]+)/$', views.searchArg, name='searchArg'),
	url(r'^search/$', views.search, name='search'),
    url(r'^test/$', views.test, name='test'),
    url(r'^upload/$', views.upload, name='upload'),
]
