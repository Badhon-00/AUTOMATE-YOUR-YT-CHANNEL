# AUTOMATE-YOUR-YT-CHANNEL

A rights-aware AI-assisted music production and YouTube channel operations platform.

## Planned capabilities
- Learn a channel's existing music and visual identity from authorized channel data.
- Create production plans for licensed or user-owned audio.
- Produce slowed/reverb, lo-fi, instrumental and authorized mashup variants.
- Render original visualizers and thumbnails.
- Prepare metadata and upload privately through the official YouTube API.
- Require explicit approval before public publication.
- Analyze channel performance and recommend experiments.

## Quick start
1. Install Node.js 20.11+ and Docker.
2. Copy `.env.example` to `.env` and set local-only values.
3. Run `docker compose up -d`.
4. Run `npm install`.
5. Run `npm run dev`.

API health check: `GET http://localhost:4000/health`.

## Safety defaults
- Public publishing requires approval (`PUBLICATION_REQUIRE_APPROVAL=true`).
- Never commit OAuth tokens, API keys, encryption keys, or private channel data.
- Only process audio for which the operator has the necessary rights and permissions.
- Do not automate fake views, subscribers, comments, or other artificial engagement.

## Current implementation status
This is the initial foundation, not a production-ready complete service. OAuth state/PKCE, encrypted token storage, database migrations, durable job workers, YouTube upload, media rendering, and deployment hardening are subsequent milestones. Do not expose it publicly until those controls are implemented and tested.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
