---
title: Bitso API Reference

language_tabs:
  - shell: Shell
  - javascript: NodeJS
  - python: Python
  - ruby: Ruby
  - java: Java
  - php: PHP

toc_footers:
  - <a href='https://bitso.com/api_setup'>Sign Up for a Bitso Developer Key</a>
  - <a href='http://github.com/tripit/slate'>Documentation Powered by Slate</a>

search: true
---

# Introduction

The Bitso API allows you to integrate the Bitso trading platform
with third party applications, such as trading applications, charting programs,
point of sale systems, and much more. Below you will find details on how the
system functions, along with examples in common programming languages.

# General

General Information about Bitso's APIs

## HTTP and WebSocket APIs

Bitso offers a HTTP API, and a WebSocket API. The HTTP API exposes
both public and private functions. The WebSocket API offers realtime
streaming of market-data, such as the Bitso order book state.

## Transfer API

Bitso’s powerful Transfer API allows for simple integration for routing Bitcoin payments directly through to a choice of Mexican Peso end-points. Please contact us if you're interested in using this API, access is available on request.

## HTTP API Responses

Our REST-like APIs will always return a JSON Object.

For successful API calls, our JSON response objects looks like:

`
{   "success": true,
    "payload": {RELEVANT_DATA_HERE}
}
`
	
For unsuccessful API calls, our JSON response objects look like:

`
{
    "success": false,
    "error": {"message": ERROR_MESSAGE, "code": ERROR_CODE}
}
`


## Notations

**Major** denotes the cryptocurrency, in our case Bitcoin (BTC) or Ether (ETH).

**Minor** denotes fiat currencies, in our case Mexican Peso (MXN)

An order book is always referred to in the API as "Major_Minor". For example: "**btc_mxn**"

## Precision

We return decimal numbers as strings to preserve full precision across platforms. We recommend you also convert your numbers to string in order to avoid undesired consequences from precision and truncation errors.


## Rate Limits

Rate limits are are based on one minute windows. If you do more than 30 requests in a minute, you get locked out for one minute.

## Error Codes

Error codes consist of four digits, first two digits correspond to
error categories, the last two digits define specific errors.

### Unknown Errors: 01 (HTTP 500)
* 01001: "Unknown Error"

### Authentication Errors: 02 (HTTP 401)
* 0201: Invalid Nonce or Invalid Credentials

### Validation Errors: 03 (HTTP 400)
* 0301: Unknown Order book
* 0302: Incorrect time frame (not 'hour' or 'minute')
* 0303: Required field missing
* 0304: Required field not valid (email, phone_number)
* 0305: Invalid SMS code (would also apply to correct code but not-correct client id)
* 0306: Order side not in (buy, sell)
* 0307: Order type not in (limit, market)
* 0308: Order request included both minor and major
* 0309: Order request does not include neither minor or major
* 0310: Incorrect WID (non-existent or does not belong to user)
* 0311: Incorrect FID (non-existent or does not belong to user)
* 0312: Incorrect OID (non-existent or does not belong to user)
* 0313: Selected currency not in (mxn, btc, eth)
* 0314: Auto-trade not available for selected currencies
* 0314: Invalid Bitcoin address
* 0315: Invalid Ripple address
* 0316: Invalid Ripple currency
* 0317: Invalid SPEI number
* 0318: Invalid SPEI numeric_ref
* 0319: Invalid SPEI notes_ref 
* 0320: Invalid pagination parameters
* 0321: Incorrect TID (non-existent)
### System Limit Errors: 04 (HTTP 400)
* 0401: Incorrect price, below the mininum
* 0402: Incorrect price, above than maximum
* 0403: Incorrect major, below the mininum
* 0404: Incorrect major, above the maximum
* 0405: Incorrect minor, below the mininum
* 0406: Incorrect minor, above the maximum
* 0407: Invalid precision

### User Limit Error: 05 (HTTP 400)
* 0501: Exceeds user limit for withdrawals

### Funds Error: 06 (HTTP 400)
* 0601: Not enough btc funds
* 0602: Not enough mxn funds

### Throttling Errors: 08 (HTTP 420)
* 0801: You have hit the request rate-limit

### Unsupported HTTP method (400 error)
* 0901: Unsupported HTTP method


## Client Libraries

The following client libraries will allow you to integrate quickly with our APIs

* [Java](https://github.com/bitsoex/bitso-java)
* [NodeJS](https://github.com/etiennetatur/bitso-api)
* [.NET](http://www.nuget.org/packages/Bitso)
* [Python](https://github.com/bitsoex/bitso-py)
* [Objective-C](https://github.com/bitsoex/bitso-ios-sdk)

# Public Endpoints


## Available Books

```shell
curl "https://api.bitso.com/v3/available_books/"
```

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": [{
        "book": "btc_mxn",
        "minimum_amount": ".003",
        "maximum_amount": "1000.00",
        "minimum_price": "100.00",
        "maximum_price": "1000000.00",
        "minimum_value": "25.00",
        "maximum_value": "1000000.00"
    }, {
        "book": "mxn_eth",
        "minimum_amount": ".003",
        "maximum_amount": "1000.00",
        "minimum_price": "100.0",
        "maximum_price": "1000000.0",
        "minimum_value": "25.0",
        "maximum_value": "1000000.0"
    }]
}
```

This endpoint returns a list of existing exchange order books and
their respective order placement limits.

### HTTP Request

`GET https://api.bitso.com/v3/available_books/`


### JSON Response

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**book** | String | Order book symbol | Major_Minor
**minimum_amount** | String | Minimum amount of major when placing orders | Major
**maximum_amount** | String | Maximum amount of major when placing orders | Major
**minimum_price** | String | Minimum price when placing orders | Minor
**maximum_price** | String | Maximum price when placing orders | Minor
**minimum_value** | String | Minimum value amount (amount*price) when placing orders | Minor
**maximum_value** | String | Maximum value amount (amount*price) when placing orders | Minor



## Ticker

```shell
curl "https://api.bitso.com/v3/ticker/?book=btc_mxn"
```

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": {
        "book": "btc_mxn",
        "volume": "22.31349615",
        "high": "5750.00",
        "last": "5633.98",
        "low": "5450.00",
        "vwap": "5393.45",
        "ask": "5632.24",
        "bid": "5520.01",
        "created_at": "2016-04-08T17:52:31.000+00:00"
    }
}
```

This endpoint returns trading information from the specified book.

### HTTP Request

`GET https://api.bitso.com/v3/ticker/`

### Query Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**book** |  | YES | Specifies which book to use

### JSON Response

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**book** | String | Order book symbol | Major_Minor
**volume** | String | Last 24 hours volume | Major
**high** | String | Last 24 hours price high | Minor/Major
**last** | String | Last traded price | Minor/Major
**low** | String | Last 24 hours price low | Minor/Major
**vwap** | String | Last 24 hours volume weighted average price: [vwap](http://en.wikipedia.org/wiki/Volume-weighted_average_price) | Minor/Major
**ask** | String | Lowest sell order | Minor/Major
**bid** | String | Highest buy order | Minor/Major
**created_at** | String | Timestamp at which the ticker was generated | ISO 8601 timestamp


## Order Book

```shell
curl "https://api.bitso.com/v3/order_book/?book=btc_mxn"
```

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": {
        "asks": [{
            "book": "btc_mxn",
            "price": "5632.24",
            "amount": "1.34491802",
            "created_at": "2016-04-08T17:52:31.000+00:00",
            "updated_at": null
        },{
            "book": "btc_mxn",
            "price": "5633.44",
            "amount": "0.4259",
            "created_at": "2016-04-08T17:52:31.000+00:00",
            "updated_at": "2016-04-08T18:43:11.000+00:00"
        },{
            "book": "btc_mxn",
            "price": "5642.14",
            "amount": "1.21642",
            "created_at": "2016-04-08T17:52:31.000+00:00",
            "updated_at": null
        }],
        "bids": [{
            "book": "btc_mxn",
            "price": "6123.55",
            "amount": "1.12560000",
            "created_at": "2016-04-08T17:52:31.000+00:00",
            "updated_at": null
        },{
            "book": "btc_mxn",
            "price": "6121.55",
            "amount": "2.23976",
            "created_at": "2016-04-08T19:34:23.000+00:00",
            "updated_at": "2016-04-08T19:54:21.000+00:00"
        }],
        "created_at": "2016-04-08T17:52:31.000+00:00"
    }
}
```

This endpoint returns a list of all open orders in the specified book.

### HTTP Request

`GET https://api.bitso.com/v3/order_book/`

