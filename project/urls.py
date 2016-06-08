
from django.conf.urls import url, include
from django.contrib import admin
from school.views import *
from team.views import *

urlpatterns = [
    #admin
    url(r'^admin/', admin.site.urls),

    #index
    url(r'^$', Index.as_view(), name = 'home'),
    
    #school
    url(r'^school/$', SchoolListView.as_view(), name = 'school_index'),
    url(r'^school/detail/(?P<slug>[-\w]+)/$', SchoolDetail.as_view(), name='school_detail'),
    url(r'^school/new/', SchoolCreate.as_view(), name = 'school_create'),
    url(r'^school/update/(?P<slug>[-\w]+)/$', SchoolUpdate.as_view(), name='school_update'),
    url(r'^school/delete/(?P<slug>[-\w]+)/$', SchoolDelete.as_view(), name='school_delete' ),
    
    #team
    url(r'^team/$', TeamListView.as_view(), name = 'team_index'),
    url(r'^team/detail/(?P<slug>[-\w]+)/$', TeamDetail.as_view(), name='team_detail'),
    url(r'^team/new/', TeamCreate.as_view(), name = 'team_create'),
    url(r'^team/update/(?P<slug>[-\w]+)/$', TeamUpdate.as_view(), name = 'team_update'),
    url(r'^team/delete/(?P<slug>[-\w]+)/$', TeamDelete.as_view(), name = 'team_delete'),
    
    #kid
    url(r'^kid/$', KidListView.as_view(), name = 'kid_index'),
    url(r'^kid/detail/(?P<slug>[-\w]+)/$', KidDetail.as_view(), name='kid_detail'),
    url(r'kid/new/', KidCreate.as_view(), name = 'kid_create'),
    url(r'^kid/update/(?P<slug>[-\w]+)/$', KidUpdate.as_view(), name='kid_update'),
    url(r'^kid/delete/(?P<slug>[-\w]+)/$', KidDelete.as_view(), name='kid_delete'),
    
    #leader
    url(r'^leader/$', LeaderListView.as_view(), name = 'leader_index'),
    url(r'^leader/detail/(?P<slug>[-\w]+)/$', LeaderDetail.as_view(), name = 'leader_detail'),
    url(r'^leader/new/', LeaderCreate.as_view(), name = 'leader_create'),
    url(r'^leader/update/(?P<slug>[-\w]+)/$', LeaderUpdate.as_view(), name = 'leader_update'),
    url(r'^leader/delete/(?P<slug>[-\w]+)/$', LeaderDelete.as_view(), name = 'leader_delete'),

    #API
    url(r'^api/',
        include('team.api.urls', namespace="api")),
]
