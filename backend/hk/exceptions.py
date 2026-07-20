from common.exceptions import (
    DomainError,
)


class InvalidHousekeepingServiceError(
    DomainError,
):
    status_code = 400

    default_message = "Invalid housekeeping service."
