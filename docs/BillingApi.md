# gpuai_sdk.BillingApi

All URIs are relative to *https://api.gpu.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_card_checkout**](BillingApi.md#create_card_checkout) | **POST** /billing/deposits/card/checkout | Top up the balance with Stripe Checkout
[**create_card_deposit**](BillingApi.md#create_card_deposit) | **POST** /billing/deposits/card | Top up the balance by charging a saved card
[**create_crypto_deposit**](BillingApi.md#create_crypto_deposit) | **POST** /billing/deposits/crypto | Create a stablecoin deposit
[**download_invoice_pdf**](BillingApi.md#download_invoice_pdf) | **GET** /billing/invoices/{id}/pdf | Download an invoice PDF
[**get_balance**](BillingApi.md#get_balance) | **GET** /billing/balance | Get the org credit balance
[**get_billing_details**](BillingApi.md#get_billing_details) | **GET** /billing/details | Get billing details
[**get_card_deposit**](BillingApi.md#get_card_deposit) | **GET** /billing/deposits/card/{id} | Get a card deposit&#39;s status
[**get_deposit**](BillingApi.md#get_deposit) | **GET** /billing/deposits/{id} | Get one stablecoin deposit
[**get_spending_limit**](BillingApi.md#get_spending_limit) | **GET** /billing/spending-limit | Get the org spending limit
[**list_deposits**](BillingApi.md#list_deposits) | **GET** /billing/deposits | List stablecoin deposits
[**list_invoices**](BillingApi.md#list_invoices) | **GET** /billing/invoices | List invoices
[**list_payment_methods**](BillingApi.md#list_payment_methods) | **GET** /billing/payment-methods | List saved cards
[**update_billing_details**](BillingApi.md#update_billing_details) | **PATCH** /billing/details | Update billing details
[**update_spending_limit**](BillingApi.md#update_spending_limit) | **PUT** /billing/spending-limit | Set the org spending limit


# **create_card_checkout**
> CardDeposit create_card_checkout(create_card_checkout_request)

Top up the balance with Stripe Checkout

Creates the same Stripe Checkout session as the dashboard's "Add credits" and returns its URL as `checkout_url`. Nothing is charged until the customer pays on that page; paying saves the card for later `POST /billing/deposits/card` top-ups. Requires the `billing:write` scope AND an organization admin. `deposit_id` is the Checkout Session id; poll `GET /billing/deposits/card/{id}`.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.card_deposit import CardDeposit
from gpuai_sdk.models.create_card_checkout_request import CreateCardCheckoutRequest
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)
    create_card_checkout_request = gpuai_sdk.CreateCardCheckoutRequest() # CreateCardCheckoutRequest | 

    try:
        # Top up the balance with Stripe Checkout
        api_response = api_instance.create_card_checkout(create_card_checkout_request)
        print("The response of BillingApi->create_card_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->create_card_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_card_checkout_request** | [**CreateCardCheckoutRequest**](CreateCardCheckoutRequest.md)|  | 

### Return type

[**CardDeposit**](CardDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | &#x60;validation-error&#x60; — amount below $5.00. |  -  |
**403** | &#x60;forbidden&#x60; — not an organization admin. &#x60;org-frozen&#x60; — the organization cannot add funds. |  -  |
**422** | &#x60;card-topup-limit&#x60; — over the per-charge limit. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_card_deposit**
> CardDeposit create_card_deposit(create_card_deposit_request, idempotency_key=idempotency_key)

Top up the balance by charging a saved card

Charges one of the organization's saved cards off-session and returns the Stripe PaymentIntent id as `deposit_id`. The balance is credited a few seconds later by GPU.ai's Stripe webhook, exactly like a deposit made on the website, including any deposit-match promotion and its card hold; poll `GET /billing/deposits/card/{id}` to see it land.

Requires the `payments:write` scope, carried by `full_access` keys (what `gpu login` issues to an organization admin) and by an explicit `{"payments": "write"}` grant, never by `standard` or `read_only`. The key owner must also be an organization admin.

Limits (server configuration, defaults shown): at most $10,000 per charge and $25,000 of saved-card charges per organization in any rolling 24 hours (declined or canceled charges do not count, and a charge left waiting for 3-D Secure stops counting after an hour). Saved-card charging can be switched off by an operator; it then answers `503 card-topup-disabled` and `POST /billing/deposits/card/checkout` still works.

An `Idempotency-Key` header is REQUIRED. Retrying with the same key replays the first attempt (here and at Stripe) instead of charging again; use a new key for each deliberate top-up. When the card issuer requires 3-D Secure, the response has `status: requires_action` and an `action_url` to open in a browser.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.card_deposit import CardDeposit
from gpuai_sdk.models.create_card_deposit_request import CreateCardDepositRequest
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)
    create_card_deposit_request = gpuai_sdk.CreateCardDepositRequest() # CreateCardDepositRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Top up the balance by charging a saved card
        api_response = api_instance.create_card_deposit(create_card_deposit_request, idempotency_key=idempotency_key)
        print("The response of BillingApi->create_card_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->create_card_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_card_deposit_request** | [**CreateCardDepositRequest**](CreateCardDepositRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**CardDeposit**](CardDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Charged, processing, or awaiting 3-D Secure. |  -  |
**400** | &#x60;validation-error&#x60; — amount below $5.00. &#x60;idempotency-key-required&#x60; — no Idempotency-Key header. |  -  |
**402** | &#x60;card-declined&#x60; — the issuer declined; nothing was charged. |  -  |
**403** | &#x60;insufficient_scope&#x60; — the key lacks &#x60;payments:write&#x60;. &#x60;forbidden&#x60; — not an organization admin. &#x60;org-frozen&#x60; — the organization cannot add funds. &#x60;region_not_supported&#x60; — GPU.ai can&#39;t provide this service in the caller&#39;s country or region. |  -  |
**409** | &#x60;no-saved-card&#x60; — no (matching) saved card; use &#x60;POST /billing/deposits/card/checkout&#x60; once to save one. &#x60;idempotency-key-used&#x60; — this key belongs to a top-up that already failed. |  -  |
**422** | &#x60;card-topup-limit&#x60; — over the per-charge limit. &#x60;card-topup-daily-limit&#x60; — over the organization&#39;s rolling-24h limit; the detail says how much is left. |  -  |
**503** | &#x60;card-topup-disabled&#x60; — saved-card charging is switched off; use Checkout. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_crypto_deposit**
> CryptoDeposit create_crypto_deposit(create_crypto_deposit_request)

Create a stablecoin deposit

Creates a deposit intent and returns the payment address and the exact token amount to send. Requires the `billing:write` scope; any member of the organization may add funds. Send the exact `pay_amount` of `asset` on `chain` and no other network — funds sent on a different network are not detected automatically. Returns 404 when stablecoin deposits are not enabled for this deployment.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.create_crypto_deposit_request import CreateCryptoDepositRequest
from gpuai_sdk.models.crypto_deposit import CryptoDeposit
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)
    create_crypto_deposit_request = gpuai_sdk.CreateCryptoDepositRequest() # CreateCryptoDepositRequest | 

    try:
        # Create a stablecoin deposit
        api_response = api_instance.create_crypto_deposit(create_crypto_deposit_request)
        print("The response of BillingApi->create_crypto_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->create_crypto_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_crypto_deposit_request** | [**CreateCryptoDepositRequest**](CreateCryptoDepositRequest.md)|  | 

### Return type

[**CryptoDeposit**](CryptoDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | &#x60;validation-error&#x60; — &#x60;amount_cents&#x60; is below the configured minimum. &#x60;unsupported-chain-asset&#x60; — the chain/asset pair is not available. &#x60;invalid-request&#x60; — malformed JSON body.  |  -  |
**403** | &#x60;org-frozen&#x60; — the organization cannot add funds; contact support. &#x60;region_not_supported&#x60; — GPU.ai can&#39;t provide this service in the caller&#39;s country or region. |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**503** | &#x60;payment-source-unavailable&#x60; — deposits are temporarily unavailable; retry shortly. |  -  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_invoice_pdf**
> bytes download_invoice_pdf(id)

Download an invoice PDF

Returns one invoice as a PDF, including the organization's billing details and full Tax ID. Requires the `billing:read` scope. An invoice belonging to another organization returns the same 404 as one that does not exist.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)
    id = 'id_example' # str | The invoice id.

    try:
        # Download an invoice PDF
        api_response = api_instance.download_invoice_pdf(id)
        print("The response of BillingApi->download_invoice_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->download_invoice_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The invoice id. | 

### Return type

**bytes**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The invoice PDF. |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance**
> Balance get_balance()

Get the org credit balance

Returns the organization's credit balance, its auto-pay configuration, and the live burn rate. Requires the `billing:read` scope. The organization is taken from the authenticated API key, never from a parameter.

Divide `balance_cents` by `burn_cents_per_hour` for the remaining runway in hours. The quotient is undefined in three cases a caller must keep apart: `burn_cents_per_hour` is 0 (nothing running, so the balance funds unbounded idle time), it is `null` (the burn rate could not be determined — NOT the same as idle), or the balance is already at or below zero.

This is the balance itself — for spend against a configured cap see `/billing/spending-limit`, and for past consumption see `/usage`.

`runway_hours` does that division for you, adding serverless inference spend over the last hour to the burn. While it is under the low-balance threshold (2 hours by default) and auto-pay is off or failing, every authenticated response carries the `GPUAI-Balance-Warning` header.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.balance import Balance
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)

    try:
        # Get the org credit balance
        api_response = api_instance.get_balance()
        print("The response of BillingApi->get_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_balance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Balance**](Balance.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * GPUAI-Balance-Warning -  <br>  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_details**
> BillingDetails get_billing_details()

Get billing details

Returns the company name, address and Tax ID printed on the organization's invoices. Requires the `billing:read` scope. The Tax ID is stored encrypted and is only ever returned masked (`tax_id_masked`); the full value is printed on the organization's own invoice PDFs and nowhere else.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.billing_details import BillingDetails
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)

    try:
        # Get billing details
        api_response = api_instance.get_billing_details()
        print("The response of BillingApi->get_billing_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_billing_details: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BillingDetails**](BillingDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_card_deposit**
> CardDepositStatus get_card_deposit(id)

Get a card deposit's status

Reports whether a card top-up has been credited to the balance, and what any deposit-match promotion decided for it. Requires the `billing:read` scope. Reads GPU.ai's ledger, never Stripe: an id that belongs to another organization reads as `pending`.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.card_deposit_status import CardDepositStatus
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)
    id = 'id_example' # str | A card deposit id (`pi_...` or `cs_...`).

    try:
        # Get a card deposit's status
        api_response = api_instance.get_card_deposit(id)
        print("The response of BillingApi->get_card_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_card_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A card deposit id (&#x60;pi_...&#x60; or &#x60;cs_...&#x60;). | 

### Return type

[**CardDepositStatus**](CardDepositStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | &#x60;validation-error&#x60; — not a card deposit id. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deposit**
> CryptoDeposit get_deposit(id)

Get one stablecoin deposit

Returns a single deposit belonging to the caller's organization. Requires the `billing:read` scope. A deposit belonging to another organization returns the same `404 deposit-not-found` as one that does not exist — deliberately, so this endpoint cannot be used to test whether a deposit id is real. Also 404 when stablecoin deposits are not enabled for this deployment.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.crypto_deposit import CryptoDeposit
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)
    id = 'id_example' # str | The deposit id.

    try:
        # Get one stablecoin deposit
        api_response = api_instance.get_deposit(id)
        print("The response of BillingApi->get_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The deposit id. | 

### Return type

[**CryptoDeposit**](CryptoDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | &#x60;deposit-not-found&#x60; — no such deposit, or it belongs to another organization. &#x60;not-found&#x60; — the feature is not enabled.  |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spending_limit**
> SpendingLimit get_spending_limit()

Get the org spending limit

Returns the organization's monthly spending limit and opt-in daily spend cap, with the current month and day spend. Requires the `billing:read` scope. Returns 404 when no limit is configured.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.spending_limit import SpendingLimit
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)

    try:
        # Get the org spending limit
        api_response = api_instance.get_spending_limit()
        print("The response of BillingApi->get_spending_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_spending_limit: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SpendingLimit**](SpendingLimit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deposits**
> ListDeposits200Response list_deposits()

List stablecoin deposits

Returns the organization's stablecoin deposits, newest first, capped at 50. Requires the `billing:read` scope. The organization is taken from the authenticated API key, never from a parameter. Returns 404 when stablecoin deposits are not enabled for this deployment.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.list_deposits200_response import ListDeposits200Response
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)

    try:
        # List stablecoin deposits
        api_response = api_instance.list_deposits()
        print("The response of BillingApi->list_deposits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_deposits: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDeposits200Response**](ListDeposits200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> InvoiceList list_invoices(limit=limit, cursor=cursor)

List invoices

Returns the organization's invoices, newest first. Every payment (card purchase, auto-pay top up, stablecoin deposit) has one; promotional credit does not. Requires the `billing:read` scope.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.invoice_list import InvoiceList
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)
    limit = 25 # int |  (optional) (default to 25)
    cursor = 'cursor_example' # str | The `next_cursor` from the previous page. (optional)

    try:
        # List invoices
        api_response = api_instance.list_invoices(limit=limit, cursor=cursor)
        print("The response of BillingApi->list_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 25]
 **cursor** | **str**| The &#x60;next_cursor&#x60; from the previous page. | [optional] 

### Return type

[**InvoiceList**](InvoiceList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_methods**
> ListPaymentMethods200Response list_payment_methods()

List saved cards

Returns the organization's saved cards as brand, last 4 digits and expiry. Card numbers are never returned. Requires the `payments:read` scope AND an organization admin (members get 403). An organization with no saved card returns an empty list. `saved_card_charge_allowed` says whether the calling key may charge these cards (`payments:write`).


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.list_payment_methods200_response import ListPaymentMethods200Response
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)

    try:
        # List saved cards
        api_response = api_instance.list_payment_methods()
        print("The response of BillingApi->list_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_payment_methods: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListPaymentMethods200Response**](ListPaymentMethods200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | &#x60;forbidden&#x60; — the key owner is not an organization admin. &#x60;insufficient_scope&#x60; — the key lacks &#x60;payments:read&#x60;. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_details**
> BillingDetails update_billing_details(update_billing_details_request, idempotency_key=idempotency_key)

Update billing details

Updates the billing details printed on invoices. Requires the `billing:write` scope and an org admin's key. Omitted fields keep their value. `tax_id` replaces the stored Tax ID (and needs `tax_id_type` unless one is already stored); an empty `tax_id` removes it. Returns 503 `tax-id-unavailable` when this deployment cannot store a Tax ID.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.billing_details import BillingDetails
from gpuai_sdk.models.update_billing_details_request import UpdateBillingDetailsRequest
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)
    update_billing_details_request = gpuai_sdk.UpdateBillingDetailsRequest() # UpdateBillingDetailsRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Update billing details
        api_response = api_instance.update_billing_details(update_billing_details_request, idempotency_key=idempotency_key)
        print("The response of BillingApi->update_billing_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->update_billing_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_billing_details_request** | [**UpdateBillingDetailsRequest**](UpdateBillingDetailsRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**BillingDetails**](BillingDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error response (RFC 7807) |  -  |
**403** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**503** | Error response (RFC 7807) |  -  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_spending_limit**
> SpendingLimit update_spending_limit(update_spending_limit_request)

Set the org spending limit

Sets the monthly spending limit and optionally sets or clears the opt-in daily spend cap. Requires the `billing:write` scope AND org-admin privileges (a non-admin member gets 403). `daily_limit_dollars` uses pointer semantics: omit to leave the cap unchanged, 0 to clear it, a positive value to set it.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.spending_limit import SpendingLimit
from gpuai_sdk.models.update_spending_limit_request import UpdateSpendingLimitRequest
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)
    update_spending_limit_request = gpuai_sdk.UpdateSpendingLimitRequest() # UpdateSpendingLimitRequest | 

    try:
        # Set the org spending limit
        api_response = api_instance.update_spending_limit(update_spending_limit_request)
        print("The response of BillingApi->update_spending_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->update_spending_limit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_spending_limit_request** | [**UpdateSpendingLimitRequest**](UpdateSpendingLimitRequest.md)|  | 

### Return type

[**SpendingLimit**](SpendingLimit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Error response (RFC 7807) |  -  |
**422** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

