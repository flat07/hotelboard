from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    exception_handler,
)

from common.exceptions import (
    DomainError,
)


def custom_exception_handler(
    exc,
    context,
):
    response = exception_handler(
        exc,
        context,
    )

    if response is not None:
        return response

    if isinstance(
        exc,
        DomainError,
    ):
        return Response(
            {
                "detail": exc.message,
            },
            status=exc.status_code,
        )

    return Response(
        {
            "detail": ("Internal server error."),
        },
        status=500,
    )
