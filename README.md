# Trocador

A plugin for BitcartCC for users to pay invoices at checkout using a different cryptocurrency. Trocador is an exchange aggregator that offers excellent rates to users while providing them strong privacy.

## Use Cases and Features

* Allow customers to pay with whichever asset they prefer.
* Settle these purchases in your wallet of choice (Bitcoin, Monero, etc).
* Choose a custom plugin name that is displayed to the user (default is "Altcoins Trocador").
* Choose a default payment currency that is shown to the user (eg: Ethereum), and the user can choose a different one.
* Optionally show Trocador to the customer first in the invoice by default.
* Optionally provide a referral code to earn a portion of the volume.

## Caveats

**We recommend setting the invoice expiry timer to at least 120 minutes.**. Most exchanges complete in about 10 minutes but the slowest may take up to a day, depending on network congestion and/or exchange delays.

We recommend not selecting lightning network as the default wallet to receive payments from Trocador, as this may worsen conversion rates and reduce the number of coins accepted.

<!-- ## How to activate -->

<!-- In the server dashboard, click on "Manage Plugins", then click the "Install" button after Trocador. -->
