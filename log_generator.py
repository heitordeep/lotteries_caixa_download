import logging


class RegisterLogs:
    def __init__(self):
        logging.basicConfig(
            format='%(levelname)s: %(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %I:%M:%S',
            filename=f'log/log_app.log',
            level=logging.DEBUG,
        )

    def debug_register(self, text):
        return logging.debug(text)

    def error_register(self, text):
        return logging.error(text)

    def warning_register(self, text):
        return logging.warning(text)

    def info_register(self, text):
        return logging.info(text)
