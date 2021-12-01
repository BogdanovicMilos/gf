import Vue from "vue";
import UsersTable from "./components/UsersTable.vue";
import TeamsTable from "./components/TeamsTable.vue";
import ClientsTable from "./components/ClientsTable.vue";
import WebsitesTable from "./components/WebsitesTable.vue";
import WebpagesTable from "./components/WebpagesTable.vue";
import LeadsTable from "./components/LeadsTable.vue";
import Notifications from
  "vue-notification";

import "./assets/css/index.css";


Vue.use(Notifications);

if (document.getElementsByClassName("leads-table").length > 0) {
  new Vue({ render: h => h(LeadsTable) }).$mount(".leads-table");
}

if (document.getElementsByClassName("users-table").length > 0) {
  new Vue({ render: h => h(UsersTable) }).$mount(".users-table");
}

if (document.getElementsByClassName("teams-table").length > 0) {
  new Vue({ render: h => h(TeamsTable) }).$mount(".teams-table");
}

if (document.getElementsByClassName("clients-table").length > 0) {
  new Vue({ render: h => h(ClientsTable) }).$mount(".clients-table");
}

if (document.getElementsByClassName("websites-table").length > 0) {
  new Vue({ render: h => h(WebsitesTable) }).$mount(".websites-table");
}

if (document.getElementsByClassName("webpages-table").length > 0) {
  new Vue({ render: h => h(WebpagesTable) }).$mount(".webpages-table");
}
