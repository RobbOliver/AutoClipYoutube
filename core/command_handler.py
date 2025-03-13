from commands import clip, clip2
from config import COMMANDS_TRIGGER


def handle_command(user, message):
    """
    Processa o comando detectado e chama a função correspondente.

    Args:
        user (str): Nome do usuário que enviou o comando.
        message (str): Mensagem enviada.

    Returns:
        None
    """
    command = message.strip().lower()

    commands_options = {
        "!clip": clip.run,
        "!clip2": clip2.run
    }

    # Verifica se a mensagem é um comando conhecido
    if command in commands_options:
        if user in COMMANDS_TRIGGER or COMMANDS_TRIGGER[0] == "ALL":
            commands_options[command](user)
            print(f"🎯🎥 Clip solicitado por {user}.")

    return None
