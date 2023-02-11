import Checkout from "@saltrafael-admin/components/Checkout.vue"
import Tab from "@saltrafael-admin/components/Tab.vue"

// Register custom components (look for UIExtensionSlot references in the code) or data dictionaries here
export default {
  extendComponents: {
    checkout_payment_tab: [Tab],
    checkout_payment_content: [Checkout],
  },
  // dictionaries: {
  //   dictionary_name: data,
  // },
}

