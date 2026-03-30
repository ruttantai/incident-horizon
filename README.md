# Incident Horizon

Incident Horizon is a real-time incident command center for operations teams. It captures incident events, broadcasts updates over WebSockets, and keeps a timeline of decisions for postmortems.

## Current scope
- Create incident rooms
- Broadcast live updates to connected clients
- Store timeline entries for after-action review

## Tech stack
- Frontend: Vue 3
- Backend: FastAPI + WebSockets
- Streaming: Redis Streams (planned integration)
- Search: Elasticsearch (planned integration)

## Repository layout
- docs/: incident model and architecture notes
- src/frontend/: Vue client
- src/backend/: API + WebSocket service
- tests/: API, websocket, and load checks
- infra/: deployment assets and service topology
- scripts/: local helper scripts

## Quick start
1. Run API server from src/backend.
2. Run frontend app from src/frontend.
3. Open two browser tabs and watch live room updates.

## Roadmap
1. Add Redis-backed event stream.
2. Add Elasticsearch indexing for incident search.
3. Add on-call timeline annotations and export.
4. Add SLO dashboard integration.
