# Incident Horizon

Incident Horizon is a real-time incident command center for engineering teams. It helps teams coordinate during outages with live updates, shared timelines, and post-incident records.

The goal is to show strong full stack engineering under reliability-focused requirements.

## Focus
- Full stack systems with real-time communication

## Stack
- Vue, Python, WebSockets, Redis Streams, Elasticsearch

## What I want this repo to demonstrate
- Realtime architecture choices and tradeoffs
- Stateful collaboration features across multiple users
- Operational thinking: observability, replay, and incident history

## Starter structure
- docs/: Incident lifecycle, architecture, and roadmap
- src/: Frontend and backend services
- tests/: Contract, integration, and load tests
- infra/: Service topology and deployment assets
- scripts/: Developer and ops helper scripts

## First build plan
1. Build incident room creation and live event feed.
2. Add timeline playback and decision log.
3. Integrate alert/event ingestion from external systems.
4. Add dashboards and alerting for system health.