### Query Parameters

Parameter | Default | Required | Description 
--------- | ------- | -------- | -----------
**book** |  | YES | Specifies which book to use


### JSON Response

Returns JSON object with "bids" and "asks". Each is a JSON Array
of open orders and each open order is represented as a JSON object

Field Name | Type | Description
---------- | ---- | -----------
**asks** | JSON Array | List of open asks
**bids** | JSON Array | List of open bids

**asks** and **bids** JSON Dictionary with the following fields:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**book** | String | Order book symbol | Major_Minor
**price** | String | Price per unit of major | Minor
**amount** | String | Major amount in order | Major
**created_at** | String | Timestamp at which the order was created | ISO 8601 timestamp
**updated_at** | String | Timestamp at which the order was updated | ISO 8601 timestamp


## Trades

```shell
curl "https://api.bitso.com/v3/trades/?book=btc_mxn"
```

> The JSON Array returned by the API looks like this:

```json
{
    "success": true,
    "payload": [{
        "book": "btc_mxn",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "amount": "0.02000000",
        "side": "buy",
        "price": "5545.01",
        "tid": 55845
    }, {
        "book": "btc_mxn",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "amount": "0.33723939",
        "side": "sell",
        "price": "5633.98",
        "tid": 55844
    }]
}
```

This endpoint returns a list of recent trades from the specified book.

### HTTP Request

`GET https://api.bitso.com/v3/trades/`

### Query Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**book** |   | Yes | Specifies which book to use
**time** | hour | No | Time frame for transaction export ("minute" - 1 minute, "hour" - 1 hour)
**marker** |  | No | Returns objects that are older or newer (depending on 'sort') than the object with this ID
**sort** | desc | No | Specifies ordering direction of returned objects
**limit** | 25 | No | Specifies number of objects to return. (Max is 100)


### JSON Response

Returns descending JSON Array of transactions. Every element in the array is a JSON object:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**book** | String | Order book symbol | Major_Minor
**created_at** | String | Timestamp at which the trade was executed | ISO 8601 timestamp
**amount** | String | Major amount transacted | Major
**side** | String | Indicates the maker order side (maker order is the order that was open on the order book) |
**price** | String | Price per unit of major | Minor
**tid** | Long | Trade ID |



## Account Required Fields

```shell
curl "https://api.bitso.com/v3/account_required_fields/"
```

> The JSON Array returned by the API looks like this:

```json
{
	"success": true,
	"payload": [
		{"field_name": "email_address", "field_description": ""},
		{"field_name": "mobile_phone_number", "field_description": ""},
		{"field_name": "given_names", "field_description": ""},
		{"field_name": "family_names", "field_description": ""}
	]
}
```

This endpoint returns a list of required fields and their descriptions
for use in the "Account Creation" endpoint.

### HTTP Request

`GET https://api.bitso.com/v3/account_required_fields/`


### JSON Response

Returns descending JSON Array. Every element in the array is a JSON object with the following fields.

Field Name | Type | Description 
---------- | ---- | ----------- 
**field_name** | String |  Field name that will be user for "account_creation" endpoint
**field_description** | String | Describes each field


## Account Creation

```shell
curl --data "email_address=value1&mobile_phone_number=value2&given_names=value3&family_names=value4" "https://api.bitso.com/v3/accounts/"
```

> The JSON Array returned by the API looks like this:

```json
{
	"success": true,
	"payload": {
		"client_id": 1234,
		"account_level": 0
	}
}
```

This endpoint returns a list of required field and their descriptions
for use in the "Account Creation" endpoint.

### HTTP Request

`POST https://api.bitso.com/v3/accounts/`

### Body Parameters
All parameters as returned by the [Account Required
Fields](#account-required-fields) endpoint


### JSON Response

Returns descending JSON Array. Every element in the array is a JSON object with the following fields.

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**client_id** | Long | Designated Bitso User ID | 
**account_level** | String | Account Verification Level |



# Private Endpoints

Private endpoints are used to manage your account and your orders. These requests must be signed (more on this below).

<aside class="notice">
Private endpoints require API Keys. Make sure you read more about obtaining your private keys <a href="#generating-api-keys">here</a>
</aside>

## Generating API Keys

Bitso uses **API Keys** to allow access to the API.
You can register a new Bitso API key at our [developer portal](https://bitso.com/api_setup).

When setting up a new API, you will need to choose an **API Name** to identify your API.
This name will never be shown anywhere apart from on your API Index page within your account.
You have the option of adding a **Withdrawal Bitcoin Address**, which can be used to lock the API Withdrawal function to a specific Bitcoin address of your choosing. This field is optional.

The three key elements you will need to sign requests are:

* Bitso API Key
* Bitso API Secret
* Bitso Client ID

## Creating and Signing Requests
```shell
#!/bin/bash
# requires:
# -httpie: https://github.com/jkbrzt/httpie

  
URL="https://api.bitso.com/v3/balance/"
CLIENT_ID="BITSO_CLIENT_ID"
API_KEY="BITSO_KEY"
API_SECRET="BITSO_SECRET"
DNONCE=$(date +%s)
SIGNATURE=$(echo -n $DNONCE$CLIENT_ID$API_KEY | openssl dgst -sha256 -hmac $API_SECRET)
http GET $URL Authorization:Bitso $API_KEY:$DNONCE:$SIGNATURE
```

```javascript
var secret = "BITSO API SECRET";
var key = "BITSO API KEY";
var client_id = "BITSO_CLIENT_ID";
var nonce = new Date().getTime();

// Create the signature
var Data = nonce + client_id + key;
var crypto = require('crypto');
var signature = crypto.createHmac('sha256', secret).update(Data).digest('hex');

// Build the auth header
var auth_header = "Bitso "+bitso_key+":" +nonce+":"+signature;


var options = {
  host: 'api.bitso.com',
  port: 443,
  path: '/v3/balance/',
  method: GET,
  headers: {
        'Authorization': auth_header
    }
};

// Send request
var http = require('https');
var req = http.request(options, function(res) {
    res.on('data', function (chunk) {
        console.log("body: " + chunk);
    });
});
req.end();
```

```python
#!/usr/bin/python

import time
import hmac
import hashlib
import requests

bitso_key = "BITSO_KEY"
bitso_secret = "BITSO_SECRET"
bitso_client_id = "BITSO_CLIENT_ID"
nonce =  str(int(round(time.time() * 1000)))

# Create signature
message = nonce +bitso_client_id+bitso_key
signature = hmac.new(bitso_secret.encode('utf-8'),message.encode('utf-8'), hashlib.sha256).hexdigest()


# Build the auth header
auth_header = 'Bitso %s:%s:%s' % (bitso_key, nonce, signature)

# Send request
response = requests.get("https://api.bitso.com/v3/balance/", headers={"Authorization": auth_header})

print response.content
```


```ruby
#!/usr/bin/ruby

require 'date'
require 'json'
require 'openssl'
require 'typhoeus'

bitso_key = "BITSO_KEY";
bitso_secret = "BITSO_SECRET";
bitso_client_id = "BITSO_CLIENT_ID";
nonce = DateTime.now.strftime('%Q')

# Create signature
message = nonce +bitso_client_id+bitso_key
signature = OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new('sha256'), bitso_secret, message)

# Build the auth header
auth_header = "'Bitso #{bitso_key}:#{nonce}:#{signature}"

# Send request
response = Typhoeus::Request.new(
  "https://api.bitso.com/v3/balance/",
  method: "get",
  headers: {"Authorization" =>  auth_header}
).run

puts response.body
```

```java
package com.bitso.awesome;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClients;
import org.json.JSONObject;

public class BitsoJavaExample {
    public static void main(String[] args) throws Exception {
        String bitsoKey = "BITSO API KEY";
        String bitsoSecret = "BITSO API SECRET";
        String bitsoClientId = "BITSO CLIENT ID";
        long nonce = System.currentTimeMillis();

        // Create the signature
        String message = nonce + bitsoClientId + bitsoKey;
        String signature = "";
        byte[] secretBytes = bitsoSecret.getBytes();
        SecretKeySpec localMac = new SecretKeySpec(secretBytes, "HmacSHA256");
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(localMac);
        byte[] arrayOfByte = mac.doFinal(message.getBytes());
        BigInteger localBigInteger = new BigInteger(1, arrayOfByte);
        signature = String.format("%0" + (arrayOfByte.length << 1) + "x", new Object[] { localBigInteger });

        String url = "https://api.bitso.com/v3/balance/";
	
        // Build the auth header
	    String authHeader = String.format("Bitso %s:%s:%s", bitsoKey, nonce, signature);
        

        // Send request
        HttpPost postRequest = new HttpPost(url);
        postRequest.addHeader("Authorization", authHeader);
        CloseableHttpResponse response = HttpClients.createDefault().execute(postRequest);
        BufferedReader in = new BufferedReader(new InputStreamReader(response.getEntity().getContent()));

        String inputLine;
        StringBuffer responseBody = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            responseBody.append(inputLine);
        }
        in.close();
        System.out.println(responseBody.toString());
    }
}

```

```php
<?php
  $bitsoKey       = 'BITSO_API_KEY';
  $bitsoSecret    = 'BITSO_API_SECRET';
  $bitsoClientId  = 'BITSO_CLIENT_ID';
  $nonce          = round(microtime(true) * 1000);

  // Create signature
  $message = $nonce . $bitsoClientId . $bitsoKey;
  $signature = hash_hmac('sha256', $message, $bitsoSecret);

  // Build the auth header
  $format = 'Bitso %s:%s:%s';
  $authHeader =  sprintf($format, ($bitsoKey, $nonce, $signature);


  // Send request
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, 'https://api.bitso.com/v3/balance/');
  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'Authorization: ' .  $authHeader)
  );
  $result = curl_exec($ch);

  echo $result;
?>
```

All REST requests should be valid JSON. You must include 3 fields as a
payload in the "Authorization" header for all Private API Endpoints in order to perform authentication:

* **key** – The API Key you generated
* **nonce** – An integer that must be unique and increasing for each API call (we recommend using a UNIX timestamp)
* **signature** – See below

### Signature

The signature is generated by creating a SHA256 HMAC using the **Bitso API Secret** on the concatenation of **nonce** + **Bitso Client ID** + **Bitso API Key** (no '+' signs in the concatenated string) and hex-encode the output. The **nonce** value should be the same as the **nonce** field in the json dictionary.

### Authorization Header

The header should be constructed, using the fields described above, in
the following form:

**Authorization: Bitso \<key>:\<nonce>:\<signature>**


## Account Balance

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": {
        "balances": [{
            "currency": "mxn",
            "total": "100.1234",
            "locked": "25.1234",
            "available": "75.0000"
        }, {
            "currency": "btc",
            "total": "4.12345678",
            "locked": "25.00000000",
            "available": "75.12345678"
        }, {
            "currency": "eth",
            "total": "50.1234",
            "locked": "40.1234",
            "available": "10.0000"
        }]
    }
}
```

This endpoint returns information concerning the user's balances for all supported currencies.

### HTTP Request

`GET https://api.bitso.com/v3/balance/`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)

