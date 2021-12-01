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
      :search-options="{
        enabled: true
      }"
      :columns="columns"
      @on-page-change="onPageChange"
      @on-per-page-change="onPerPageChange"
      @on-search="onSearch"
      @on-sort-change="onSortChange"
    >
      <template slot="table-column" slot-scope="props">
        <span v-if="props.column.field == 'delete_icon'">
          <svg width="23" height="23">
            <use xlink:href="/static/dashboard/img/trash.svg#ico-trash" />
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
        <span v-else>
          {{ props.formattedRow[props.column.field] }}
        </span>
      </template>
    </vue-good-table>
  </div>
</template>

<script>
import client from "../../services/client";
import { VueGoodTable } from "vue-good-table";
import "vue-good-table/dist/vue-good-table.css";
export default {
  components: {
    VueGoodTable,
  },
  data() {
    return {
      columns: [
        {
          label: "Email",
          field: "email"
        },
      ],
      rows: [],
      totalRecords: 0,
      searchTerm: "",
      serverParams: {
        page: 1,
      },
      show: false,
    };
  },
  mounted () {
    this.getUsers();
  },
  methods: {
    updateParams(newProps) {
      this.serverParams = Object.assign({}, this.serverParams, newProps);
    },
    onPageChange(params) {
      this.updateParams({page: params.currentPage});
      this.getUsers();
    },
    onPerPageChange(params) {
      this.updateParams({perPage: params.currentPerPage});
      this.getUsers();
    },
    onSortChange(params) {
      this.updateParams({
        sort: [{
          type: params[0].type,
          field: params[0].field,
        }],
      });
      this.getUsers();
    },
    onSearch(params) {
      this.updateParams({searchTerm: params.searchTerm});
      this.getUsers();
    },
    async getUsers() {
      try {
        const response = await client.get("/api/users/", {"params": this.serverParams});
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
  },
};
</script>
