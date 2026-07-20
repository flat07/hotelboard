from common.exceptions import (
    DomainError,
)


class RoomNotFoundError(
    DomainError,
):
    status_code = 404

    default_message = "Invalid room."
