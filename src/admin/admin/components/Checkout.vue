<template>
  <v-tab-item>
    <iframe :src="url" style="width: 100%; min-height: 350px; padding: 10px" />
  </v-tab-item>
</template>

<script>
function getUrl(that) {
  const {
    store,
    invoice,
    tickerTo,
    toCurrencyDue,
    toCurrencyAddress,
    itemDesc,
  } = that
  const { name: storeName } = store
  const { buyer_email: customerEmail } = invoice

  const networkTo = "Mainnet"

  // -- Optional Params --
  let amount = toCurrencyDue
  const fromPreset = "&ticker_from=xmr&network_from=Mainnet"

  let fiatCurrency, donation
  if (!amount || (amount.startsWith("0.00") && amount.endsWith("0"))) {
    amount = null
    donation = true
  }

  // Where the checkout page will open: self | blank | top
  const checkoutTarget = "&target=blank"

  const url =
    "https://trocador.app/anonpay/?" +
    `ticker_to=${tickerTo}` +
    `&network_to=${networkTo}` +
    `&address=${toCurrencyAddress}` +
    (amount ? `&amount=${amount}` : "") +
    (storeName ? `&name=${storeName}` : "") +
    (itemDesc ? `&description=${itemDesc}` : "") +
    fromPreset +
    (customerEmail ? `&email=${customerEmail}` : "") +
    (fiatCurrency ? `&fiat_equiv=${fiatCurrency}` : "") +
    (donation ? "&donation=True" : "") +
    checkoutTarget

  return url
}

export default {
  props: ["store", "invoice", "tickerTo", "toCurrencyAddress", "toCurrencyDue"],
  data() {
    return {
      itemDesc: undefined,
      address: undefined,
      shown: false,
    }
  },
  computed: {
    url() {
      return getUrl(this)
    },
  },
  beforeMount() {
    this.getProductDescription()
  },
  methods: {
    async getProductDescription() {
      // TODO: array of product IDs - only display when length === 1
      return await this.$axios
        .get(`/products/${this.productId}`)
        .then((r) => console.log(r))
    },
  },
}
</script>
