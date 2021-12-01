<template>
  <form class="footer__form" @submit.prevent="submitForm">
    <h3 class="section_title" data-aos="fade-up" data-aos-delay="100">
      Ready to discuss?
    </h3>
    <div class="footer__form-field" data-aos="fade-up" data-aos-delay="100">
      <input v-model="fullName" name="full_name" type="text" placeholder="Enter your Name">
      <svg width="22" height="22">
        <use xlink:href="/static/marketing/img/sprite.svg#ico-user" />
      </svg>
    </div>
    <p v-if="validationErrors.hasOwnProperty('full_name')" class="validation-error">
      * Name: {{ validationErrors.full_name[0] }}
    </p>
    <div class="footer__form-field" data-aos="fade-up" data-aos-delay="100">
      <input v-model="phoneNumber" name="phone_number" type="text" placeholder="Enter your Phone">
      <svg width="23" height="23">
        <use xlink:href="/static/marketing/img/sprite.svg#ico-tel" />
      </svg>
    </div>
    <p v-if="validationErrors.hasOwnProperty('phone_number')" class="validation-error">
      * Phone: {{ validationErrors.phone_number[0] }}
    </p>
    <button type="submit" class="btn btn-white" data-aos="fade-up" data-aos-delay="100">
      Schedule a Call
    </button>
    <p v-if="response" class="response">
      {{ response }}
    </p>
  </form>
</template>

<script>
import client from "../../../services/client";

export default {
  data() {
    return {
      fullName: "",
      phoneNumber: "",
      response: "",
      validationErrors: {},
    };
  },
  methods: {
    async submitForm() {
      try {
        await client.post("/api/schedule-a-call/", {
          full_name: this.fullName,
          phone_number: this.phoneNumber
        });
        this.validationErrors = {};
        this.response = "Submited successfully.";
      } catch (error) {
        if (error.response) {
          this.validationErrors = error.response.data;
        } else {
          this.response = "Submit failed, try again.";
        }
      }
    }
  }
};
</script>

<style scoped>
  .response, .validation-error {
    margin-top: 5px;
    font-size: 12px;
  }
</style>