### JSON Response


Returns a JSON Array. Every element in the array is a JSON object with the following fields.


Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**currency** | String | Currency symbol | 
**total** | String | Total balance | Currency
**locked** | String | Currency balance locked in open orders | Currency
**available** | String | Currency balance available for use | Currency

## Fees

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": {
        "fees": [{
            "book": "mxn_btc",
            "fee_decimal": "0.0001",
            "fee_percent": "0.01"
        }, {
            "book": "mxn_eth",
            "fee_decimal": "0.001",
            "fee_percent": "0.1"
        }, {
            "book": "cop_btc",
            "fee_decimal": "0.01",
            "fee_percent": "1"
        }]
    }
}
```

This endpoint returns information on customer fees for all available
order books

### HTTP Request

`GET https://api.bitso.com/v3/fees/`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)

### JSON Response


Returns a JSON Array. Every element in the array is a JSON object with the following fields.


Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**book** | String | Order book symbol | Major_Minor
**fee_decimal** | String | Customer trading fee as a decimal | 
**fee_percent** | String | Customer trading fee as a percentage | 




## Ledger

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": [{
        "eid": "c4ca4238a0b923820dcc509a6f75849b",
        "operation": "trade",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "balance_updates": [{
            "currency": "btc",
            "amount": "-0.25232073"
        }, {
            "currency": "mxn",
            "amount": "1013.540958479115"
        }],
        "details": {
            "tid": 51756,
            "oid": "19vaqiv72drbphig81d3y1ywri0yg8miihs80ng217drpw7xyl0wmytdhtby2ygk"
        }
    }, {
        "eid": "6512bd43d9caa6e02c990b0a82652dca",
        "operation": "fee",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "balance_updates": [{
            "currency": "mxn",
            "amount": "-10.237787459385"
        }],
        "details": {
            "tid": 51756,
            "oid": "19vaqiv72drbphig81d3y1ywri0yg8miihs80ng217drpw7xyl0wmytdhtby2ygk"
        }
    }, {
        "operation": "trade",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "balance_updates": [{
            "currency": "eth",
            "amount": "4.86859395"
        }, {
            "currency": "mxn",
            "amount": "-626.77"
        }],
        "details": {
            "tid": 51757,
            "oid": "19vaqiv72drbphig81d3y1ywri0yg8miihs80ng217drpw7xyl0wmytdhtby2ygk"
        }
    }, {
        "eid": "698d51a19d8a121ce581499d7b701668",
        "operation": "fee",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "balance_updates": [{
            "currency": "eth",
            "amount": "0.04917771"
        }],
        "details": {
            "tid": 51757,
            "oid": "19vaqiv72drbphig81d3y1ywri0yg8miihs80ng217drpw7xyl0wmytdhtby2ygk"
        }
    }, {
        "eid": "b59c67bf196a4758191e42f76670ceba",
        "operation": "funding",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "balance_updates": [{
            "currency": "btc",
            "amount": "0.48650929"
        }],
        "details": {
            "fid": "fc23c28a23905d8614499816c3ade455",
            "method": "Bitcoin",
            "funding_address": "18MsnATiNiKLqUHDTRKjurwMg7inCrdNEp"
        }
    }, {
        "eid": "b0baee9d279d34fa1dfd71aadb908c3f",
        "operation": "funding",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "balance_updates": [{
            "currency": "mxn",
            "amount": "300.15"
        }],
        "details": {
            "fid": "3ef729ccf0cc56079ca546d58083dc12",
            "method": "SPEI Transfer",
            "sender_name": "MANUEL OROZCO Y BERRA",
            "sender_bank": "BBVA Bancomer",
            "sender_clabe": "012610001967722183",
            "numeric_reference": "80416",
            "concepto": "Para el regalo",
            "clave_rastreo": "BNET01001604080002076841"
        }
 
    }, {
        "eid": "96e79218965eb72c92a549dd5a330112",
        "operation": "withdrawal",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "balance_updates": [{
            "currency": "mxn",
            "amount": "-200.15"
        }],
        "details": {
            "wid": "c5b8d7f0768ee91d3b33bee648318688",
            "method": "SPEI Transfer",
            "beneficiary_name": "DANIEL COSIO VILLEGAS",
            "beneficiary_bank": "BANAMEX",
            "beneficiary_clabe": "5204165009315197",
            "numeric_reference": "99548",
            "concepto": "Por los tacos del viernes",
            "clave_rastreo": "BNET01001604080002076841"
        }
    }]
}
```

Returns a list of all the user's registered operations.

### HTTP Request

`GET https://api.bitso.com/v3/ledger/`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)


