import uvicorn
from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from pydantic import BaseModel

from tdd_api import r
from tdd_api.core.dependencies import Logger

app = FastAPI(title="TDD API")
app.include_router(r.router)

FastAPIInstrumentor.instrument_app(app)


class MessageResponse(BaseModel):
    message: str


@app.get("/")
async def root(log: Logger) -> list[dict[str, str]]:
    log.error("This is from kink logger!")
    return [{"message": "Hello, world!"}]


def run() -> None:
    uvicorn.run(app, reload=True, port=8888, log_config=None)


if __name__ == "__main__":
    run()
