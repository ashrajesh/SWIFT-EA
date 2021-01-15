# SWIFT-EA
Chainlink external adapter that allows SWIFT financial messages to be accessed by the blockchain or smart contract for transaction verification use cases.

## Install
```
pipenv install
```

## Test
```
pipenv run pytest
```

## Run Serverless (via AWS Lambda or GCP Functions)
### Create zip file

```bash
pipenv lock -r > requirements.txt
pipenv run pip install -r requirements.txt -t ./package
pipenv run python -m zipfile -c cl-ea.zip main.py adapter.py bridge.py ./package/*
```

# Solidity Example Integration:
### Declare UETR ID for desired Transaction
'''
req.add("UETR", "97ed4827-7b6f-4491-a06f-b548d5a7512d")
'''

### GET status via HTTP request from options listed on: https://developer.swift.com/content/tracker-reference#tag/Get-Payment-Transaction-Details
```
req.add("status", "transactions") or "changed/transactions" or "cancellation" or "status"
```

### Declare your OAuth Basic 2.0 from Sandbox
'''
req.add("oauth", "YourSWIFT-APIOauthToken")
'''

# Sample Request Body
'''
{'id': 0, 'data': {'UETR': '97ed4827-7b6f-4491-a06f-b548d5a7512d', 'status': 'transactions', 'oauth_token': 'YourSWIFT-APIOauthToken'}}
'''

# Example JSON Response
'''
{
  "uetr": "97ed4827-7b6f-4491-a06f-b548d5a7512d",
  "transaction_status": "ACCC",
  "initiation_time": "2020-08-30T09:00:00.000Z",
  "completion_time": "2020-08-30T17:00:00.000Z",
  "last_update_time": "2020-08-30T17:00:00.000Z",
  "payment_event": [
    {
      "network_reference": "200830BANABEBBGXXX0001000001",
      "message_name_identification": "103",
      "business_service": "001",
      "tracker_event_type": "CTPT",
      "valid": true,
      "instruction_identification": "abc123",
      "transaction_status": "ACSP",
      "transaction_status_reason": "G000",
      "return": false,
      "settlement_method": "INDA",
      "from": "BANABEBBXXX",
      "to": "BANBUS33XXX",
      "serial_parties": {
        "debtor_agent": "BANABEBBXXX",
        "creditor_agent": "BANDJPJTXXX"
      },
      "sender_acknowledgement_receipt": "2020-08-30T09:30:00.000Z",
      "received_date": "2020-08-30T09:30:01.000Z",
      "instructed_amount": {
        "currency": "USD",
        "amount": "1000.00"
      },
      "interbank_settlement_amount": {
        "currency": "USD",
        "amount": "990.00"
      },
      "interbank_settlement_date": "2020-08-30T00:00:00.000Z",
      "charge_bearer": "CRED",
      "charge_amount": [
        {
          "currency": "USD",
          "amount": "10.00"
        }
      ],
      "last_update_time": "2020-08-30T09:30:01.000Z"
    },
    {
      "network_reference": "200830BANBUS33GXXX0033000007",
      "message_name_identification": "199",
      "business_service": "001",
      "tracker_event_type": "CTSU",
      "valid": true,
      "instruction_identification": "statusabc123",
      "transaction_status": "ACSP",
      "transaction_status_reason": "G000",
      "return": false,
      "forwarded_to_agent": "BANCUS33XXX",
      "settlement_method": "INDA",
      "from": "BANBUS33XXX",
      "to": "TRCKCHZZXXX",
      "originator": "BANBUS33XXX",
      "sender_acknowledgement_receipt": "2020-08-30T10:00:00.000Z",
      "confirmed_amount": {
        "currency": "USD",
        "amount": "970.00"
      },
      "charge_bearer": "CRED",
      "charge_amount": [
        {
          "currency": "USD",
          "amount": "10.00"
        },
        {
          "currency": "USD",
          "amount": "20.00"
        }
      ],
      "last_update_time": "2020-08-30T10:00:00.000Z"
    },
    {
      "network_reference": "200830BANCUS33GXXX0017000003",
      "message_name_identification": "103",
      "business_service": "001",
      "tracker_event_type": "CTPT",
      "valid": true,
      "instruction_identification": "def456",
      "transaction_status": "ACSP",
      "transaction_status_reason": "G000",
      "return": false,
      "settlement_method": "INDA",
      "from": "BANCUS33XXX",
      "to": "BANDJPJTXXX",
      "serial_parties": {
        "debtor_agent": "BANABEBBXXX",
        "creditor_agent": "BANDJPJTXXX"
      },
      "sender_acknowledgement_receipt": "2020-08-30T10:30:00.000Z",
      "received_date": "2020-08-30T10:30:01.000Z",
      "instructed_amount": {
        "currency": "USD",
        "amount": "1000.00"
      },
      "interbank_settlement_amount": {
        "currency": "USD",
        "amount": "940.00"
      },
      "interbank_settlement_date": "2020-08-30T00:00:00.000Z",
      "charge_bearer": "CRED",
      "charge_amount": [
        {
          "currency": "USD",
          "amount": "10.00"
        },
        {
          "currency": "USD",
          "amount": "20.00"
        },
        {
          "currency": "USD",
          "amount": "30.00"
        }
      ],
      "last_update_time": "2020-08-30T10:30:01.000Z"
    },
    {
      "network_reference": "200830BANJPJTGXXX0123000007",
      "message_name_identification": "199",
      "business_service": "001",
      "tracker_event_type": "CTSU",
      "valid": true,
      "instruction_identification": "statusdef456",
      "transaction_status": "ACCC",
      "return": false,
      "funds_available": "2020-08-30T17:00:00.000Z",
      "from": "BANDJPJTXXX",
      "to": "TRCKCHZZXXX",
      "originator": "BANDJPJTXXX",
      "sender_acknowledgement_receipt": "2020-08-30T17:00:00.000Z",
      "confirmed_amount": {
        "currency": "USD",
        "amount": "900.00"
      },
      "charge_bearer": "CRED",
      "charge_amount": [
        {
          "currency": "USD",
          "amount": "10.00"
        },
        {
          "currency": "USD",
          "amount": "20.00"
        },
        {
          "currency": "USD",
          "amount": "30.00"
        },
        {
          "currency": "USD",
          "amount": "40.00"
        }
      ],
      "last_update_time": "2020-08-30T17:00:00.000Z"
    }
  ]
}
'''


# Testing & Development

* replace all test_data with your individual sandbox credentials from https://developer.swift.com/getting-started-g4c-sandbox-api (adjust input parameters to reflect new UETR and OAuth Token).
* replace base_url with 'https://api.swiftnet.sipn.swift.com/swift-apitracker/v4/payments' to exit sandbox mode and use real time data. Ensure to accomodate for SSL Certification when making requests along with other security / identification protocols.



### Original Template Credit: https://github.com/thodges-gh/CL-EA-Python-Template