### Query Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**marker** |  | No | Returns objects that are older or newer (depending on 'sort') than the object with this ID
**sort** | desc | No | Specifies ordering direction of returned objects
**limit** | 25 | No | Specifies number of objects tu return. (Max is 100)


### JSON Response

Returns a descending JSON Array of transactions. Every element in the array is a JSON object:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**eid** | String | Entry ID | -
**operation** | String | Unique identifier (only for trades) | -
**created_at** | String | Timestamp at which the order was created | ISO 8601 timestamp
**balance_updates** | JSON object | Updates to user balances for this operation (See dictionary specification below) | -
**details** | JSON object | Specific operation  details | -

### JSON Object for balance_updates

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**currency** | String | Currency for this balance update | -
**balance** | String | Amount added or subtracted to user balance | Currency


### Filter Ledger by operation type

You can specify that the ledger endpoint return only objects that are
a specific operation type.

`GET https://api.bitso.com/v3/ledger/trades/`

`GET https://api.bitso.com/v3/ledger/fundings/`

`GET https://api.bitso.com/v3/ledger/withdrawals/`

`GET https://api.bitso.com/v3/ledger/fees/`

## Withdrawals

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": [{
        "wid": "c5b8d7f0768ee91d3b33bee648318688",
        "status": "pending",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "currency": "btc",
        "method": "Bitcoin",
        "amount": "0.48650929",
        "details": {
            "withdrawal_address": "18MsnATiNiKLqUHDTRKjurwMg7inCrdNEp",
            "tx_hash": "d4f28394693e9fb5fffcaf730c11f32d1922e5837f76ca82189d3bfe30ded433"
        }
    }, {
        "wid": "p4u8d7f0768ee91d3b33bee6483132i8",
        "status": "complete",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "currency": "mxn",
        "method": "SPEI Transfer",
        "amount": "2612.70",
        "details": {
            "beneficiary_name": "BERTRAND RUSSELL",
            "beneficiary_bank": "BANAMEX",
            "beneficiary_clabe": "002320700708015728",
            "numeric_reference": "99548",
            "concepto": "Por los 🌮 del viernes",
            "clave_rastreo": "BNET01001604080002076841",
            "cep": {
                "return": {
                    "cda": {
                        "cadenaOriginal": "||1|13062016|13062016|172053|40002|STP|Bitso - BERTRAND RUSSELL|40|646180115400000002|BIT140123U70|BANAMEX|BERTRAND RUSSELL|40|002320700708015728|ND|-|0.00|2612.70|00001000000401205824||",
                        "conceptoPago": "-",
                        "cuentaBeneficiario": "002320700708015728",
                        "cuentaOrdenante": "646180115400000002",
                        "fechaCaptura": "20160613",
                        "fechaOperacion": "20160613",
                        "hora": "17:08:42",
                        "iva": "0.00",
                        "monto": "2612.70",
                        "nombreBeneficiario": "BERTRAND RUSSELL",
                        "nombreInstBeneficiaria": "BANAMEX",
                        "nombreInstOrdenante": "STP",
                        "nombreOrdenante": "Bitso - Russell",
                        "referenciaNumerica": "99548",
                        "rfcCurpBeneficiario": "ND",
                        "rfcCurpOrdenante": "BIT140123U70",
                        "selloDigital": "cd7yUrnmUQ7CG6M+LX7WOZeizOpkTyMlEAunJaP2j5MAaNPZxy+vAJtgiVL73i1LNSrwK10eBb66Rh4\/RxU6AT2S03chQ\/BS1beknH5xPpGQg+wEXeANtnF2lp71lAD6QZ2O0NE4MIDvLhGGjTGklSP+2fS6joTAaV+tLbtrIp8JiR0MOX1rGPC5h+0ZHNvXQkcHJz3s68+iUAvDnQBiSu768b2C4zpHzteGEnJhU8sAdk83spiWogKALAVAuN4xfSXni7GTk9HObTTRdY+zehfWVPdE\/7uQSmMTzOKfPbQU02Jn\/5DdE3gYk6JZ5m70JsUSFBTF\/EVX8hhg0pu2iA==",
                        "serieCertificado": "",
                        "tipoOperacion": "C",
                        "tipoPago": "1"
                    },
                    "estadoConsulta": "1",
                    "url": "http:\/\/www.banxico.org.mx\/cep?i=90646&s=20150825&d=viAKjS0GVYB8qihmG9I%2B9O1VUvrR2td%2Fuo3GyVDn8vBp371tVx5ltRnk4QsWP6KP%2BQvlWjT%2BzfwWWTA3TMk4tg%3D%3D"
                }
            }
        }
    }, {
        "wid": "of40d7f0768ee91d3b33bee64831jg73",
        "status": "complete",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "currency": "mxn",
        "method": "Debit Card",
        "amount": "500.00",
        "details": {
            "beneficiary_name": "ALFRED NORTH WHITEHEAD",
            "beneficiary_bank": "BANAMEX",
            "beneficiary_clabe": "5204165009315197",
            "numeric_reference": "30535",
            "concepto": "-",
            "clave_rastreo": "BNET01001604080002076841",
            "cep": {
                "return": {
                    "cda": {
                        "cadenaOriginal": "||1|07042016|07042016|095656|40002|STP|Bitso - Al|40|646180115400000002|BIT140123U70|BANAMEX|ALFRED NORTH WHITEHEAD|3|5204165009315197|ND|-|0.00|500.00|00001000000401205824||",
                        "conceptoPago": "-",
                        "cuentaBeneficiario": "5204165009315197",
                        "cuentaOrdenante": "646180115400000002",
                        "fechaCaptura": "20160407",
                        "fechaOperacion": "20160407",
                        "hora": "09:56:51",
                        "iva": "0.00",
                        "monto": "500.00",
                        "nombreBeneficiario": "ALFRED NORTH WHITEHEAD",
                        "nombreInstBeneficiaria": "BANAMEX",
                        "nombreInstOrdenante": "STP",
                        "nombreOrdenante": "Bitso - RUSSELL",
                        "referenciaNumerica": "30535",
                        "rfcCurpBeneficiario": "ND",
                        "rfcCurpOrdenante": "BIT140123U70",
                        "selloDigital": "GaXpeaKgkc+gc0w9XgBbRCMmKWLNdSTV5C4CNQ4DL4ZVT+1OBSqNtX\/pv2IGjI7bKjCkaNrKUdaCdFwG6SdZ0nS9KtYSx1Ewg2Irg6x4kSzeHdlzBDr6ygT+bb+weizxcXMARKkciPuSQlyltCrEwSi07yVzachKfcEN8amj2fsEzim7gSyUc3ecKA1n8DX89158fwukKTIg4ECfOLsgueKF8unwbICWHXwRaaxIAA6PVw7O6WwGXxMtMBTCdiT202c8I2SnULFqK9QVJlQ\/YDRXFI4IMMAwGQZWbbmk8gf\/J3Fixy+0lcQV35TBBrbHyFPiaHaRN95yK\/BUxPOhag==",
                        "serieCertificado": "",
                        "tipoOperacion": "C",
                        "tipoPago": "1"
                    },
                    "estadoConsulta": "1",
                    "url": "http:\/\/www.banxico.org.mx\/cep?i=90646&s=20150825&d=3AeATtn9mM9yySMqwClgSTnKIddFN7JVwo38kDBVjOBRtcYVENx1LblV%2BXOHnKEGTfp0g%2BVLM76C3ewQ0c9vpA%3D%3D"
                }
            },
            "folio_origen": "BITSO4405016499736144"
        }
    }]
}
```

Returns detailed info on a user's fund withdrawals.

### HTTP Request


`GET https://api.bitso.com/v3/withdrawals/`

`GET https://api.bitso.com/v3/withdrawals/wid/`

`GET https://api.bitso.com/v3/withdrawals/wid-wid-wid/`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)



