from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^kids/$',
		views.KidListView.as_view(),
		name='kid_list'),

	url(r'^kids/(?P<pk>\d+)/$',
		views.KidDetailView.as_view(),
		name="kid_detalle"),

	url(r'^kids/create/$',
		views.KidCreateView.as_view(),
		name="kid_create"),
]