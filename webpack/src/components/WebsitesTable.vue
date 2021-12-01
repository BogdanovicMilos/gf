<template>
  <div>
    <vue-good-table
      mode="remote"
      :total-rows="totalRecords"
      :pagination-options="{
        enabled: true,
        perPage: 10
      }"
      :rows="rows"
      :columns="columns"
      :search-options="{
        enabled: true
      }"
      @on-page-change="onPageChange"
      @on-per-page-change="onPerPageChange"
      @on-search="onSearch"
      @on-sort-change="onSortChange"
      @on-cell-click="onCellClick"
    >
      <template slot="table-column" slot-scope="props">
        <span v-if="props.column.field == 'delete_icon'">
          <svg width="23" height="23">
            <use xlink:href="/static/dashboard/img/trash.svg#ico-trash" />
          </svg>
        </span>
        <span
          v-if="props.column.field == 'change_icon'"
        >
          <svg class="trash-icon" width="23" height="23">
            <use xlink:href="/static/dashboard/img/pen.svg#ico-pen" />
          </svg>
        </span>
        <span v-else>
          {{ props.column.label }}
        </span>
      </template>
      <template slot="table-row" slot-scope="props">
        <span v-if="props.column.field == 'delete_icon'">
          <svg class="trash-icon" width="23" height="23">
            <use xlink:href="/static/dashboard/img/trash.svg#ico-trash" />
          </svg>
        </span>
        <span
          v-if="props.column.field == 'change_icon'"
          @click="editRow(props.row.id)"
        >
          <svg class="trash-icon" width="23" height="23">
            <use xlink:href="/static/dashboard/img/pen.svg#ico-pen" />
          </svg>
        </span>
        <span v-else>
          {{ props.formattedRow[props.column.field] }}
        </span>
      </template>
    </vue-good-table>
    <modal v-model="show" name="confirm_dialog" @confirm="confirm" @cancel="cancel">
      <template #title>
        Are you sure?
      </template>
    </modal>
    <modal
      v-model="openModal"
      name="edit_dialog"
      @confirm="save"
      @cancel="cancel"
    >
      <div class="table-popup__wrapper">
        <div class="table-popup__item">
          <div class="table-popup__fileds">
            <label for="websiteName">
              Name
            </label>
            <input
              id="websiteName"
              v-model="table.name"
              type="text"
              name="websiteName"
            >
          </div>
          <div class="table-popup__fileds">
            <label for="websiteDomain">
              Domain
            </label>
            <input
              id="websiteDomain"
              v-model="table.domain"
              type="text"
              name="websiteDomain"
            >
          </div>
        </div>
      </div>
    </modal>
    <div class="table-add__button">
      <button @click="addWebsite">
        Add Website
      </button>
    </div>
    <notifications position="top right" classes="notification" />
  </div>
</template>

<script>
import client from "../../services/client";
import { VueGoodTable } from "vue-good-table";
import "vue-good-table/dist/vue-good-table.css";
import Modal from "./Modal.vue";
import { $vfm } from "vue-final-modal";
export default {
  components: {
    VueGoodTable,
    Modal,
  },
  data() {
    return {
      clientId: null,
      columns: [
        {
          label: "Name",
          field: "name",
        },
        {
          label: "Domain",
          field: "domain",
        },
        {
          label: "",
          field: "change_icon",
          width: "50px",
          sortable: false
        },
        {
          label: "",
          field: "delete_icon",
          width: "50px",
          sortable: false
        },
      ],
      rows: [],
      totalRecords: 0,
      searchTerm: "",
      serverParams: {
        page: 1,
      },
      table: {
        name: null,
        domain: null,
      },
      openModal: false,
      show: false,
    };
  },
  beforeMount() {
    const roolElement = document.getElementsByClassName("websites-table")[0];
    this.clientId = roolElement.getAttribute("data-client-id");
  },
  mounted () {
    this.getWebSites();
  },
  methods: {
    onCellClick(params) {
      if (params.column.field == "delete_icon")
      {$vfm.show("confirm_dialog", params);}
    },
    updateParams(newProps) {
      this.serverParams = Object.assign({}, this.serverParams, newProps);
    },
    onPageChange(params) {
      this.updateParams({page: params.currentPage});
      this.getWebSites();
    },
    editRow(id) {
      $vfm.show("edit_dialog", id);
      let current = this.rows.find(i => i.id==id);
      this.table.name = current.name;
      this.table.domain = current.domain;
    },
    save(close, id) {
      this.editWebsite(id);
      close();
      this.table.name = this.table.domain = null;
    },
    confirm(close, params) {
      this.deleteWebSite(params.row.id);
      this.$notify({"title": "Deleted",
        "text": "The website is deleted",
        "type": "success"});
      close();
    },
    cancel(close) {
      close();
      this.table.name = this.table.domain = null;
    },
    addWebsite() {
      $vfm.show("edit_dialog");
    },
    onPerPageChange(params) {
      this.updateParams({perPage: params.currentPerPage});
      this.getWebSites();
    },
    onSortChange(params) {
      this.updateParams({
        sort: [{
          type: params[0].type,
          field: params[0].field,
        }],
      });
      this.getWebSites();
    },
    onSearch(params) {
      this.updateParams({searchTerm: params.searchTerm});
      this.getWebSites();
    },
    async getWebSites() {
      try {
        const response = await client.get(`/api/clients/${this.clientId}/websites/`, {"params": this.serverParams});
        this.rows = response.data;
        this.totalRecords = response.metadata.count;
      } catch (error) {
        if (error.response) {
          this.validationErrors = error.response.data;
        } else {
          this.response = "Request failed, try again.";
        }
      }
    },
    async deleteWebSite(WebSiteId) {
      try {
        await client.delete(`/api/websites/${WebSiteId}/`);
        this.getWebSites();
      } catch (error) {
        if (error.response) {
          this.validationErrors = error.response.data;
        } else {
          this.response = "Request failed, try again.";
        }
      }
    },
    async editWebsite(WebSiteId) {
      if (WebSiteId && typeof WebSiteId == "number") {
        try {
          await client.put(`/api/websites/${WebSiteId}/`, {
            name: this.table.name,
            domain: this.table.domain
          });
          this.getWebSites();
        } catch (error) {
          if (error.response) {
            this.validationErrors = error.response.data;
          } else {
            this.response = "Request failed, try again.";
          }
        }
      } else {
        try {
          await client.post(`/api/clients/${this.clientId}/websites/`, {
            name: this.table.name,
            domain: this.table.domain
          });
          this.getWebSites();
        } catch (error) {
          if (error.response) {
            this.validationErrors = error.response.data;
          } else {
            this.response = "Request failed, try again.";
          }
        }
      }
    },
  },
};
</script>

<style>
.trash-icon {
    cursor: pointer;
}
</style>
