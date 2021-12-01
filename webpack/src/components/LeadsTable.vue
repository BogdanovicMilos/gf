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
          <svg width="23" height="23">
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
            <label for="fullName">
              Full Name
            </label>
            <input
              id="fullName"
              v-model="table.full_name"
              type="text"
              name="fullName"
            >
          </div>
          <div class="table-popup__fileds">
            <label for="phoneNumber">
              Phone Number
            </label>
            <input
              id="phoneNumber"
              v-model="table.phone_number"
              type="text"
              name="phoneNumber"
            >
          </div>
          <div class="table-popup__fileds">
            <label for="emailAddress">
              Email Address
            </label>
            <input
              id="emailAddress"
              v-model="table.email_address"
              type="text"
              name="emailAddress"
            >
          </div>
          <div class="table-popup__fileds">
            <label for="website">
              Website
            </label>
            <input
              id="website"
              v-model="table.website"
              type="text"
              name="website"
            >
          </div>
          <div class="table-popup__fileds">
            <label for="monthlyAdBudget">
              Monthly Ad Budget
            </label>
            <select
              id="monthlyAdBudget"
              v-model="table.monthly_ad_budget"
              name="monthlyAdBudget"
            >
              <option value="less_than_10_thousand">
                Less than $10,000/month
              </option>
              <option value="between_10_and_25_thousand">
                $10,000-$25,000/month
              </option>
              <option value="between_25_and_50_thousand">
                $25,001-$50,000/month
              </option>
              <option value="between_50_and_100_thousand">
                $50,001-$100,000/month
              </option>
              <option value="more_than_100_thousand">
                $100,000+/month
              </option>
            </select>
          </div>
          <div class="table-popup__fileds">
            <label for="message">
              Message
            </label>
            <input
              id="message"
              v-model="table.message"
              type="text"
              name="message"
            >
          </div>
        </div>
      </div>
    </modal>
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
          label: "Full Name",
          field: "full_name",
        },
        {
          label: "Phone Number",
          field: "phone_number",
        },
        {
          label: "Email Address",
          field: "email_address",
        },
        {
          label: "Website",
          field: "website",
        },
        {
          label: "Monthly Ad Budget",
          field: "monthly_ad_budget",
        },
        {
          label: "Message",
          field: "message",
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
        full_name: null,
        phone_number: null,
        email_address: null,
        website: null,
        monthly_ad_budget: null,
        message: null,
      },
      openModal: false,
      show: false,
    };
  },
  mounted () {
    this.getLeads();
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
      this.getLeads();
    },
    editRow(id) {
      $vfm.show("edit_dialog", id);
      let current = this.rows.find(i => i.id==id);
      this.table.full_name = current.full_name;
      this.table.phone_number = current.phone_number;
      this.table.email_address = current.email_address;
      this.table.website = current.website;
      this.table.monthly_ad_budget = current.monthly_ad_budget;
      this.table.message = current.message;
    },
    save(close, id) {
      this.editClient(id);
      close();
      this.table.full_name = this.table.phone_number =
      this.table.email_address = this.table.website =
      this.table.monthly_ad_budget = this.table.message = null;
    },
    confirm(close, params) {
      this.deleteLead(params.row.id);
      this.$notify({
        "title": "Deleted",
        "text": "The lead is deleted",
        "type": "success"
      });
      close();
    },
    cancel(close) {
      close();
    },
    onPerPageChange(params) {
      this.updateParams({perPage: params.currentPerPage});
      this.getLeads();
    },
    onSortChange(params) {
      this.updateParams({
        sort: [{
          type: params[0].type,
          field: params[0].field,
        }],
      });
      this.getLeads();
    },
    onSearch(params) {
      this.updateParams({searchTerm: params.searchTerm});
      this.getLeads();
    },
    async getLeads() {
      try {
        const response = await client.get("/api/leads/", {"params": this.serverParams});
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
    async deleteLead(LeadId) {
      try {
        await client.delete(`/api/leads/${LeadId}`);
        this.getLeads();
      } catch (error) {
        if (error.response) {
          this.validationErrors = error.response.data;
        } else {
          this.response = "Request failed, try again.";
        }
      }
    },
    async editClient(LeadId) {
      if (LeadId && typeof LeadId == "number") {
        try {
          await client.put(`/leads/${LeadId}`, {
            full_name: this.table.full_name,
            phone_number: this.table.phone_number,
            email_address: this.table.email_address,
            website: this.table.website,
            monthly_ad_budget: this.table.monthly_ad_budget,
            message: this.table.message,
          });
          this.getLeads();
        } catch (error) {
          if (error.response) {
            this.validationErrors = error.response.data;
          } else {
            this.response = "Request failed, try again.";
          }
        }
      } else {
        try {
          await client.post("/api/leads/", {
            full_name: this.table.full_name,
            phone_number: this.table.phone_number,
            email_address: this.table.email_address,
            website: this.table.website,
            monthly_ad_budget: this.table.monthly_ad_budget,
            message: this.table.message,
          });
          this.getLeads();
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
