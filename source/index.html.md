---
title: Bitso API Reference

language_tabs:
  - shell: cURL
  - javascript: NodeJS
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

## Notations

**Major** denotes the cryptocurrency, in our case Bitcoin (BTC).

**Minor** denotes fiat currencies such as Mexican Peso (MXN), etc

An order book is always referred to in the API as "Major_Minor". For example: "**btc_mxn**"

## Precision

We return decimal numbers as strings to preserve full precision across platforms. We recommend you also convert your numbers to string in order to avoid undesired consequences from precision and truncation errors.

## Client Libraries

The following client libraries will allow you to integrate quickly with our APIs

* [Java](https://github.com/bitsoex/bitso-java)
* [NodeJS](https://github.com/etiennetatur/bitso-api)
* [.NET](http://www.nuget.org/packages/Bitso)

# Public Endpoints

## Ticker

```shell
curl "https://bitso.com/api/v2/ticker?book=btc_mxn"
```

> The JSON dictionary retuned by the API looks like this:

```json
{
    "volume": "22.31349615",
    "high": "5750.00",
    "last": "5633.98",
    "low": "5450.00",
    "vwap": "5393.45",
    "ask": "5632.24",
    "bid": "5520.01",
    "timestamp": "1447348096"
}
```

This endpoint returns trading information from the specified book.

### HTTP Request

`GET https://api.bitso.com/v2/ticker`

### Query Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**book** | btc_mxn | No | Specifies which book to use

### JSON Response

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**last** | String | Last traded price | Minor/Major
**high** | String | Last 24 hours price high | Minor/Major
**low** | String | Last 24 hours price low | Minor/Major
**vwap** | String | Last 24 hours volume weighted average price: [vwap](http://en.wikipedia.org/wiki/Volume-weighted_average_price) | Minor/Major
**volume** | String | Last 24 hours volume | Major
**bid** | String | Highest buy order | Minor/Major
**ask** | String | Lowest sell order | Minor/Major

## Order Book

```shell
curl "https://api.bitso.com/v2/order_book?book=btc_mxn&group=1"
```

> The JSON dictionary retuned by the API looks like this:

```json
{
    "asks": [
        ["5632.24", "1.34491802"],
        ["5632.25", "1.00000000"],
        ["5633.99", "0.61980799"]
    ],
    "bids": [
        ["5520.01", "0.34493053"],
        ["5520.00", "0.08000000"],
        ["5486.01", "0.00250000"]
    ],
    "timestamp": "1447348416"
}
```

This endpoint returns a list of all open orders in the specified book.

### HTTP Request

`GET https://api.bitso.com/v2/order_book`

### Query Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**book** | btc_mxn | No | Specifies which book to use
**group** | 1 | No | Group orders with the same price (0 - false; 1 - true)

### JSON Response

Returns JSON dictionary with "bids" and "asks". Each is a JSON Array of open orders and each open order is represented as a JSON Array of price (minor) and amount (major).

Field Name | Type | Description
---------- | ---- | -----------
**asks** | JSON Array | List of open asks
**bids** | JSON Array | List of open bids

**asks** and **bids** JSON Array format:

Array Position | Type | Description | Units
-------------- | ---- | ----------- | -----
**0** | String | Order Price | Minor
**1** | String | Order Amount | Major

## Transactions

```shell
curl "https://api.bitso.com/v2/transactions?book=btc_mxn&time=minute"
```

> The JSON Array retuned by the API looks like this:

```json
[
    {
        "date": "1447350465",
        "amount": "0.02000000",
        "side": "buy",
        "price": "5545.01",
        "tid": 55845
    },
    {
        "date": "1447347533",
        "amount": "0.33723939",
        "side": "sell",
        "price": "5633.98",
        "tid": 55844
    }
]
```

This endpoint returns a list of recent trades from the specified book.

### HTTP Request

`GET https://api.bitso.com/v2/transactions`

### Query Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**book** | btc_mxn | No | Specifies which book to use
**time** | hour | No | Time frame for transaction export ("minute" - 1 minute, "hour" - 1 hour)

### JSON Response

Returns descending JSON Array of transactions. Every element in the array is a JSON dictionary:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**date** | String | Unix timestamp | Seconds
**tid** | Long | transaction id | -
**price** | String | Price per unit of major | Minor
**amount** | String | Major amount transacted | Major
**side** | String | Indicates the maker order side (maker order is the order that was open on the order book) | -

# Private Endpoints

Private endpoints are used to manage your account and your orders. These requests must be signed (more about this below).

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

```javascript
var secret = "BITSO API SECRET";
var key = "BITSO API KEY";
var client_id = "BITSO CLIENT ID";
var nonce = new Date().getTime();

// Create the signature
var Data = nonce + client_id + key;
var crypto = require('crypto');
var signature = crypto.createHmac('sha256', secret).update(Data).digest('hex');

// Build the request parameters
var querystring = require('querystring');
var data = querystring.stringify({
  key: key,
  nonce: nonce,
  signature: signature
});
var options = {
  host: 'api.bitso.com',
  port: 443,
  path: '/v2/balance',
  method: 'POST',
  headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
};

// Send request
var http = require('https');
var req = http.request(options, function(res) {
    res.on('data', function (chunk) {
        console.log("body: " + chunk);
    });
});
req.write(data);
req.end();
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
message = nonce + bitso_key + bitso_client_id
signature = OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new('sha256'), bitso_secret, message)

# Build the request parameters
o = {
  :key => bitso_key,
  :nonce => nonce.to_i,
  :signature => signature
}
body = JSON.generate(o)

# Send request
response = Typhoeus::Request.new(
  "https://api.bitso.com/v2/balance",
  method: "post",
  body: body,
  headers: { "Content-Type" => "application/json" }
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
        String message = nonce + bitsoKey + bitsoClientId;
        String signature = "";
        byte[] secretBytes = bitsoSecret.getBytes();
        SecretKeySpec localMac = new SecretKeySpec(secretBytes, "HmacSHA256");
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(localMac);
        byte[] arrayOfByte = mac.doFinal(message.getBytes());
        BigInteger localBigInteger = new BigInteger(1, arrayOfByte);
        signature = String.format("%0" + (arrayOfByte.length << 1) + "x", new Object[] { localBigInteger });

        // Build the request parameters
        JSONObject o = new JSONObject();
        o.put("key", bitsoKey);
        o.put("nonce", nonce);
        o.put("signature", signature);
        String body = o.toString();
        String url = "https://api.bitso.com/v2/balance";

        // Send request
        HttpPost postRequest = new HttpPost(url);
        postRequest.addHeader("Content-Type", "application/json");
        postRequest.setEntity(new StringEntity(body));

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

  // Build the request parameters
  $o = array(
      'key'       => $bitsoKey,
      'nonce'     => $nonce,
      'signature' => $signature
  );
  $body = json_encode($o);

  // Send request
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, 'https://api.bitso.com/v2/balance');
  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
  curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'Content-Type: application/json; charset=utf-8',
      'Content-Length: ' . strlen($body))
  );
  $result = curl_exec($ch);

  echo $result;
?>
```

All REST requests should be valid JSON. You need to POST 3 fields as a JSON payload to the API in order to perform authentication:

* **key** – The API Key you generated
* **nonce** – An integer that must be unique and increasing for each API call (we recommend using a UNIX timestamp)
* **signature** – See below

### Signature

The signature is generated by creating a SHA256 HMAC using the **Bitso API Secret** on the concatenation of **nonce** + **Bitso Client ID** + **Bitso API Key** (no '+' signs in the concatenated string) and hex-encode the output. The **nonce** value should be the same as the **nonce** field in the json dictionary.

## Account balance

> The JSON dictionary retuned by the API looks like this:

```json
{
    "btc_available": "46.67902107",
    "fee": "1.0000",
    "mxn_available": "26864.57",
    "btc_balance": "46.67902107",
    "mxn_reserved": "0.00",
    "mxn_balance": "26864.57",
    "btc_reserved": "0.00000000"
}
```

This endpoint returns information of all balances.

### HTTP Request

`POST https://api.bitso.com/v2/balance`

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)

### JSON Response

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**mxn_balance** | String | MXN balance | MXN
**btc_balance** | String | BTC balance | BTC
**mxn_reserved** | String | MXN locked in open orders | MXN
**btc_reserved** | String | BTC locked in open orders | BTC
**mxn_available** | String | MXN available for trading (balance - reserved) | MXN
**btc_available** | String | BTC available for trading (balance - reserved) | BTC
**fee** | String | Customer trading fee as a *percentage* | -

## User Transactions

> The JSON dictionary retuned by the API looks like this:

```json
[
    {
        "datetime": "2015-10-10 16:19:33",
        "method": "Bitcoin",
        "btc": "0.48650929",
        "type": 0
    },
    {
        "datetime": "2015-10-09 13:49:00",
        "method": "SPEI Transfer",
        "mxn": "-1800.15",
        "type": 1
    },
    {
        "btc": "-0.25232073",
        "datetime": "2015-10-09 13:45:46",
        "mxn": "1023.77",
        "rate": "4057.45",
        "id": 51756,
        "type": 2,
        "order_id": "19vaqiv72drbphig81d3y1ywri0yg8miihs80ng217drpw7xyl0wmytdhtby2ygk"
    }
]
```

Returns a list of the user's transactions.

### HTTP Request

`POST https://api.bitso.com/v2/user_transactions`

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**offset** | 0 | No | Skip that many transactions before beginning to return results
**limit** | 100 | No | Limit result to that many transactions
**sort** | desc | Sorting by date and time (asc - ascending; desc - descending)
**book** | btc_mxn | No | Specifies which book to use


### JSON Response

Returns a descending JSON Array of transactions. Every element in the array is a JSON dictionary:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**datetime** | String | Date and time | -
**id** | long | Unique identifier (only for trades) | -
**type** | int | Transaction type (0 - deposit; 1 - withdrawal; 2 - trade) | -
**method** | String | Deposit or withdrawal method | -
**(minor currency code)** | String | The minor currency amount | Minor
**(major currency code)** | String | The major currency amount | Major
**order_id** | String | A 64 character long hexadecimal string representing the order that was fully or partially filled (only for trades) | -
**rate** | String | Price per minor (only for trades) | Minor

## Open Orders

> The JSON dictionary retuned by the API looks like this:

```json
[
    {
        "amount": "0.01000000",
        "datetime": "2015-11-12 12:37:01",
        "price": "5600.00",
        "id": "543cr2v32a1h684430tvcqx1b0vkr93wd694957cg8umhyrlzkgbaedmf976ia3v",
        "type": "1",
        "status": "1"
    },
    {
        "amount": "0.12680000",
        "datetime": "2015-11-12 12:33:47",
        "price": "4000.00",
        "id": "qlbga6b600n3xta7actori10z19acfb20njbtuhtu5xry7z8jswbaycazlkc0wf1",
        "type": "0",
        "status": "0"
    },
    {
        "amount": "1.12560000",
        "datetime": "2015-11-12 12:33:23",
        "price": "6123.55",
        "id": "d71e3xy2lowndkfmde6bwkdsvw62my6058e95cbr08eesu0687i5swyot4rf2yf8",
        "type": "1",
        "status": "0"
    }
]
```

Returns a list of the user's open orders.

### HTTP Request

`POST https://api.bitso.com/v2/open_orders`

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**book** | btc_mxn | No | Specifies which book to use


### JSON Response

Returns a JSON Array of open orders. Every element in the array is a JSON dictionary:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**datetime** | String | Date and time | -
**id** | String | The order ID | -
**type** | String | The order type (0 - buy; 1 - sell) | -
**price** | String | The order's price | Minor
**amount** | String | The order's major currency amount | Major
**status** | String | The order's status (0 - active; 1 - partially filled) | -

## Lookup Order

> The JSON dictionary retuned by the API looks like this:

```json
[{
    "amount": "0.01000000",
    "created": "2015-11-12 12:37:01",
    "price": "5600.00",
    "book": "btc_mxn",
    "id": "543cr2v32a1h684430tvcqx1b0vkr93wd694957cg8umhyrlzkgbaedmf976ia3v",
    "type": "1",
    "updated": "2015-11-12 12:37:40",
    "status": "-1"
}]
```

Returns a list of details for 1 or more orders

### HTTP Request

`POST https://api.bitso.com/v2/lookup_order`

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**id** | - | Yes | A single or array of 64 characters long hexadecimal strings taken from the list of orders


### JSON Response

Returns a JSON Array with details about 1 or more orders. Each order is represented by a JSON dictionary:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**id** | String | The order ID  passed to the API | -
**book** | String | Which orderbook the order belongs to (not shown when status = 0) | -
**price** | String | The order's price | Minor
**amount** | String | The order's major currency amount | Major
**type** | String | The order type (0 - buy; 1 - sell) | -
**status** | String | The order's status (-1 - cancelled; 0 - active; 1 - partially filled; 2 - complete) | -
**created** | String | The date the order was created | -
**updated** | String | The date the order was last updated (not shown when status = 0)


## Cancel Order

> The string retuned by the API looks like this:

```json
"true"
```

Cancels an open order

### HTTP Request

`POST https://api.bitso.com/v2/cancel_order`

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**id** | - | Yes | A 64 characters long hexadecimal string taken from the list of orders

### HTTP Response

Returns "true" (quotation marks included) if the order has been found and canceled. Otherwise it returns a JSON dictionary indicating the error

## Place a Buy Order

> The JSON dictionary retuned by the API looks like this:

```json
{
    "amount": "0.10000000",
    "datetime": "2015-11-12 12:53:28",
    "price": "100.00",
    "book": "btc_mxn",
    "id": "kidxgibf009w85qykad1sdoktdmdlbo6t23akepkfzgn56mphzracfv6thjfs8lm",
    "type": "0",
    "status": "0"
}
```

Places a buy order (both limit and market orders are available)

### HTTP Request

`POST https://api.bitso.com/v2/buy`

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**book** | btc_mxn | No | Specifies which book to use
**amount** | - | Yes | Amount of major currency to buy
**price** | - | No | If supplied, this will place a **limit order** to buy at the specified price. If not supplied, this will place a **market order** to buy the amount of major currency specified in **amount** at the market rate

### JSON Response

Returns a JSON dictionary representing the order:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**id** | String | The order ID | -
**book** | String | Which orderbook the order belongs to (not shown when status = 0) | -
**datetime** | String | The date and time
**type** | String | The order type (0 - buy; 1 - sell) | -
**status** | String | **(Only for limit orders)** The order's status (-1 - cancelled; 0 - active; 1 - partially filled; 2 - complete) | -
**price** | String | **(Only for limit orders)** The order's price | Minor
**amount** | String | **(Only for limit orders)** The order's major amount | Major

## Place a Sell Order

> The JSON dictionary retuned by the API looks like this:

```json
{
    "amount": "0.01000000",
    "datetime": "2015-11-12 13:29:33",
    "price": "10000.00",
    "book": "btc_mxn",
    "id": "5umhs73uxry9ykblk923xxi48j4jhcwm7i40q7vnztxxd8jyil1gjkkr4obl1789",
    "type": "1",
    "status": "0"
}
```

Places a sell order (both limit and market orders are available)

### HTTP Request

`POST https://api.bitso.com/v2/sell`

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**book** | btc_mxn | No | Specifies which book to use
**amount** | - | Yes | Amount of major currency to sell
**price** | - | No | If supplied, this will place a **limit order** to sell at the specified price. If not supplied, this will place a **market order** to sell the amount of major currency specified in **amount** at the market rate

### JSON Response

Returns a JSON dictionary representing the order:

Field Name | Type | Description | Units
---------- | ---- | ----------- | -----
**id** | String | The order ID | -
**book** | String | Which orderbook the order belongs to (not shown when status = 0) | -
**datetime** | String | The date and time
**type** | String | The order type (0 - buy; 1 - sell) | -
**status** | String | **(Only for limit orders)** The order's status (-1 - cancelled; 0 - active; 1 - partially filled; 2 - complete) | -
**price** | String | **(Only for limit orders)** The order's price | Minor
**amount** | String | **(Only for limit orders)** The order's major amount | Major

## Bitcoin Deposit

> The string retuned by the API looks like this:

```json
"3CaPt93nYFzapDHMk6zZsXqiD8dJqKjWvb"
```

Gets a Bitcoin deposit address to fund your account

### HTTP Request

`POST https://api.bitso.com/v2/bitcoin_deposit_address`

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)

### HTTP Response

Returns a bitcoin deposit address (quotation marks included) that can be used to fund your account

## Bitcoin Withdrawal

> The string retuned by the API looks like this:

```json
"ok"
```

Triggers a bitcoin withdrawal from your account

### HTTP Request

`POST https://api.bitso.com/v2/bitcoin_withdrawal`

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**amount** | - | Yes | The amount of BTC to withdraw from your account
**address** | - | Yes | The Bitcoin address we will send the amount to

### HTTP Response

Returns “ok” (quotation marks included) if the withdrawal was successfully triggered. Otherwise it returns a JSON dictionary indicating the error

## Ripple Withdrawal

> The string retuned by the API looks like this:

```json
"ok"
```

Triggers a Ripple withdrawal from your account

### HTTP Request

`POST https://api.bitso.com/v2/ripple_withdrawal`

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**currency** | - | Yes | The currency to withdraw
**amount** | - | Yes | The amount of currency to withdraw from your account
**address** | - | Yes | The ripple address we will send the amount to

### HTTP Response

Returns “ok” (quotation marks included) if the withdrawal was successfully triggered. Otherwise it returns a JSON dictionary indicating the error

<aside class="warning">
<b>The Ripple address associated to your account for deposits will be updated accordingly!</br>
Please ensure that any subsequent Ripple funding emanates from this address.</b>
</aside>

## Bank Withdrawal (SPEI)

> The string retuned by the API looks like this:

```json
"ok"
```

Triggers a SPEI withdrawal from your account.
These **withdrawals are immediate** during banking hours (M-F 9:00AM - 5:00PM Mexico City Time).


### HTTP Request

`POST https://api.bitso.com/v2/spei_withdrawal`

### Body Parameters

Parameter | Default | Required | Description
--------- | ------- | -------- | -----------
**key** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**signature** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**nonce** | - | Yes | See [Creating and Signing Requests](#creating-and-signing-requests)
**amount** | - | Yes | The amount of MXN to withdraw from your account
**recipient_given_names** | - | Yes | The recipient's first and middle name(s)
**recipient_family_names** | - | Yes | The recipient's last name
**clabe** | - | Yes | The [CLABE](https://en.wikipedia.org/wiki/CLABE) number where the funds will be sent to
**notes_ref** | - | Yes | The alpha-numeric reference number for this SPEI
**numeric_ref** | - | Yes | The numeric reference for this SPEI

### HTTP Response

Returns “ok” (quotation marks included) if the withdrawal was successfully triggered. Otherwise it returns a JSON dictionary indicating the error