### Query Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**marker** |  | No | Returns objects that are older or newer (depending on 'sort') than the object with this ID
**sort** | desc | No | Specifies ordering direction of returned objects
**limit** | 25 | No | Specifies number of objects tu return. (Max is 100)

### JSON Response

Returns a JSON Array of open orders. Every element in the array is a JSON object:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**wid** | String | The unique withdrawal ID | -
**currency** | String | Currency withdrawn | -
**method** | String | Method for this withdrawal (MXN, BTC, ETH). | -
**amount** | String | The withdrawn amount | currency
**status** | String | The status for this withdrawal (pending, complete, cancelled) | currency
**created_at** | String | Timestamp at which the withdrawal as created |ISO 8601 timestamp
**details** | JSON object | Specific withdrawal details | -


## Fundings

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": [{
        "fid": "c5b8d7f0768ee91d3b33bee648318688",
        "status": "pending",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "currency": "btc",
        "method": "Bitcoin",
        "amount": "0.48650929",
        "details": {
            "funding_address": "18MsnATiNiKLqUHDTRKjurwMg7inCrdNEp",
            "tx_hash": "d4f28394693e9fb5fffcaf730c11f32d1922e5837f76ca82189d3bfe30ded433"
        }
    }, {
        "fid": "p4u8d7f0768ee91d3b33bee6483132i8",
        "status": "complete",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "currency": "mxn",
        "method": "SPEI Transfer",
        "amount": "300.15",
        "details": {
            "sender_name": "BERTRAND RUSSELL",
            "sender_bank": "BBVA Bancomer",
            "sender_clabe": "012610001967722183",
            "receive_clabe": "646180115400467548",
            "numeric_reference": "80416",
            "concepto": "Para el 🐖",
            "clave_rastreo": "BNET01001604080002076841",
            "beneficiary_name": "ALFRED NORTH WHITEHEAD"
        }
    }]
}
```

Returns detailed info on a user's fund withdrawals.

### HTTP Request


`GET https://api.bitso.com/v3/fundings/`

`GET https://api.bitso.com/v3/fundings/fid/`

`GET https://api.bitso.com/v3/fundings/fid-fid-fid/`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)


### Query Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**marker** |  | No | Returns objects that are older or newer (depending on 'sort') than the object with this ID
**sort** | desc | No | Specifies ordering direction of returned objects
**limit** | 25 | No | Specifies number of objects tu return. (Max is 100)


### JSON Response

Returns a JSON Array of open orders. Every element in the array is a JSON object:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**fid** | String | The unique funding ID | -
**currency** | String | Currency funded | -
**method** | String | Method for this funding (MXN, BTC, ETH). | -
**amount** | String | The funding amount | currency
**status** | String | The status for this funding (pending, complete, cancelled) | currency
**created_at** | String | Timestamp at which the funding as created |ISO 8601 timestamp
**details** | JSON object | Specific funding details | -

## User Trades

```shell
curl "https://api.bitso.com/v3/user_trades/?book=btc_mxn"
```

> The JSON Array returned by the API looks like this:

```json
{
    "success": true,
    "payload": [{
        "book": "mxn_btc",
        "major": "-0.25232073",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "minor": "1013.540958479115",
        "fees_amount": "-10.237787459385",
        "fees_currency": "mxn",
        "price": "4057.45",
        "tid": 51756,
        "oid": "19vaqiv72drbphig81d3y1ywri0yg8miihs80ng217drpw7xyl0wmytdhtby2ygk",
        "side": "sell"
    }, {
        "book": "mxn_btc",
        "major": "4.86859395",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "minor": "-626.77",
        "fees_amount": "-0.04917771",
        "fees_currency": "btc",
        "price": "127.45",
        "tid": 51757,
        "oid": "19vaqiv72drbphig81d3y1ywri0yg8miihs80ng217drpw7xyl0wmytdhtby2ygk",
        "side": "buy"
    }]
}
```

This endpoint returns a list of recent trades from the specified book.

### HTTP Request

`GET https://api.bitso.com/v3/user_trades/`

`GET https://api.bitso.com/v3/user_trades/tid/`

`GET https://api.bitso.com/v3/user_trades/tid-tid-tid/`

### Query Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**book** |   | Yes | Specifies which book to use
**marker** |  | No | Returns objects that are older or newer (depending on 'sort') than the object with this ID
**sort** | desc | No | Specifies ordering direction of returned objects
**limit** | 25 | No | Specifies number of objects to return. (Max is 100)


### JSON Response

Returns descending JSON Array of transactions. Every element in the array is a JSON object:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**book** | String | Order book symbol | Major_Minor
**major** | String | Major amount transacted | Major
**minor** | String | Minr amount transacted | Minor
**price** | String | Price per unit of major | Minor
**side** | String | Indicates the user's side for this trade (buy, sell) |
**fees_currency** | String | Indicates the currency in which the trade fee was charged | -
**fees_amount** | String | Indicates the amount charged as trade fee |
**tid** | Long | Trade ID |
**oid** | Long | Users' Order ID |
**created_at** | String | Timestamp at which the trade was executed | ISO 8601 timestamp

## Open Orders

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": [{
        "book": "btc_mxn",
        "amount": "0.01000000",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "updated_at": "2016-04-08T17:52:51.000+00:00",
        "price": "5600.00",
        "oid": "543cr2v32a1h684430tvcqx1b0vkr93wd694957cg8umhyrlzkgbaedmf976ia3v",
        "side": "buy",
        "status": "partial-fill",
        "type": "limit"
    }, {
        "book": "btc_mxn",
        "amount": "0.12680000",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "updated_at": "2016-04-08T17:52:41.000+00:00",
        "price": "4000.00",
        "oid": "qlbga6b600n3xta7actori10z19acfb20njbtuhtu5xry7z8jswbaycazlkc0wf1",
        "side": "sell",
        "status": "open",
        "type": "limit"
    }, {
        "book": "btc_mxn",
        "amount": "1.12560000",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "updated_at": "2016-04-08T17:52:41.000+00:00",
        "price": "6123.55",
        "oid": "d71e3xy2lowndkfmde6bwkdsvw62my6058e95cbr08eesu0687i5swyot4rf2yf8",
        "side": "sell",
        "status": "open",
        "type": "limit"
    }]
}
```

Returns a list of the user's open orders.

### HTTP Request

`GET https://api.bitso.com/v2/open_orders?book=btc_mxn`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)


### Query Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**book** | -  | YES | Specifies which book to use


### JSON Response

Returns a JSON Array of open orders. Every element in the array is a JSON object:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**oid** | String | The Order ID | -
**book** | String | Order book symbol | Major_Minor
**amount** | String | The order's major currency amount | Major
**created_at** | String | Timestamp at which the trade was executed |ISO 8601 timestamp
**updated_at** | String | Timestamp at which the trade was updated | ISO 8601 timestamp
**price** | String | The order's price | Minor
**side** | String | The order side (buy, sell) | -
**status** | String | The order's status (open, partial-fill) | 
**type** | String | The order type (will always be 'limit' for open orders) | -


## Lookup Orders

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": [{
        "book": "btc_mxn",
        "amount": "0.01000000",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "updated_at": "2016-04-08T17:52:51.000+00:00",
        "price": "5600.00",
        "oid": "543cr2v32a1h684430tvcqx1b0vkr93wd694957cg8umhyrlzkgbaedmf976ia3v",
        "side": "buy",
        "status": "partial-fill",
        "type": "limit"
    }, {
        "book": "btc_mxn",
        "amount": "0.12680000",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "updated_at": "2016-04-08T17:58:31.000+00:00",
        "price": "4000.00",
        "oid": "qlbga6b600n3xta7actori10z19acfb20njbtuhtu5xry7z8jswbaycazlkc0wf1",
        "side": "sell",
        "status": "open",
        "type": "limit"
 
    }, {
        "book": "btc_mxn",
        "amount": "1.12560000",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "updated_at": "2016-04-08T17:53:31.000+00:00",
        "price": "6123.55",
        "oid": "d71e3xy2lowndkfmde6bwkdsvw62my6058e95cbr08eesu0687i5swyot4rf2yf8",
        "side": "sell",
        "status": "open",
        "type": "limit"
    }]
}
```

Returns a list of details for 1 or more orders

### HTTP Request

`GET https://api.bitso.com/v3/orders/<oid>/`

