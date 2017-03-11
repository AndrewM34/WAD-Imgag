from django.conf.urls import url
from imgag import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^login/$', views.login, name='login'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^reset_password/$', views.reset_pass, name='reset'),
    # url(r'^change_password/$', views.change_pass, name='change'),
    url(r'^account/$', views.account, name='account'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.categories, name='categories'),
    url(r'^post/(?P<post_hashid>[\w]+)/$', views.post, name='post'),
    url(r'^post/(?P<post_hashid>[\w]+)/vote/(?P<users_vote>-?1)$', views.vote, name='vote'),
    url(r'^add_comment/(?P<post_hashid>[\w]+)/$', views.add_comment, name='add_comment'),
    url(r'^search/$', views.search, name='search'),
    url(r'^test/$', views.test, name='test'),
    url(r'^upload/$', views.upload, name='upload'),
]
