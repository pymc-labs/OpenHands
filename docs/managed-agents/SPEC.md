# Managed Agents Layer — Spec

A Claude-Managed-Agents-compatible resource model and REST API implemented on top of OpenHands' existing runtime (EventStream, AgentController, Runtime, ConversationManager).

This document defines the target shape. Scaffold files under `openhands/managed_agents/` hold the skeleton; each section below corresponds to one or more of those modules.

## Goals

- Offer an API surface compatible in shape with Claude Managed Agents (`/v1/agents`, `/v1/environments`, `/v1/sessions`, `/v1/sessions/{id}/events`, `/v1/vaults`, `/v1/skills`, `/v1/files`).
- Reuse OpenHands runtime unchanged: EventStream stays the source of truth, AgentController keeps the loop, Runtime keeps sandbox execution.
- Keep everything org-scoped, API-key gated, rate-limited.
- Add nothing that breaks the existing OpenHands UI / server path.

## Non-goals

- Drop-in wire compatibility with Anthropic's beta headers. Shape-only.
- Claude-only model support. Model selection stays pluggable via LiteLLM.

## Resource model

### Organizations
- `organizations` + `memberships` + `api_keys`. All resources below are org-scoped.
- API-key auth via `Authorization: Bearer <key>` on every `/v1/*` call.

### Agents
- Versioned. Row: `{id, org_id, name, model, system_prompt, tools, mcp_servers, skills, version, created_at}`.
- `POST /v1/agents`, `POST /v1/agents/{id}/versions`, `GET`, `LIST`, `DELETE`.
- Resolver composes a concrete `Agent` instance at session start from the stored config; no more selection-by-class-name.

### Environments
- Row: `{id, org_id, base_image, packages[], network_rules, mounted_files[]}`.
- Builder materializes → cached Docker image / sandbox template. One-to-one with OpenHands Runtime config.

### Sessions
- Row: `{id, org_id, agent_id, agent_version, environment_id, status, vault_ids[], created_at, archived_at}`.
- Status: `idle | running | rescheduling | terminated`. Maps from `AgentState`.
- `POST/GET/LIST/archive/DELETE`. `archive` blocks new events, preserves history.
- Backed by an OpenHands `Session` (EventStream + AgentController + Runtime).

### Events
- Append-only log. Projected from EventStream Actions/Observations.
- User events: `user.message`, `user.interrupt`, `user.tool_confirmation`.
- `POST /v1/sessions/{id}/events` (typed), `GET /v1/sessions/{id}/events` (replay), `GET …/events/stream` (SSE).

### Vaults
- Per-org OAuth credential store with automatic refresh.
- Referenced by `vault_ids` at session creation.
- Credentials injected into MCP server env at sandbox boot.

### Skills
- Versioned resource with `agent_skills` join.
- Loaded into the agent's prompt/tool set at session start.

### Files
- Independent resource, not tied to session lifecycle.
- Referenced by environment `mounted_files`.

### Outcomes (research preview tier)
- Typed session result schema declared on the agent, validated at session end.

### Memory (research preview tier)
- `memories` table + retrieval hook + writeback tool. Wraps existing `openhands.memory`.

### Child sessions / multi-agent (research preview tier)
- Child session resource; parent delegates via a `task`-style tool.

## Runtime alignment

### EventStream adapter (`runtime/eventstream_adapter.py`)
- `user.message` → `MessageAction`.
- `user.interrupt` → agent state transition to stopped.
- `user.tool_confirmation` → unblocks a gated Action (see confirmation gate).
- Outbound: Actions/Observations → MA event envelopes.

### Confirmation gate (`runtime/confirmation_gate.py`)
- Before executing a flagged Action, the controller awaits a matching confirmation event. Reuses OpenHands' existing confirmation mode.

### Vault injection (`runtime/vault_injection.py`)
- At sandbox boot, resolve `vault_ids` → credentials → env vars on MCP servers.

## Server layer

### `server/v1_router.py`
- FastAPI router mounted at `/v1`, gated by `auth.require_api_key`.
- All handlers currently raise `501`. Each landing PR flips one group live.

### `server/auth.py`
- Bearer key lookup, org resolution, stored as request-scoped state.

### `server/rate_limit.py`
- Redis sliding-window. Two buckets per org: creates, reads. Limits mirror MA's published ones.

## Implementation roadmap

Each bullet below is a follow-up PR after this scaffold merges.

1. **DB layer** — migrations + Pydantic/ORM models for every table above. Keep isolated from existing `openhands.storage`.
2. **Orgs + API keys + auth** — wire `require_api_key`, seed bootstrap, `POST /v1/organizations`.
3. **Agents CRUD + versioning** — resolver that composes `Agent` from a row.
4. **Environments CRUD + builder** — Docker image cache keyed on config hash.
5. **Sessions + EventStream bridge** — `POST /v1/sessions` spins up OpenHands `Session`; status mirrors `AgentState`.
6. **Events API + SSE** — implement event adapter + replay + stream.
7. **Steer / interrupt / confirmation** — schema alignment and confirmation gate wiring.
8. **Vaults + injection.**
9. **Skills registry + per-agent join.**
10. **Files service.**
11. **Rate limits.**
12. **Outcomes + memory + child sessions** (research-preview tier).

## Out of scope for scaffold PR

- Any DB migrations.
- Any router mounted into the live FastAPI app.
- Any behavior change to existing OpenHands endpoints.

## Test strategy

- Unit tests per resource module as each lands.
- Integration: spin up an OpenHands `Session` via the MA REST path and replay a canned event log end-to-end.
- Contract: schema-level tests that MA-style event envelopes round-trip through the EventStream adapter.