`GET https://api.bitso.com/v3/orders/<oid>-<oid>-<oid>/`


### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)



### JSON Response

Returns a JSON Array of open orders. Every element in the array is a JSON object:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**oid** | String | The Order ID | -
**book** | String | Order book symbol | Major_Minor
**amount** | String | The order's major currency amount | Major
**created_at** | String | Timestamp at which the order was created |ISO 8601 timestamp
**updated_at** | String | Timestamp at which the order was updated | ISO 8601 timestamp
**price** | String | The order's price | Minor
**side** | String | The order side (buy, sell) | -
**status** | String | The order's status (open, partial-fill, closed) | 
**type** | String | The order type (market, limit) | -


## Cancel Order

> The string returned by the API looks like this:

```json
{
    "success": true,
    "payload":[
        "543cr2v32a1h684430tvcqx1b0vkr93wd694957cg8umhyrlzkgbaedmf976ia3v",
        "qlbga6b600n3xta7actori10z19acfb20njbtuhtu5xry7z8jswbaycazlkc0wf1",
        "d71e3xy2lowndkfmde6bwkdsvw62my6058e95cbr08eesu0687i5swyot4rf2yf8"
		]
}
```

Cancels open order(s)

### HTTP Request

`DELETE https://api.bitso.com/v3/orders/<oid>/`

`DELETE https://api.bitso.com/v3/orders/<oid>-<oid>-<oid>/`

`DELETE https://api.bitso.com/v3/orders/all/`



### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)


### JSON Response

The response is a list of Order IDs (OIDs) for the canceled orders. Orders may not be successfully cancelled if they have been filled, have been already cancelled, or the OIDs are incorrect.

## Place an Order

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": {
        "book": "btc_mxn",
        "amount": "0.01000000",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "updated_at": null,
        "price": "5600.00",
        "oid": "543cr2v32a1h684430tvcqx1b0vkr93wd694957cg8umhyrlzkgbaedmf976ia3v",
        "side": "buy",
        "status": "open",
        "type": "limit"
    }
}
```

Places a buy or sell order (both limit and market orders are available)

### HTTP Request

`POST https://api.bitso.com/v3/orders/`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-

### Body Parameters


Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**book** | - | Yes | Specifies which book to use
**side** | - | Yes | The order side (buy, sell) 
**type** | - | Yes | The order type (market, limit) |
**major** | - | No | The amount of major currency for this order. An order could be specified in terms of major or minor, never both.
**minor** | - | No | The amount of minor currency for this order. An order could be specified in terms of major or minor, never both.
**price** | - | No | Price per unit of major. For use only with limit orders | Minor (MXN)


### JSON Response

Returns a JSON object representing the order:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**oid** | String | The Order ID | -
**book** | String | Order book symbol | Major_Minor
**amount** | String | The order's major currency amount | Major
**created_at** | String | Timestamp at which the order was created |ISO 8601 timestamp
**updated_at** | String | Timestamp at which the order was updated | ISO 8601 timestamp
**price** | String | The order's price | Minor
**side** | String | The order side (buy, sell) | -
**status** | String | The order's status (open, partial-fill, closed) | 
**type** | String | The order type (market, limit) | -


## Funding Destination

> The JSON object returned by the API looks like this:

```json
{
    "success": true,
    "payload": {
        "account_identifier_name": "SPEI CLABE",
        "account_identifier": "646180115400346012"             
    }
}
```

Returns account funding information for specified currencies.

### HTTP Request

`GET https://api.bitso.com/v3/funding_destination/`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)


### Query Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**fund_currency** | - | Yes | Specifies which currency to fund with.
**converted_currency** | - | No | Specifies what currency to auto-trade for. Funds received will be automatically traded for this currency. 


### JSON Response

Returns a JSON object representing the order:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**account_identifier_name** | String | Account identifier name to fund with the specified currency. | -
**account_identifier** | String | Identifier to where the funds can be sent to. | -



## Bitcoin Withdrawal

> The string returned by the API looks like this:

```json
{
    "success": true,
    "payload": {
        "wid": "c5b8d7f0768ee91d3b33bee648318688",
        "status": "pending",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "currency": "btc",
        "method": "Bitcoin",
        "amount": "-0.48650929",
        "details": {
            "withdrawal_address": "3EW92Ajg6sMT4hxK8ngEc7Ehrqkr9RoDt7",
            "tx_hash": null
        }
    }
}
```

Triggers a bitcoin withdrawal from the user's account

### HTTP Request

`POST https://api.bitso.com/v3/bitcoin_withdrawal/`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**amount** | - | Yes | The amount of BTC to withdraw from your account
**address** | - | Yes | The Bitcoin address to send the amount to

### JSON Response

Returns a JSON object representing the order:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**wid** | String | Unique Withdrawal ID | -
**status** | String | Status of the withdrawal request (pending, complete) | -
**created_at** | String | Timestamp at which the withdrawal request was created | ISO 8601 timestamp
**currency** | String | Currency specified for this withdrawal (BTC) | -
**method** | String | Method for this withdrawal (BTC). | -
**amount** | String | Amount to withdraw. | BTC
**details** | String | Method specific details for this withdrawal | -

## Ether Withdrawal

> The string returned by the API looks like this:

```json
{
    "success": true,
    "payload": {
        "wid": "c5b8d7f0768ee91d3b33bee648318698",
        "status": "pending",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "currency": "btc",
        "method": "Ether",
        "amount": "-10.00",
        "details": {
            "withdrawal_address": "0x55f03a62acc946dedcf8a0c47f16ec3892b29e6d",
            "tx_hash": null
        }
    }
}
```

Triggers an Ethereum withdrawal from the user's account

### HTTP Request

`POST https://api.bitso.com/v3/ether_withdrawal/`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**amount** | - | Yes | The amount of ETH to withdraw from your account
**address** | - | Yes | The ETH address to send the amount to

### JSON Response

Returns a JSON object representing the order:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**wid** | String | Unique Withdrawal ID | -
**status** | String | Status of the withdrawal request (pending, complete) | -
**created_at** | String | Timestamp at which the withdrawal request was created | ISO 8601 timestamp
**currency** | String | Currency specified for this withdrawal (ETH) | -
**method** | String | Method for this withdrawal (ETH). | -
**amount** | String | Amount to withdraw. | ETH
**details** | String | Method specific details for this withdrawal | -


## Ripple Withdrawal

> The string returned by the API looks like this:

```json
{
    "success": true,
    "payload": {
        "wid": "c5b8d7f0768ee91d3b33bee648318688",
        "status": "pending",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "currency": "btc",
        "method": "Ripple",
        "amount": "-0.48650929",
        "details": {
            "withdrawal_address": "rG1QQv2nh2gr7RCZ1P8YYcBUKCCN633jCn",
            "tx_id": null
        }
    }
}
 
```

Triggers a Ripple withdrawal from your account

### HTTP Request

`POST https://api.bitso.com/v3/ripple_withdrawal/`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**amount** | - | Yes | The amount of ETH to withdraw from your account
**address** | - | Yes | The ETH address to send the amount to
**currency** | - | Yes | The currency to withdraw

### JSON Response

Returns a JSON object representing the order:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**wid** | String | Unique Withdrawal ID | -
**status** | String | Status of the withdrawal request (pending, complete) | -
**created_at** | String | Timestamp at which the withdrawal request was created | ISO 8601 timestamp
**currency** | String | Currency specified for this withdrawal | -
**method** | String | Method for this withdrawal | -
**amount** | String | Amount to withdraw | -
**details** | String | Method specific details for this withdrawal | -



<aside class="warning">
<b>The Ripple address associated to your account for deposits will be updated accordingly!</br>
Please ensure that any subsequent Ripple funding emanates from this address.</b>
</aside>

## Bank Withdrawal (SPEI)

> The string returned by the API looks like this:

