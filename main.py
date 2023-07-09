import logging
import logging.handlers

def send_syslog(ip_address):
    # Set up the logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.INFO)

    # Create a SysLogHandler
    handler = logging.handlers.SysLogHandler(address=(ip_address, 514))

    # Set the formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    # Send syslog messages
    logger.info('This is an informational message.')
    #logger.warning('This is a warning message.')
    #logger.error('This is an error message.')


send_syslog("192.168.0.105")
send_syslog("192.168.1.1")
send_syslog("192.168.1.2")
send_syslog("192.168.1.3")
send_syslog("192.168.1.4")
send_syslog("192.168.1.5")
send_syslog("192.168.1.6")
send_syslog("192.168.1.7")
send_syslog("192.168.1.100")
send_syslog("192.168.1.101")
send_syslog("192.168.1.102")
send_syslog("192.168.1.200")


