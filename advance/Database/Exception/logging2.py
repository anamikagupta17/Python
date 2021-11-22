from logging import*
log_format1='{lineno} *** {asctime} ** {message}'  # if we use style='{'
log_format='%(asctime)s --%(message)s'

basicConfig(filename='log.txt',level=DEBUG,filemode='w',format=log_format) # by defult append mode
basicConfig(filename='log2.txt',level=DEBUG,filemode='w',style="{",format=log_format1) # by defult append mode
logger=getLogger("anamika")
logger.info("this is info")
warning("this is warning")
error("this is error")
critical("this is critical")
debug("this is debug")