```json
{
    "success": true,
    "payload": {
        "wid": "p4u8d7f0768ee91d3b33bee6483132i8",
        "status": "pending",
        "created_at": "2016-04-08T17:52:31.000+00:00",
        "currency": "mxn",
        "method": "SPEI Transfer",
        "amount": "-300.15",
        "details": {
            "sender_name": "JUAN ESCUTIA",
            "receive_clabe": "012610001967722183",
            "sender_clabe": "646180115400467548",
            "numeric_reference": "80416",
            "concepto": "Tacos del viernes",
            "clave_rastreo": null,
            "beneficiary_name": "FRANCISCO MARQUEZ"
        }
    }
}
```

Triggers a SPEI withdrawal from your account.
These **withdrawals are immediate** during banking hours (M-F 9:00AM - 5:00PM Mexico City Time).


### HTTP Request

`POST https://api.bitso.com/v3/spei_withdrawal/`

### Authorization Header Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**amount** | - | Yes | The amount of ETH to withdraw from your account
**recipient_given_names** | - | Yes | The recipient's first and middle name(s)
**recipient_family_names** | - | Yes | The recipient's last name
**clabe** | - | Yes | The [CLABE](https://en.wikipedia.org/wiki/CLABE) number where the funds will be sent to
**notes_ref** | - | Yes | The alpha-numeric reference number for this SPEI
**numeric_ref** | - | Yes | The numeric reference for this SPEI


### JSON Response

Returns a JSON object representing the order:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**wid** | String | Unique Withdrawal ID | -
**status** | String | Status of the withdrawal request (pending, complete) | -
**created_at** | String | Timestamp at which the withdrawal request was created | ISO 8601 timestamp
**currency** | String | Currency specified for this withdrawal (MXN) | -
**method** | String | Method for this withdrawal (SPEI Transfer) | -
**amount** | String | Amount to withdraw | -
**details** | String | Method specific details for this withdrawal | -


# WebSocket API

## General

The Orders channel maintains an up-to-date list of the top 20 asks and the top 20 bids, new messages are sent across the channel whenever there is a change in either top 20.

The Diff-Orders channel will send across any modifications to the order book. Specifically, any state changes in existing orders (including orders not in the top 20), and any new orders. An order could be removed, in which case it won't have an 'a' field (amount), or am order could have been partially filled (you can look up an order's state via the lookup_order endpoint) which will be reflected in the amount field. In theory, you can get a copy of the full order book via REST once, and keep it up to date by using the diff-orders channel.

An order's timestamp field is immutable. Even if the amount field is mutated, or the order removed, the timestamp field remains as it was when the order was created. Note that a timestamp is not unique. Different orders can have the same timestamp.

### How to connect

> Create a WebSocket instance:

```blab
websocket = new WebSocket('wss://ws.bitso.com');
```

> Subscribe to each channel you wish to connect to:

```blab
websocket.onopen = function() {
    websocket.send(JSON.stringify({ action: 'subscribe', book: 'btc_mxn', type: 'trades' }));
    websocket.send(JSON.stringify({ action: 'subscribe', book: 'btc_mxn', type: 'diff-orders' }));
    websocket.send(JSON.stringify({ action: 'subscribe', book: 'btc_mxn', type: 'orders' }));
};
```

> The server will acknowledge each subscription to a channel with a message. For example, a successful subscription to the 'trades' channel
will be acknowledged in the following manner:

```blab
{action: "subscribe", response: "ok", time: 1455831538045, type: "trades"}
```

> Once you've succesfully subscribed to a channel, listen for messages and handle them appropriately:

```blab
websocket.onmessage = function(message){
                var data = JSON.parse(message.data);

                if (data.type == 'trades' && data.payload) {

                }
                else if (data.type == 'diff-orders' && data.payload) {

                }
                else if (data.type == 'orders' && data.payload) {

                }
            };
```

### Example Implementation

