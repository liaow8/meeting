from django.conf.urls import patterns

urlpatterns = patterns(
    'homework.views',
    (r'^$', 'home'),
    (r'^host/$', 'show_host'),
    (r'^operation/$', 'show_operation'),
)
