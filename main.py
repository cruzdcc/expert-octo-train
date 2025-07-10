import logging
from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()
logger = logging.getLogger("uvicorn.access")

@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "API funcionando. Usa /captura?tag=ID para pruebas con Tap Tag."
    }

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

    logger.info(f"Nuevo acceso: {info}")
    return info

