# Kentik API and Schema Findings

> [!WARNING]
> This report contains lab resource IDs and API request IDs. Keep this branch
> local. Do not merge it into `main` or share it beyond the API team without
> removing those details.

Tracker review: 2026-10-28. The latest live evidence is dated 2026-10-27.
This file is the single current tracker for API findings, progress, and next
actions. Linked reports hold supporting evidence.

## Read-only Revalidation, 2026-10-27

The REST e2e suite made no writes: 89 passed, 16 expected xfails, and 139
mutating cases were skipped. The gRPC suite also made no writes: 87 passed,
16 expected xfails, and 139 mutating cases were skipped.

The dedicated deadline test reproduced the deadline error on all six services.
The read-only `ktbgp.RouteService.List` call returned HTTP 501.

Four missing-resource GETs returned these results:

| Resource | Result |
| --- | --- |
| AS group | HTTP 400 `INVALID_ARGUMENT` |
| Site market | HTTP 400 `INVALID_ARGUMENT` |
| FlowTag | HTTP 404 `NOT_FOUND` |
| Custom application | HTTP 200 with an empty object |

The rate-limit probe recorded `60, 60;w=60` on each response. Two device
requests and one gRPC device request used one counter. Site and site-market
requests started separate counters. The probe did not approach the limit.

The local schema audit used `api-schema-public` commit
`8ec5847688b6ac76b76ceea1cba46f862725d758`. It still found three services
with no REST paths, and private or protected services with published paths.
The audit did not test authorization.

The read-only alert-list probe sent seven body variants. Every call returned
HTTP 200. It returned 160 alerts for `activeAt` alone and for `startedAt`
alone. It returned zero alerts for the other five bodies.

Local logs and probe code remain in the ignored
`local-evidence/revalidation-2026-10-27/` folder. Git does not track those files.

## Findings And Status

File separate tickets for unrelated behavior. Recheck older findings before
filing them as current defects.

| # | Finding | Status | Next action | Evidence |
| --- | --- | --- | --- | --- |
| 1 | Merge body and URL path fields for `UpdateASGroup` and `UpdateSiteMarket` | Confirmed on 2026-10-27 | File one ticket for this request shape. Keep the shared internal cause unconfirmed. | [Body-merge evidence](upstream-rest-update-body-merge.md) |
| 2 | `CreateFlowTag` returns HTTP 500 | Confirmed over REST on 2026-10-27 | File separately. Recheck gRPC create with a disposable resource. | [Historical draft](archive/upstream-jira-drafts.md) |
| 3 | V5 batch success status | HTTP 200 observed on 2026-10-27; contract unresolved | Ask which status is correct and whether the response must include a batch ID. | Local evidence only; no request ID was captured. |
| 4 | AutoAck `Replace` returns `SyntaxError` | Separate issue observed on 2026-10-27 | Ask the API team to inspect request `dbgge7gzked0089cpq20`. Do not classify this as a body-merge failure. | [Historical draft](archive/upstream-jira-drafts.md) |
| 5 | gRPC calls with deadlines return `RangeError` | Reproduced on all six services on 2026-10-27 | Ask the API team to confirm the server-side cause in logs. | [Historical draft](archive/upstream-jira-drafts.md) |
| 6 | Alert list requires `startedAt` | Not reproduced on 2026-10-27 | No action unless it recurs. Keep the old report as history. | [Archived report](archive/upstream-alert-list-requirements.html) |
| 7 | Filtered `CreateSavedFilter` returns HTTP 500 | Prior result; not rechecked | Recheck only with an approved disposable resource and cleanup. | [Historical draft](archive/upstream-jira-drafts.md) |
| 8 | Missing custom application returns HTTP 200 with an empty object | Confirmed by read-only GET on 2026-10-27 | Ask whether this response is intended. | [Historical draft](archive/upstream-jira-drafts.md) |
| 9 | Missing AS group or site market returns HTTP 400 | Confirmed by read-only GETs on 2026-10-27 | Ask whether `INVALID_ARGUMENT` is the intended missing-resource response. | [Historical draft](archive/upstream-jira-drafts.md) |
| 10 | Missing IDs return HTTP 500 in alerting, audit, and vault | Reproduced by read-only REST and gRPC suites on 2026-10-27 | Ask the API team to return a missing-resource response instead. | [Historical draft](archive/upstream-jira-drafts.md) |
| 11 | Malformed IDs return HTTP 500 | Reproduced by read-only REST and gRPC suites on 2026-10-27 | Ask the API team to return HTTP 400 `INVALID_ARGUMENT`. | [Historical draft](archive/upstream-jira-drafts.md) |
| 12 | Published kagent, kmeta, and ktbgp operations return HTTP 501 | Reproduced for kagent and kmeta; ktbgp List also returned 501 | Ask which published operations the API supports. | [Historical draft](archive/upstream-jira-drafts.md), [Alert-list evidence](archive/upstream-alert-list-requirements.html) |
| 13 | `kptr` and `deviceconf` lack HTTP bindings | Confirmed in schema commit `8ec5847688b6ac76b76ceea1cba46f862725d758` | Ask whether the 13 public RPCs will receive HTTP bindings. | [Schema audit](upstream-kptr-missing-http-annotations.html) |
| 14 | Visibility metadata conflicts with published REST paths | Confirmed in schema; authorization not tested | Ask what the visibility values mean and whether downstream tools must receive them. | [Visibility report](upstream-service-visibility-exposure.html) |
| 15 | Rate-limit documentation conflicts with observed headers | Header scope reconfirmed; documented limits remain unverified | Correct the documented scope. Verify concurrency, delay, and hourly limits. | [Rate-limit report](upstream-ratelimit-scope-undocumented.html) |
| 16 | `openapi-python-generator` requires formatter packages with `--formatter none` | Draft request; confirmed against version 2.1.2 | File the request with the generator maintainers. Add the issue link to the SDK dependency guide. | [Draft request](upstream-openapi-python-generator-optional-formatters.md) |

## Source Notes

This file is the only current status tracker. The detailed reports hold
evidence. Archived drafts preserve historical claims and do not set current
status.

The [body-merge Markdown report](upstream-rest-update-body-merge.md) contains
the request transcripts and follow-up evidence. The archived HTML snapshots and
draft issue list remain in [archive/](archive/).

Reusable investigation scripts live under [scripts/](scripts/) and their
purpose and side effects are listed in [README.md](README.md). Local account
captures and one-off experiments stay in the ignored `local-evidence/` folder.

## Confirmed Request IDs

| Finding | Request ID |
| --- | --- |
| AS group update, HTTP 400 | `dbgenbntkfgg0a1txqtg` |
| Site market update, HTTP 500 | `dbgepd9tkfgg0f9838cg` |
| FlowTag create, HTTP 500 | `dbgesketkfgg04rgdw1g` |
| AutoAck Replace, HTTP 500 | `dbgge7gzked0089cpq20` |
| Earlier AutoAck control, HTTP 400 | `dbck78dzked00d9jjmr0` |
| Missing AS group, HTTP 400 | `dbgk2dhtkfgg06g8sqy0` |
| Missing site market, HTTP 400 | `dbgk2dhtkfgg0bsxm3jg` |
| Missing FlowTag, HTTP 404 | `dbgk2dhtkfgg0bsxm3k0` |
| V5 batch, HTTP 200 | No request ID was captured |
