import logging


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

# logging.debug('This is a debug message')
# logging.info('This is a info message')
# logging.warning('This is a warning message')
# logging.error('This is a error message')
# logging.critical('This is a critical message')

# -----
# # Create handler with manual
# logger = logging.getLogger(__name__)

# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# # Set level and format

# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# # Set the properties

# logger.addHandler(stream_h)
# logger.addHandler(file_h)
# logger.warning('this is a warning')
# logger.error('this is a error')

# -----
# create log config with logging.conf

# logging.config.fileConfig('logging.conf') # or we can create dictconfig and use logging.config.dictConfig('dictlogging.conf')

# logger = logging.getLogger('simpleExample')
# logger.debug('this is a debug message')

# -----

# try:
#     a = [1,2,3]
#     val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True)    

# import traceback
# try:
#     a = [1,2,3]
#     val = a[4]
# except:
#     logging.error("The error is %s", traceback.format_exc())

# -----

# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # Roll over after 2KB and keep backup logs app.log.1, app.log.2, etc..
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info('Helloworld')
    
# It'll create multi log files because of 2KB memory limit

## Also create filehandler with timedrotate and observe passed time for log

# from logging.handlers import TimedRotatingFileHandler
# import time

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # Roll over after 2KB and keep backup logs app.log.1, app.log.2, etc..
# # s = second, m = minutes, h = hours, d = days, midnight, w0 = wednesday, etc....
# handler = TimedRotatingFileHandler('app.log', when='s', backupCount=5, interval=5,)
# logger.addHandler(handler)

# for _ in range(6):
#     logger.info('Helloworld')
#     time.sleep(5)
    
## It'll create multi log files after every 5 seconds

# python-json-logger
# https://github.com/madzak/python-json-logger
# pip install python-json-logger