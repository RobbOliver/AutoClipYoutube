class ChannelIDNotFoundError(Exception):
    """Exceção lançada quando o Channel ID não puder ser encontrado a partir do handle."""

    def __init__(self, message="Error to get ChannelID."):
        super().__init__(message)


class VideoIDNotFoundError(Exception):
    """Exceção lançada quando o Video ID não puder ser encontrado a partir do Channel ID."""

    def __init__(self, message="Error to get VideoID."):
        super().__init__(message)
