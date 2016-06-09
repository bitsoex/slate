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

## HTTP and WebSocket APIs

Bitso offers a HTTP API, and a WebSocket API. The HTTP API exposes both public and private functions. The WebSocket API offers realtime streaming of market-data, such as the Bitso orderbook state.

## Transfer API

Bitso’s powerful Transfer API allows for simple integration for routing Bitcoin payments directly through to a choice of Mexican Peso end-points. Please contact us if you're interested in using this API, access is available on request.

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
* [Python](https://github.com/bitsoex/bitso-py)
* [Objective-C](https://github.com/bitsoex/bitso-ios-sdk)

# Public Endpoints

## Ticker

```shell
curl "https://bitso.com/api/v2/ticker?book=btc_mxn"
```

> The JSON dictionary returned by the API looks like this:

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

> The JSON dictionary returned by the API looks like this:

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

> The JSON Array returned by the API looks like this:

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

> The JSON dictionary returned by the API looks like this:

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

> The JSON dictionary returned by the API looks like this:

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

> The JSON dictionary returned by the API looks like this:

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

> The JSON dictionary returned by the API looks like this:

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

> The string returned by the API looks like this:

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

> The JSON dictionary returned by the API looks like this:

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
**amount** | - | Yes | For limit orders, this indicates the amount of major currency to buy. For market orders, this indicates the amount of minor currency to spend
**price** | - | No | If supplied, this will place a **limit order** to buy at the specified price. If not supplied, this will place a **market order** and spend the amount of minor currency specified in **amount** to buy major currency at the market rate.

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

> The JSON dictionary returned by the API looks like this:

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

> The string returned by the API looks like this:

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

> The string returned by the API looks like this:

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

> The string returned by the API looks like this:

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

> The string returned by the API looks like this:

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

> Once you've succesfuly subscribed to a channel, listen for messages and handle them appropriately:

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

> The JSON dictionary returned by the API looks like this:

```json
{
   "quote":{
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
   },
   "success":true
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

> The JSON dictionary returned by the API looks like this:

```json
{
   "order":{
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
   },
   "success":true
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
