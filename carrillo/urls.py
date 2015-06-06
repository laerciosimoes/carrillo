from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carrillo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', "encuestas.views.login", name="login"),
    url(r'^chart/', "encuestas.views.chart_view", name="chart"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',name="my_login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="auth_logout"),
)