Use this example native javascript implementation for your reference:
[https://bitso.com/ws_demo.html](https://bitso.com/ws_demo.html)

## Trades Channel

> Messages on this channel look like this:

```json
{
  "type": "trades",
  "book": "btc_mxn",
  "payload": [
    {
      "i": 72022,
      "a": 0.0035,
      "r": 7190,
      "v": 25.16
    }
  ]
}
```

### Client subscription message

`{ action: 'subscribe', book: 'btc_mxn', type: 'trades' }`

### Server subscription response message

`{action: "subscribe", response: "ok", time: 1455831538045, type: "trades"}`

### Server JSON message

The payload contains an array with one or more trades of the following form:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**i** | Number | A unique number identifying the transaction | -
**a** | Number | Amount | Major
**r** | String | Rate | Minor
**v** | String | Value | Minor

## Diff-Orders

> Messages on this channel look like this:

```json
{
  "type": "diff-orders",
  "book": "btc_mxn",
  "payload": [
    {
      "d": 1455315979682,
      "r": 7251.1,
      "t": 1,
      "a": 0.29437179,
      "v": 2134.51
    }
  ]
}
```

### Client subscription message

`websocket.send(JSON.stringify({ action: 'subscribe', book: 'btc_mxn', type: 'diff-orders' }));`

### Server subscription response message

`{action: "subscribe", response: "ok", time: 1455831538047, type: "diff-orders"}`

### Server JSON Message

The payload contains an array with one or more orders of the following form:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**d** | Number | Unix timestamp | Milliseconds
**r** | String | Rate | Minor
**t** | Number | 0 indicates buy 1 indicates sell | -
**a** | Number | Amount | Major
**v** | String | Value | Minor

## Orders

> Messages on this channel look like this:

```json
{
  "type": "orders",
  "book": "btc_mxn",
  "payload": {
    "bids": [
      {
        "r": 7185,
        "a": 0.001343,
        "v": 9.64,
        "t": 1,
        "d": 1455315394039
      },
      {
        "r": 7183.01,
        "a": 0.007715,
        "v": 55.41,
        "t": 1,
        "d": 1455314938419
      },
      {
        "r": 7183,
        "a": 1.59667303,
        "v": 11468.9,
        "t": 1,
        "d": 1455314894615
      }
    ],
    "asks": [
      {
        "r": 7251.1,
        "a": 0.29437179,
        "v": 2134.51,
        "t": 0,
        "d": 1455315979682
      },
      {
        "r": 7251.72,
        "a": 1.32057812,
        "v": 9576.46,
        "t": 0,
        "d": 1455303931277
      }
    ]
  }
}
```

### Client Subscription message

`{ websocket.send(JSON.stringify({ action: 'subscribe', book: 'btc_mxn', type: 'orders' }));`

### Server subscription response message

`{action: "subscribe", response: "ok", time: 1455831538048, type: "orders"}`

### Server JSON message

The payload contains a JSON with two keys, one for the bids and the other for asks on the order book. Both bids and asks contain orders of the following form:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**r** | String | Rate | Minor
**a** | Number | Amount | Major
**v** | String | Value | Minor
**t** | Number | 0 indicates buy 1 indicates sell | -
**d** | Number | Unix timestamp | Milliseconds

# Transfer API

<aside class="notice">
Access to this API is available on request, and not enabled by default. Users won't be able to use this API unless Bitso has enabled it on their account.
</aside>

## General

Bitso’s powerful Transfer API allows for simple integration for routing Bitcoin payments directly through to a choice of Mexican Peso end-points.

The workflow breaks down in the following steps:

1. Request quote
2. Create transfer using quote
3. Send bitcoins to address given
4. After 1 confirmation, pesos are delivered

The quote acquired in step #1 is valid for 60 seconds. Once this is used to create a transfer (#2), that transfer is then valid for 60 seconds from creation (within which time the Bitcoin transaction to satisfy it must be ‘seen’ by our servers – this typically happens within 20 seconds).

Once the transfer is satisfied, the Bitcoin transaction must be confirmed before a further action takes place. Typically this takes around a maximum of 10 minutes, but can be a little longer.

The transfer can be monitored throughout the process by making a request to the URL returned with the transfer creation.

### Authentication

The Transfer API is accessible via an API key created for your account. For full details on creating an API key and how to sign your API requests, please refer to:
[the authentication section](#creating-and-signing-requests)

## Requesting a Quote

> The JSON object returned by the API looks like this:

```json
{
   "success":true,
   "payload":{
      "btc_amount":"0.14965623",
      "currency":"MXN",
      "rate":"3340.99",
      "gross":"500.00",
      "outlets":{
         "sp":{
            "id":"sp",
            "name":"SPEI Transfer",
            "required_fields":[
               "recipient_given_names",
               "recipient_family_names",
               "clabe",
               "bank_name"
            ],
            "minimum_transaction":"500.00",
            "maximum_transaction":"2500000.00",
            "daily_limit":"10000.00",
            "fee":"12.00",
            "net":"488.00",
            "available":"1",
            "verification_level_requirement":"0"
         },
         "vo":{
            "id":"vo",
            "name":"Voucher",
            "required_fields":[
               "email_address"
            ],
            "minimum_transaction":"25.00",
            "maximum_transaction":"9999.00",
            "fee":"0.00",
            "daily_limit":"0.00",
            "net":"500.00",
            "available":"1",
            "verification_level_requirement":"0"
         },
         "rp":{
            "id":"rp",
            "name":"Ripple",
            "required_fields":[
               "ripple_address"
            ],
            "minimum_transaction":"0.00",
            "maximum_transaction":"10000000.00",
            "fee":"5.00",
            "daily_limit":"0.00",
            "net":"495.00",
            "available":"1",
            "verification_level_requirement":"0"
         },
         "pm":{
            "id":"pm",
            "name":"Pademobile",
            "required_fields":[
               "phone_number"
            ],
            "minimum_transaction":"1.00",
            "maximum_transaction":"1000000.00",
            "fee":"0.00",
            "daily_limit":"0.00",
            "net":"500.00",
            "available":"1",
            "verification_level_requirement":"0"
         },
         "bw":{
            "id":"bw",
            "name":"Bank Wire",
            "required_fields":[
               "recipient_full_name",
               "account_holder_address",
               "bank_name",
               "bank_address",
               "account_number",
               "swift",
               "other_instructions"
            ],
            "minimum_transaction":"1000.00",
            "maximum_transaction":"2500000.00",
            "daily_limit":"2500000.00",
            "fee":"500.00",
            "net":"0.00",
            "available":"1",
            "verification_level_requirement":"0"
         }
      },
      "timestamp":"1425101044",
      "expires_epoch":"1425101104"
   }
}
```

### HTTP Request

`POST https://api.bitso.com/v2/transfer_quote`

### Body Parameters

Parameter | Required | Description
--------- | -------- | -----------
**btc_amount** | No | Mutually exclusive with amount. Either this, or amount should be present in the request. The total amount in Bitcoins, as provided by the user. NOTE: The amount is in BTC format (900mbtc = .9 BTC).
**amount** | No | Mutually exclusive with btc_amount. Either this, or btc_amount should be present in the request. The total amount in Fiat currency. Use this if you prefer specifying amounts in fiat instead of BTC.
**currency** | Yes | An ISO 4217 fiat currency symbol (ie, “MXN”). If btc_amount is provided instead of amount, this is the currency to which the BTC price will be converted into. Otherwise, if amount is specified instead of btc_amount, this is the currency of the specified amount.
**full** | No | (optional, defaults to False) - Show the required_fields for each payment outlet as an array of {id, name} objects. This accepts either True or False. When not provided or if the value is False, the required_fields for each Payment Outlet are returned as an array of id strings. For more information about required_fields, please refer to the Payment Outlet Documentation.
**key** | Yes | API key (see Authentication)
**signature** | Yes | Signature (see Authentication)
**nonce** | Yes | nonce (see Authentication)

## Creating a Transfer

> The JSON object returned by the API looks like this:

```json
{
   "success":true,
   "payload":{
      "btc_amount":"0.14965623",
      "btc_pending":"0",
      "btc_received":"0",
      "confirmation_code":"9b2a4",
      "created_at":"1425101044",
      "currency":"MXN",
      "currency_amount":"0",
      "currency_fees":"0",
      "currency_settled":"0",
      "expires_epoch":1425101104,
      "fields":{
         "phone_number":"5554181042"
      },
      "id":"9b2a431b98597312e99cbff1ba432cbf",
      "payment_outlet_id":"pm",
      "qr_img_uri":"https:\/\/chart.googleapis.com\/chart?chl=bitcoin%3AmgKZfNdFJgztvfvhEaGgMTQRQ2iHCadHGa%3Famount%3D0.14965623&chs=400x400&cht=qr&choe=UTF-8&chld=L%7C0",
      "user_uri":"https:\/\/api.bitso.com\/v2\/transfer\/9b2a431b98597312e99cbff1ba432cbf",
      "wallet_address":"mgKZfNdFJgztvfvhEaGgMTQRQ2iHCadHGa"
   } 
}
```

### HTTP Request

`POST https://api.bitso.com/v2/transfer_create`

### Body Parameters

Parameter | Required | Description
--------- | -------- | -----------
**btc_amount** | No | Mutually exclusive with amount. Either this, or amount should be present in the request. The total amount in Bitcoins, as provided by the user. NOTE: The amount is in BTC format (900mbtc = .9 BTC).
**amount** | No | Mutually exclusive with btc_amount. Either this, or btc_amount should be present in the request. The total amount in Fiat currency. Use this if you prefer specifying amounts in fiat instead of BTC.
**currency** | Yes | An ISO 4217 fiat currency symbol (ie, “MXN”). If btc_amount is provided instead of amount, this is the currency to which the BTC price will be converted into. Otherwise, if amount is specified instead of btc_amount, this is the currency of the specified amount.
**rate** | Yes | This is the rate (e.g. BTC/MXN), as acquired from the transfer_quote method. You must request a quote in this way before creating a transfer.
**payment_outlet** | Yes | The outlet_id as provided by quote method. See below for more information on available outlets.
**required_field1** | Yes | Each of the other ‘required fields’, as stipulated in the quote method for the chosen payment_outlet.
**required_field2** | Yes |
**key** | Yes | API key (see Authentication)
**signature** | Yes | Signature (see Authentication)
**nonce** | Yes | nonce (see Authentication)

## Reviewing a Transfer

Make requests to the transfer review end point at any time to monitor the status of your transfer.

### HTTP Request

`GET https://api.bitso.com/v2/transfer/<transfer_id>`

### Response

Parameter | Required | Description
--------- | -------- | -----------
**status** | Yes | **pending**: waiting for the bitcoin transaction to be seen, **confirming**: transaction has been seen, and now waiting for a network confirmation, **completed**: transaction has completed, and funds dispatched via the outlet specified.

## Currently Available Outlets

### SPEI

SPEI is Mexico’s lightning fast and inexpensive inter-bank transfer system (akin to SEPA in Europe, and vastly superior to ACH).

All bank accounts in Mexico can be identified by their special 18-digit SPEI account number, otherwise known as a ‘CLABE’.

Transfers executed via SPEI are typically concluded within a few seconds (within banking hours).

### Pademobile

Pademobile is a popular mobile wallet and payments system in Latin America and beyond. Users running the Pademobile wallet on their cellphone can carry a balance in local currency, and spend it at a variety of locations, including cash-out at stores such as 7-Eleven (this is limited to 300 MXN per day, per location).

Pademobile accounts are identified simply by the user’s phone number. Recipients who do not have smart phones, or who have not installed the wallet app, will receive a text message containing instructions on how to access the received funds.

For more information, please see:  https://www.pademobile.com/en/mx/

### Ripple

As a Ripple Gateway, Bitso is able to issue currencies such as the Mexican Peso directly into the Ripple Network. For more information on Ripple, please see: https://ripple.com/

### Voucher

Bitso offers the ability to issue voucher codes redeemable on Bitso.com, and delivered by email. Simply specify the amount and email address, and the recipient can at any time register on Bitso.com and redeem their code.

### Bank Wire

Execute a standard international bank wire via this outlet.
