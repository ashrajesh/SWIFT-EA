# SWIFT-EA
Chainlink external adapter that allows SWIFT financial messages to be accessed by the blockchain or smart contract


# Solidity Example Integration:
Declare UETR ID for desired Transaction
req.add("UETR", "d2ecb184-b622-11e9-a2a3-2a2ae2dbcce4")

GET status via HTTP request from options listed on: https://developer.swift.com/content/tracker-reference#tag/Get-Payment-Transaction-Details
req.add("status", "transactions") or "changed/transactions"

Declare your OAuth Basic 2.0
req.add("oauth", "YourSWIFT-APIOauthToken")

# Example JSON Response