import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logging_config import logger


class RequestLoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):
        request_id = str(uuid.uuid4())

        start_time = time.time()

        response = await call_next(request)

        duration = (
            time.time() - start_time
        ) * 1000

        logger.info(
            f"request_id={request_id} "
            f"method={request.method} "
            f"path={request.url.path} "
            f"status={response.status_code} "
            f"duration_ms={duration:.2f}"
        )

        return response