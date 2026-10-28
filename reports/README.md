# Reports

This directory contains one current status tracker, supporting reports, and
reusable investigation scripts.

## Current status

Use [kentik-api-team-findings.md](kentik-api-team-findings.md) for the current
findings, progress, and next actions. Other reports hold evidence. They do not
maintain a second status list.

The [pre-PR audit](pre-pr-audit-2026-10-10/report.md) keeps its own validation
and deferred-risk ledgers because it tracks a separate SDK audit.

## Scripts

Run commands from the repository root unless a script says otherwise. Read the
script header before running it. Live probes need credentials and contact the
Kentik API. Do not run them against a production account.

| Folder | Contents | Effects |
| --- | --- | --- |
| [scripts/rest-body-merge/](scripts/rest-body-merge/) | `audit.py`, `live_probe.py`, `curl_repro.sh` | `audit.py` is offline. The live probes create test objects and attempt cleanup. Use a lab account. |
| [scripts/grpc-deadlines/](scripts/grpc-deadlines/) | `deadline_checks.sh`, `sdk_check.py`, `camelify_repro.js` | The checks call live read-only APIs. The local reproduction needs Node.js packages `@grpc/grpc-js`, `@grpc/proto-loader`, and `lodash`. |
| [scripts/missing-resource-errors/](scripts/missing-resource-errors/) | `curl_check.sh`, `sdk_check.py` | Live read-only GET requests. |
| [scripts/schema/](scripts/schema/) | `annotation_audit.py` | Reads the sibling `api-schema-public` checkout. |
| [scripts/v5/](scripts/v5/) | `live_probe.py` | Live read-only GET and query requests. It prints response shapes, not record contents. |

The scripts are tracked when they are reusable, do not contain credentials or
account captures, and state their side effects in their headers.

## Local evidence

The local `local-evidence/` folder is ignored by Git. Keep account-specific
captures, raw query results, generated output, and one-off experiments there.
It includes retired probes that are not safe or useful to run as maintained
scripts.

## Archive

`archive/` holds old report snapshots and draft tickets. Use them as historical
evidence. Use the current tracker for status.