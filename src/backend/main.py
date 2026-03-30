from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel

app = FastAPI(title="Incident Horizon API", version="0.1.0")


class IncidentIn(BaseModel):
    title: str
    severity: str


incidents: list[dict] = []
connections: list[WebSocket] = []


@app.get("/incidents")
def list_incidents() -> list[dict]:
    return incidents


@app.post("/incidents")
def create_incident(payload: IncidentIn) -> dict:
    incident = {"id": len(incidents) + 1, **payload.model_dump(), "status": "open"}
    incidents.append(incident)
    return incident


@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket) -> None:
    await ws.accept()
    connections.append(ws)
    try:
        while True:
            message = await ws.receive_text()
            for conn in list(connections):
                await conn.send_text(message)
    except WebSocketDisconnect:
        connections.remove(ws)
