---
layout: page
title: Getting Started with Horizon Cloud Service
#permalink: /apis/horizon-cloud-nextgen/
hide:
  #- navigation
  - toc
---

![](assets/logos/horizon-cloud-logo.png){ align=right }

This is a API documentation for the VMware Horizon Cloud Service - next-gen

*Horizon Cloud is a modern cloud-first, multi-cloud Desktop as a Service (DaaS) deployment with Thin Edge Infrastructure. The service provides you with a global view of your desktops and applications spanning across on-premises and cloud environments. Regardless of the location of your desktop and application deployments, Horizon Cloud enables you to consistently manage and monitor them.*

## Onboarding Customer to Data Center (HDC)
Once you receive your CSP invitation link in the email, please redeem it by clicking on the url. If you have not received an email, please reach out to VMWare.
  + Then do CSP Login
  + You have an option to create to use an existing CSP organization or create a new one to onboard to Horizon Cloud Services.
  + As an organization owner, need to go to "Identity & Access Management" and edit the existing user to add the following role:
    + **Administrator**  
  
  Customer may add more users and assign the role above. Administrator role is required to access entire UI and API. All the APIs need a bearer token generated from an API token. Follow these steps to get your API token.
  + Go to your account and API Tokens tab.
  + Click on Generate a New API TOKEN link. Provide a name for the API token and keep the defaults.
  + Save the API token information and keep it handy.

## General API Notes

### Authentication
*Please take a note of above two steps The same authentication scheme ("Authorization: Bearer") is required for all API calls*

### Obtain a CSP Access Token

Login to CSP Portal and obtain the following:
- CSP Org ID
  Take the 'Long Organization ID' from the 'View Organization' page in CSP
- EITHER CSP oAuth Application ID and oAuth Application secret 
  These can be found when originally creating the OAuth App within your Organization page, or can be regenerated from the same area. Note: OAuth App should have the Horizon Cloud Service listed as a Service Role
- OR CSP API Token
  See the previous section for details about create API Tokens
  All API calls require authentication using an Access Token.
  Choose one of the following methods to obtain an Access Token

#### 1a. To obtain an Access Token by using a CSP API Token
One authentication scheme is to use an "Access Token", which is obtained by making an API call that takes  your  API Token as input, and returns an Access Token. This Access Token is then supplied as a bearer token in an "Authentication" header with every API request. All the following steps will assume this authentication header, it will not be explicitly mentioned each time.
Note: `{{csp-url}}` value will typically be [https://connect.omnissa.com](https://connect.omnissa.com)
```
POST https://{{csp-url}}/csp/gateway/am/api/auth/api-tokens/authorize
```
```
Headers:      Content-Type : application/x-www-form-urlencoded
Request Body: refresh_token : {{YOUR-API-TOKEN-FROM-GETTING-STARTED-STEP-2}}
Response:
{
  "id_token": {{id-token-value}},
  "token_type": "bearer",
  "expires_in": 1799,
  "scope": "scope.....{snippet}",
  "access_token": "{{access-token-value}}",
  "refresh_token": "{{refresh-token-value}}"
}
```
An example using curl:
```
% curl --request POST '{csp-host}/csp/gateway/am/api/auth/api-tokens/authorize'  \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'refresh_token={api-token-from-CSP}'
```

Take a note of the  *{{access-token-value}}*. This is what you will use in a header for all subsequent API calls.
```
Authentication : Bearer {{access-token-value}}
```

#### 1b. To obtain an Access Token by using a CSP OAuth application
Obtain the Titan access token by using the CSP oAuth credentials.
```
POST https://{{csp-url}}/csp/gateway/am/api/auth/authorize
```
```
Headers:        Content-type: application/x-www-form-urlencoded
Authorization : Basic
Username =      {{oAuth Application ID}}
Password =      {{oAuth Application secret}}
Request Body:   grant_type : client_credentials

Response: 200 OK
{
  "id_token": null,
  "token_type": "bearer",
  "expires_in": 1799,
  "scope": "scope.....{snippet}",
    "access_token": "{{access-token-value}}",
    "refresh_token": "{{refresh-token-value}}"
    }
```
Take a note of the  *{{access-token-value}}*. This is what you will use in a header for all subsequent API calls.
```
Authentication : Bearer {{access-token-value}}
```

<swagger-ui src="horizon-cloud-nextgen-api-doc-public.yaml"/>
