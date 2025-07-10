from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

@app.get("/captura")
async def captura_info(request: Request):
    info = {
        "ip": request.client.host,
        "user_agent": request.headers.get("user-agent"),
        "headers": dict(request.headers),
        "query_params": dict(request.query_params),
        "url": str(request.url),
        "method": request.method,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    print("Nuevo acceso:", info)  # Esto aparecerá en los logs de Render
    return {"status": "ok", "message": "Acceso registrado"}
