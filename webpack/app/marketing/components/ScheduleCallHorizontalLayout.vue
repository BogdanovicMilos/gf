<template>
  <div
    class="intro__form"
    data-aos="fade-up"
    data-aos-delay="200"
  >
    <form @submit.prevent="submitForm">
      <div class="intro__form-field" data-aos="fade-up" data-aos-delay="100">
        <input v-model="fullName" name="full_name" type="text" placeholder="Enter your Name">
        <svg width="22" height="22">
          <use xlink:href="/static/marketing/img/sprite.svg#ico-user" />
        </svg>
      </div>
      <div class="intro__form-field" data-aos="fade-up" data-aos-delay="100">
        <input v-model="phoneNumber" name="phone_number" type="text" placeholder="Enter your Phone">
        <svg width="23" height="23">
          <use xlink:href="/static/marketing/img/sprite.svg#ico-tel" />
        </svg>
      </div>
      <button type="submit" class="btn btn-main" data-aos="fade-up" data-aos-delay="100">
        Schedule a Call
      </button>
    </form>
    <div class="notifications">
      <p v-if="validationErrors.hasOwnProperty('full_name')" class="validation-error">
        * Name: {{ validationErrors.full_name[0] }}
      </p>
      <p v-if="validationErrors.hasOwnProperty('phone_number')" class="validation-error">
        * Phone: {{ validationErrors.phone_number[0] }}
      </p>
      <p v-if="response" class="response">
        {{ response }}
      </p>
    </div>
  </div>
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
  .intro__form {
    display: block;
  }

  form {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .notifications {
    text-align: left;
  }

  .response, .validation-error {
    margin-top: 5px;
    font-size: 12px;
  }

  @media (max-width: 1024px) {
    .intro__form button,
    .intro__form-field {
      width: calc((100% /3) - 16px);
      margin: 0;
    }
  }

  @media (max-width: 767px) {
    form {
      flex-direction: column;
    }
    .intro__form button,
    .intro__form-field {
      width: 100%;
    }
    .intro__form-field {
      margin-bottom: 16px;
    }
  }
</style>
