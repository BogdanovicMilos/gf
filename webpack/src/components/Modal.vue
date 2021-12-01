<template>
  <vue-final-modal
    v-slot="{ params, close }"
    v-bind="$attrs"
    classes="modal-dialog"
    content-class="modal-content"
    v-on="$listeners"
  >
    <span class="modal-header">
      <h5 class="modal-title"> <slot name="title" /></h5>
    </span>
    <div class="modal-body">
      <slot :params="params" />
    </div>
    <div class="modal-footer">
      <button class="btn btn-white" data-dismiss="modal" @click="$emit('cancel', close)">
        Close
      </button>
      <button class="btn btn-primary" data-dismiss="modal" @click="$emit('confirm', close, params)">
        Yes
      </button>
    </div>
  </vue-final-modal>
</template>

<script>
import { VueFinalModal } from "vue-final-modal";

export default {
  name: "Modal",
  components: {
    VueFinalModal,
  },
  inheritAttrs: false,
};
</script>
