class ChannelIDNotFoundError(Exception):
    """Exceção lançada quando o Channel ID não puder ser encontrado a partir do handle."""

    def __init__(self, message="Error to get ChannelID."):
        super().__init__(message)


class VideoIDNotFoundError(Exception):
    """Exceção lançada quando o Video ID não puder ser encontrado a partir do Channel ID."""

    def __init__(self, message="Error to get VideoID."):
        super().__init__(message)


class ChatIDNotFoundError(Exception):
    """Exceção lançada quando o Chat ID não puder ser encontrado a partir do Video ID."""

    def __init__(self, message="Error to get ChatID."):
        super().__init__(message)


class YTDLNotFoundError(Exception):
    """Exceção lançada quando o yt-dlp não puder ser encontrado."""

    def __init__(self, message="yt-dlp not found."):
        super().__init__(message)

class FFmpegNotFoundError(Exception):
    """Exceção lançada quando o ffmpeg não puder ser encontrado."""

    def __init__(self, message="ffmpeg not found."):
        super().__init__(message)