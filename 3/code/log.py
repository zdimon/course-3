import logging
import requests

FORMAT = '%(asctime)-15s %(name)s  %(message)s'

#filename="sample.log"

logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)



req = requests.get('https://google.com')


logger.info('Info problem: %s', 'connection reset')
logger.warning('Warning problem: %s', 'connection reset')
logger.error('Error problem: %s', 'connection reset')
logger.critical('Critical problem: %s', 'connection reset')

