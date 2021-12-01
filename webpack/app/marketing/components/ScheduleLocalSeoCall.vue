<template>
  <form
    class="service_contact__form"
    data-aos="fade"
    data-aos-delay="450"
    @submit.prevent="submitForm"
  >
    <div class="service_contact__form-field">
      <input v-model="fullName" type="text" placeholder="Enter your Name">
      <img src="/static/marketing/img/content/form/user.svg" alt="">
    </div>
    <p v-if="validationErrors.hasOwnProperty('full_name')" class="validation-error">
      * Name: {{ validationErrors.full_name[0] }}
    </p>
    <div class="service_contact__form-field">
      <input v-model="emailAddress" type="text" placeholder="Enter your E-mail">
      <img src="/static/marketing/img/content/form/email.svg" alt="">
    </div>
    <p v-if="validationErrors.hasOwnProperty('email_address')" class="validation-error">
      * Email: {{ validationErrors.email_address[0] }}
    </p>
    <div class="service_contact__form-field">
      <input v-model="phoneNumber" type="text" placeholder="Enter your Phone number">
      <img src="/static/marketing/img/content/form/phone.svg" alt="">
    </div>
    <p v-if="validationErrors.hasOwnProperty('phone_number')" class="validation-error">
      * Phone: {{ validationErrors.phone_number[0] }}
    </p>
    <div class="service_contact__form-field">
      <input v-model="website" type="text" placeholder="Enter your website">
      <img src="/static/marketing/img/content/form/internet.svg" alt="">
    </div>
    <p v-if="validationErrors.hasOwnProperty('website')" class="validation-error">
      * Website: {{ validationErrors.website[0] }}
    </p>
    <div class="service_contact__form-field">
      <div class="service_contact__form-label">
        Monthly ad budget
      </div>
      <div class="service_contact__form-select">
        <select v-model="monthlyAdBudget" name="monthly_ad_budget">
          <option value="less_than_10_thousand">
            less than $10,000/month
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
    </div>
    <p v-if="validationErrors.hasOwnProperty('monthly_ad_budget')" class="validation-error">
      * Budget: {{ validationErrors.monthly_ad_budget[0] }}
    </p>
    <button class="btn btn-main">
      Schedule Ad Strategy Call
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
      emailAddress: "",
      phoneNumber: "",
      website: "",
      monthlyAdBudget: "less_than_10_thousand",
      response: "",
      validationErrors: {},
    };
  },
  methods: {
    async submitForm() {
      try {
        await client.post("/api/schedule-a-local-seo-call/", {
          full_name: this.fullName,
          email_address: this.emailAddress,
          phone_number: this.phoneNumber,
          website: this.website,
          monthly_ad_budget: this.monthlyAdBudget
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
