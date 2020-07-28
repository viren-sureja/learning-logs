"""Define URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index,name="index"),

    # Show all topics.
    url(r'^topics/$',views.topics, name="topics"),

    # detail page for the single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name="topic"),

    # page for adding new topic
    url(r'^new_topic/$', views.new_topic, name="new_topic"),

    # page for adding new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry,name="new_entry"),
    
    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name="edit_entry"),


]

# in url 1. is regular expression
#        2. is to call function in views
#        3. is referred to the url name 