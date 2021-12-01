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
      <template
        slot="table-column"
        slot-scope="props"
      >
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
            <label for="companyName">
              Company Name
            </label>
            <input
              id="companyName"
              v-model="table.company_name"
              type="text"
              name="companyName"
            >
          </div>
        </div>
      </div>
    </modal>
    <div class="table-add__button">
      <button @click="addClient">
        Add Client
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
      columns: [
        {
          label: "Company name",
          field: "company_name",
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
        company_name: null,
        team: null,
        user: null,
      },
      openModal: false,
      show: false,
    };
  },
  mounted () {
    this.getClients();
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
      this.getClients();
    },
    editRow(id) {
      $vfm.show("edit_dialog", id);
      let current = this.rows.find(i => i.id==id);
      this.table.company_name = current.company_name;
    },
    save(close, id) {
      this.editClient(id);
      close();
      this.table.company_name = this.table.team = this.table.user = null;
    },
    confirm(close, params) {
      this.deleteClient(params.row.id);
      this.$notify({
        "title": "Deleted",
        "text": "The client is deleted",
        "type": "success"
      });
      close();
    },
    cancel(close) {
      close();
      this.table.company_name = null;
    },
    addClient() {
      $vfm.show("edit_dialog");
    },
    onPerPageChange(params) {
      this.updateParams({perPage: params.currentPerPage});
      this.getClients();
    },
    onSortChange(params) {
      this.updateParams({
        sort: [{
          type: params[0].type,
          field: params[0].field,
        }],
      });
      this.getClients();
    },
    onSearch(params) {
      this.updateParams({searchTerm: params.searchTerm});
      this.getClients();
    },
    async getClients() {
      try {
        const response = await client.get("/api/clients/", {"params": this.serverParams});
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
    async deleteClient(ClientId) {
      try {
        await client.delete(`/api/client/${ClientId}`);
        this.getClients();
      } catch (error) {
        if (error.response) {
          this.validationErrors = error.response.data;
        } else {
          this.response = "Request failed, try again.";
        }
      }
    },
    async editClient(ClientId) {
      if (ClientId && typeof ClientId == "number") {
        try {
          await client.put(`/api/client/${ClientId}`, {
            company_name: this.table.company_name,
          });
          this.getClients();
        } catch (error) {
          if (error.response) {
            this.validationErrors = error.response.data;
          } else {
            this.response = "Request failed, try again.";
          }
        }
      } else {
        try {
          await client.post("/api/clients/", {
            company_name: this.table.company_name,
          });
          this.getClients();
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
.table-popup__item {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: #fff;
  border-radius: 12px;
  padding: 0 40px;
}
.table-popup__fileds {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin: 8px 0;
}
.table-popup__fileds label {
  color: #000;
}
.table-popup__fileds input,
.table-popup__fileds select {
  width: 100%;
  border: 1px solid #cbcbcb;
  border-radius: 4px;
  background: transparent;
  padding: 0 8px;
  outline: none;
}
.table-add__button {
  width: 100%;
  margin-top: 16px;
  display: flex;
  justify-content: flex-end;
}
.table-add__button button {
  border: none;
  outline: none;
  border-radius: 4px;
  padding: 8px 12px;
  background: #045cff;
  color: #fff;
}
</style>
