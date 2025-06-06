---
layout: page
title: Horizon Cloud Service Next Gen API
hide:
  #- navigation
  - toc
---

![Horizon Cloud](../../../assets/logos/Horizon-Cloud-v-lm.png){ align=right }

## What is the Horizon Cloud Service Next Gen

Horizon Cloud Next Gen is a modern cloud-first, multi-cloud Desktop as a Service (DaaS) deployment with Thin Edge Infrastructure. The service provides you with a global view of your desktops and applications spanning across on-premises and cloud environments. Regardless of the location of your desktop and application deployments, Horizon Cloud enables you to consistently manage and monitor them.

## Onboarding Customer to Data Center (HDC)

Once you receive your Cloud Services Portal (CSP) invitation link in the email, please redeem it by clicking on the url. If you have not received an email, please reach out to Omnissa.

- Login to ***CSP*** ([https://connect.omnissa.com](https://connect.omnissa.com)).
- You have an option to create to use an existing CSP organization or create a new one to onboard to Horizon Cloud Services.
- As an organization owner, you need to go to "Identity & Access Management" and edit the existing user to add the **Administrator** role. Customers may add more users and assign the role above. The Administrator role is required to access the entire UI and API.

> All API calls need a bearer token generated from an API token. Follow these steps to get your API token.
>
> - Go to your account and API Tokens tab.
> - Click on Generate a New API TOKEN link. Provide a name for the API token and keep the defaults.
> - Save the API token information and keep it handy.

## General API Notes

### Authentication

!!!Important
    Please take a note of below two steps.  
    The same authentication scheme ("Authorization: Bearer") is required for all API calls

### Obtain a CSP Access Token

##### Login to CSP Portal and obtain either

- CSP Org ID
  Take the 'Long Organization ID' from the 'View Organization' page in CSP

**OR**

- CSP oAuth Application ID and oAuth Application secret

These can be found when originally creating the OAuth App within your Organization page, or can be regenerated from the same area.

!!!Note
    OAuth App should have the Horizon Cloud Service listed as a Service Role

##### Create a CSP API Token

> See the previous section for details about creating an API Token. All API calls require authentication using an Access Token.

### Obtain an Access Token

Choose one of the following methods:

##### To obtain an Access Token by using a CSP API Token

One authentication scheme is to use an "Access Token", which is obtained by making an API call that takes your API Token as input, and returns an Access Token. This Access Token is then supplied as a bearer token in an "Authentication" header with every API request. All the following steps will assume this authentication header, it will not be explicitly mentioned each time.

Note `{csp-url}` value will typically be [https://connect.omnissa.com](https://connect.omnissa.com)

```json
  POST https://{csp-url}/csp/gateway/am/api/auth/api-tokens/authorize
```

```json
  Headers:      Content-Type : application/x-www-form-urlencoded
  Request Body: refresh_token : {YOUR-API-TOKEN-FROM-GETTING-STARTED-STEP-2}
  Response:
  {
    "id_token": {id-token-value},
    "token_type": "bearer",
    "expires_in": 1799,
    "scope": "scope.....{snippet}",
    "access_token": "{access-token-value}",
    "refresh_token": "{refresh-token-value}"
  }
```

An example using curl:

```sh
  curl --request POST '{csp-host}/csp/gateway/am/api/auth/api-tokens/authorize'  \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'refresh_token={api-token-from-CSP}'
```

Take a note of the  *`{access-token-value}`*. This is what you will use in a header for all subsequent API calls.

```json
  Authentication : Bearer {access-token-value}
```

##### To obtain an Access Token by using a CSP OAuth application

Obtain the Access Token by using the CSP oAuth credentials.

```json
  POST https://{csp-url}/csp/gateway/am/api/auth/authorize
```

```json
  Headers:        Content-type: application/x-www-form-urlencoded
  Authorization:  Basic
  Username:       {oAuth_Application_ID}
  Password:       {oAuth_Application_secret}
  Body:           grant_type : client_credentials
```

Response: 200 OK

```json
{
  "id_token": null,
  "token_type": "bearer",
  "expires_in": 1799,
  "scope": "scope.....{snippet}",
    "access_token": "{access-token-value}",
    "refresh_token": "{refresh-token-value}"
}
```

Take a note of the *`{access-token-value}`*. This is what you will use in a header for all subsequent API calls.

```json
Authentication : Bearer {access-token-value}
```

<swagger-ui src="horizon-cloud-nextgen-api-doc-public.yaml"/>

<!-- [OAD(./docs/horizon-cloud-nextgen/horizon-cloud-nextgen-api-doc-public.yaml)] -->
