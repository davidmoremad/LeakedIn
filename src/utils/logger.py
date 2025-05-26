import logging

class LoggerFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[94m',  # Blue
        'INFO': '\033[92m',   # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',  # Red
        'CRITICAL': '\033[41;1m',  # Red background
        'RESET': '\033[0m'    # Reset to default
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        log_icon = getattr(record, 'log_icons', '')  # Safely get log_icons
        message = super().format(record)
        return f"{log_color}{log_icon}{message}{self.COLORS['RESET']}"
    
class Logger:
    def __init__(self, level=logging.DEBUG, log_icons=" "):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

        # Create console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # Create formatter and add it to the handler
        # Debug: [>] HH:MM:SS - Message - Debug message
        # Info: [i] HH:MM:SS - Message
        # Warning: [!] HH:MM:SS - Message
        # Error: [X] HH:MM:SS - Message
        # Critical: [X] HH:MM:SS - Message
        formatter = LoggerFormatter(f'%(asctime)s - %(message)s', datefmt='%H:%M:%S')
        ch.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(ch)

    def debug(self, message):
        self.logger.debug(message, extra={'log_icons': '[>] '})

    def info(self, message):
        self.logger.info(message, extra={'log_icons': '[i] '})

    def warning(self, message):
        self.logger.warning(message, extra={'log_icons': '[!] '})

    def error(self, message):
        self.logger.error(message, extra={'log_icons': '[X] '})

    def critical(self, message):
        self.logger.critical(message, extra={'log_icons': '[X] '})