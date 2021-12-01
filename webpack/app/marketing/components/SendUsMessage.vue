<template>
  <form @submit.prevent="submitForm">
    <div class="service_contact__form-field">
      <input v-model="fullName" type="text" placeholder="Enter your Name">
      <img src="/static/marketing/img/content/form/user.svg" alt="">
    </div>
    <p v-if="validationErrors.hasOwnProperty('full_name')" class="validation-error">
      * Name: {{ validationErrors.full_name[0] }}
    </p>
    <div class="service_contact__form-field">
      <input v-model="phoneNumber" type="text" placeholder="Enter your Phone number">
      <img src="/static/marketing/img/content/form/phone.svg" alt="">
    </div>
    <p v-if="validationErrors.hasOwnProperty('phone_number')" class="validation-error">
      * Phone: {{ validationErrors.phone_number[0] }}
    </p>
    <div class="service_contact__form-field">
      <textarea v-model="message" placeholder="Message" />
    </div>
    <p v-if="validationErrors.hasOwnProperty('full_name')" class="validation-error">
      * Message: {{ validationErrors.message[0] }}
    </p>
    <button class="btn btn-main">
      Send
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
      message: "",
      response: "",
      validationErrors: {},
    };
  },
  methods: {
    async submitForm() {
      try {
        await client.post("/api/send-us-a-message/", {
          full_name: this.fullName,
          phone_number: this.phoneNumber,
          message: this.message
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
  .service_contact__form-field {
    margin-bottom: 0;
    margin-top: 2rem;
  }
  .service_contact__form-field:first-of-type {
    margin-top: 0;
  }

  .response, .validation-error {
    margin-top: 5px;
    font-size: 12px;
  }

  button {
    margin-top: 2rem;
  }
</style>
