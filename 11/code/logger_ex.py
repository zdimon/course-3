import logging
from logger_import import sum
import logging.config

logging.basicConfig(level=logging.DEBUG)



logging.config.dictConfig({
    'version': 1,              
    'disable_existing_loggers': True,  

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',    
            'class':'logging.StreamHandler',
        },  
        'file': {
            'level':'INFO',    
            'class':'logging.FileHandler',
            'filename': 'root.log',
        }, 
    },
    'loggers': {
        '': {                  
            'handlers': ['file'],        
            'level': 'INFO',  
            'propagate': True  
        }
    }
})

logger = logging.getLogger(__name__)

logger.info('Start reading database')
# read database here

records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here

logger.info('Finish updating records')


try:
    open('/path/to/does/not/exist', 'rb')
except Exception, e:
    logger.error('Failed to open file', exc_info=True)



sum(2,0)






