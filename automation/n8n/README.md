# n8n workflow blueprints

Import the JSON files from n8n (Workflows -> Import from File). Configure credentials in n8n's credential store; never put API keys in exported workflow JSON.

- 01: accepts a music request and requires explicit rights confirmation.
- 02: hands validated work to the application API for durable background processing.
- 03: requires an explicit human approval before scheduling public publication.

Required application endpoints (to be implemented before activation):
- POST /api/v1/requests
- POST /api/v1/jobs
- POST /api/v1/publications/approve-and-schedule

All workflows are inactive templates. Configure signed webhooks, replay protection, API_BASE_URL and N8N_WEBHOOK_SECRET. Set the instance timezone to Asia/Dhaka. These files are not a complete deployment by themselves.
