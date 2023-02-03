from django.conf.urls import url
from . import views
app_name = 'restappReview'

urlpatterns = [

    url(r'^products/(?P<pk>[0-9]+)$',views.Productlist.as_view()),
    url(r'^products/(?P<product_id>[0-9]+)/reviews/?P<review_id>[0-9]+/$',views.ReviewDetail.as_view()),
]
