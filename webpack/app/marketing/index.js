import Vue from "vue";
import VueSanitize from "vue-sanitize";

import "./assets/css/index.css";
import ScheduleLocalSeoCall from "./components/ScheduleLocalSeoCall.vue";
import SendUsMessage from "./components/SendUsMessage.vue";
import ScheduleCallHorizontalLayout from "./components/ScheduleCallHorizontalLayout.vue";
import ScheduleCall from "./components/ScheduleCall.vue";
import HomeNews from "./components/HomeNews.vue";

Vue.use(VueSanitize);

if (document.getElementsByClassName("schedule-a-local-seo-call").length > 0) {
  new Vue({ render: h => h(ScheduleLocalSeoCall) }).$mount(".schedule-a-local-seo-call");
}

if (document.getElementsByClassName("send-us-a-message").length > 0) {
  new Vue({ render: h => h(SendUsMessage) }).$mount(".send-us-a-message");
}

if (document.getElementsByClassName("schedule-a-call-horizontal-layout").length > 0) {
  new Vue({ render: h => h(ScheduleCallHorizontalLayout) }).$mount(".schedule-a-call-horizontal-layout");
}

if (document.getElementsByClassName("schedule-a-call").length > 0) {
  new Vue({ render: h => h(ScheduleCall) }).$mount(".schedule-a-call");
}

if (document.getElementsByClassName("home-news").length > 0) {
  new Vue({ render: h => h(HomeNews) }).$mount(".home-news");
}
