# Architecture

## Services
- **Web dashboard**: channel overview, request intake, production review, approvals and analytics.
- **API**: authenticated control plane; validates requests and owns business rules.
- **Worker**: durable media and analytics jobs; long-running work must not run in HTTP requests.
- **n8n**: orchestration, schedules, retries and notifications. It is not the source of truth.
- **Media engine**: FFmpeg-based audio/video rendering in isolated worker processes.
- **PostgreSQL**: projects, jobs, channel settings, rights records and audit events.
- **Redis**: queue transport and short-lived coordination.
- **Object storage**: source and generated media with retention policies.

## Core production flow
Request -> rights review -> analysis/plan -> render -> automated QC -> private YouTube upload -> approval -> scheduled publication -> analytics feedback.

## Security requirements before production
1. Implement OAuth authorization-code flow with state, PKCE where supported, strict redirect URI validation and one-time state consumption.
2. Encrypt refresh/access tokens at rest using a managed key; never log tokens.
3. Authenticate dashboard/API users and enforce per-channel authorization.
4. Sign n8n webhooks and validate timestamp/replay windows.
5. Make uploads and publishing idempotent; record YouTube video IDs and job state.
6. Require an auditable approval record before changing privacy to public or scheduling publication.
7. Isolate FFmpeg and downloaded media; enforce file size, duration and codec limits.
8. Add rate limits, backups, structured logs, monitoring and deletion/retention controls.

## Rights and monetization
Each source track needs a rights record covering owner, source, license evidence, commercial-use permission, derivative/remix permission and attribution. A transform such as slowing or adding reverb does not itself grant copyright permission. Claim detection is not a substitute for a license.
