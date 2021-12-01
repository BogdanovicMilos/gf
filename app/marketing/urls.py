from django.urls import path

from .views import marketing, LeadsView
from .views_api import (
    ScheduleAdStrategyCallApiView,
    SendUsMessageApiView,
    ScheduleCallApiView,
    LeadsApiView,
    LeadApiView,
)


urlpatterns = [
    path("", marketing.index, name="index"),
    path("media-buying/", marketing.media_buying, name="media_buying"),
    path("facebook-ads/", marketing.facebook_ads, name="facebook_ads"),
    path("google-ads/", marketing.google_ads, name="google_ads"),
    path("enterprise-seo/", marketing.enterprise_seo, name="enterprise_seo"),
    path("local-seo/", marketing.local_seo, name="local_seo"),
    path("search-engine-optimization/", marketing.search_engine_optimization, name="seo"),
    path("about-us/", marketing.about_us, name="about_us"),
    path("get-in-touch/", marketing.get_in_touch, name="get_in_touch"),
    path("saas-marketing/", marketing.saas_marketing, name="saas_marketing"),
    path("api/schedule-a-local-seo-call/", ScheduleAdStrategyCallApiView.as_view(), name="schedule_a_local_seo_call"),
    path("api/send-us-a-message/", SendUsMessageApiView.as_view(), name="send_us_a_message"),
    path("api/schedule-a-call/", ScheduleCallApiView.as_view(), name="schedule_a_call"),
    path("dashboard/leads", LeadsView.as_view(), name="dashboard_leads"),
    path("api/leads/", LeadsApiView.as_view(), name="leads"),
    path("api/leads/<int:lead_id>", LeadApiView.as_view(), name="lead"),
]
