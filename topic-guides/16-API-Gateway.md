# Section 16: API Gateway

## The idea

API Gateway is the **front desk of a busy office building**. Nobody wanders straight to your engineers' desks (your Lambda functions, your backends). Everyone checks in at the front desk first, where the receptionist **routes** them to the right floor, **checks their ID** (authentication), **turns away crowds** when the lobby is full (throttling), and **writes every visit in the logbook** (logging) — all *before* your code runs a single line.

That's API Gateway: a fully managed service that sits in front of your backend and handles routing, auth, rate limiting, caching, and monitoring.

Burn in the canonical serverless chain — the exam's favorite architecture:

```
Client --> CloudFront --> API Gateway --> Lambda --> DynamoDB
```

The reflex: **"no servers to manage, pay per request"** → this chain. When a question describes a REST API with zero server management, this is the answer skeleton.

## Three API types

| Type | Personality | Features | Trigger phrase |
|---|---|---|---|
| **REST API** | Full-featured flagship | **API keys, usage plans, caching, WAF, request validation** | Needs any of those features |
| **HTTP API** | Minimalist, **~70% cheaper** | Simple proxy to Lambda/HTTP, built-in **JWT** auth, low latency | **"Lowest cost"** simple Lambda proxy |
| **WebSocket API** | **Persistent two-way** connection | Server can push to clients | **"Real-time chat"**, "live push", live dashboards |

THE trap: usage plans, API keys, and caching are **REST API only**. If the question needs them, HTTP API is a distractor no matter how cheap it is.

## Endpoint types (where does it live?)

| Endpoint | For | Note |
|---|---|---|
| **Edge-Optimized** | **Globally distributed clients** | Routed through CloudFront's edge network automatically (default) |
| **Regional** | Clients in the **same region** | Or when you want to bolt on **your own CloudFront** distribution |
| **Private** | **VPC-only** access | Reached via an **Interface VPC Endpoint** — never touches the internet |

## Authorization choices

Match the method to the API type. HTTP APIs can validate JWTs from compatible third-party issuers directly; third-party identity does not automatically require custom Lambda code.

| Authorizer | Use when the caller is... | Mechanism |
|---|---|---|
| **IAM / SigV4** | **AWS-native**: internal services, EC2 roles, IAM users | Requests signed with AWS credentials (Signature Version 4) |
| **Cognito User Pool authorizer** | **App users who sign in** (mobile/web app accounts) | Cognito issues a **JWT** (JSON Web Token); gateway validates it, zero custom code |
| **Lambda Authorizer** | **Custom logic**: third-party identity provider, legacy/**bespoke tokens**, weird rules | Your Lambda inspects the token and returns an IAM policy |

Hook: **IAM = machines, Cognito = your users, Lambda Authorizer = anything weird.**

## Traffic control & performance

- **Default throttle: 10,000 requests/second in many Regions**, with lower defaults in some Regions; shared per account and Region. Exceed it and clients get **HTTP 429 Too Many Requests** — "clients receiving 429" → you're being throttled.
- **Usage Plans + API Keys** (REST only): best-effort per-customer quotas and rate tiers; API keys are not authentication or authorization. Trigger: **"SaaS company sells API access in Basic/Pro tiers"** → usage plans with API keys.
- **Caching**: gateway caches responses (**default TTL 300 seconds**), reducing backend load and latency. "Reduce calls hitting the backend for repeated requests" → enable API Gateway caching.

## Two mechanical facts (free points)

1. **Integration timeout depends on API type.** Regional and private REST APIs can request an increase beyond the default 29 seconds; this may require a throttle-quota reduction. HTTP APIs have a 30-second maximum. For jobs that should outlive a client connection, return **202 Accepted only after durably accepting work**, then use a queue or workflow with a job ID and status endpoint. Sources: [REST timeout increases](https://repost.aws/knowledge-center/api-gateway-timeout-limit), [HTTP API quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-quotas.html).

```
Client --> API GW --202--> (immediately)
              |
              +--> SQS --> Lambda/worker (takes 2 min, nobody's waiting)
```

2. **CORS (Cross-Origin Resource Sharing).** When **browser JavaScript on one domain** calls your API on another domain and gets blocked with cross-origin errors → **enable CORS** on API Gateway. Browser + cross-domain + JS error = CORS, every time.

## Question patterns

> *"Build a REST API with no servers to manage, pay only per request"* → **API Gateway + Lambda + DynamoDB** (the canonical serverless chain)
> *"SaaS company wants to offer customers different API request limits per pricing tier"* → **Usage Plans + API Keys** (REST API only — per-customer tiers)
> *"Mobile app users must sign in before calling the API"* → **Cognito User Pool authorizer** (app users = Cognito JWTs)
> *"Company has an existing custom/third-party token system for API auth"* → **check native JWT support first**, then Lambda Authorizer for custom logic
> *"Cheapest way to expose a simple Lambda function over HTTP with JWT auth"* → **HTTP API** (~70% cheaper, minimal features)
> *"Push live updates to a real-time dashboard / chat application"* → **WebSocket API** (persistent two-way connection)
> *"API must be accessible only from within the VPC, never the internet"* → **Private endpoint + Interface VPC Endpoint**
> *"Backend process takes 2 minutes; API Gateway requests keep timing out — fix it"* → **Go async: return 202, queue to SQS/Step Functions** (check API type and quota; async avoids keeping the connection open)
> *"Browser JavaScript from another domain gets blocked calling the API"* → **Enable CORS** on API Gateway
> *"Clients suddenly receive HTTP 429 errors"* → **Throttling** — raise the limit or add caching/usage plans

## Pocket card

| Keyword | Answer |
|---|---|
| Serverless REST API | API GW + Lambda + DynamoDB |
| API keys / usage plans / caching / WAF | REST API (only) |
| Lowest cost, simple proxy, JWT | HTTP API |
| Real-time / chat / live push | WebSocket API |
| Global clients | Edge-Optimized endpoint |
| VPC-only API | Private endpoint (Interface Endpoint) |
| AWS-service callers | IAM / SigV4 auth |
| App users sign in | Cognito User Pool authorizer |
| Custom/third-party tokens | Lambda Authorizer |
| 429 errors | Check account, stage, route, and usage-plan throttles; regional defaults vary |
| Long-running backend | Check API timeout; consider durable async acceptance + job status |
| Cache TTL default | 300 seconds |
| Browser cross-domain error | Enable CORS |

You just saw the fix for slow backends is "drop the work into a queue and walk away" — that queue, and the whole messaging toolbox around it, is the next section.

Targeted review: 2026-10-10. See [account quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html) and [HTTP JWT authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html).
