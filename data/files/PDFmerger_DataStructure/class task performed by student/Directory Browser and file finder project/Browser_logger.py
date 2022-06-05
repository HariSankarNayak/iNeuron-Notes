import logging as lg
lg.basicConfig(filename='Browser_logs.log',level=lg.DEBUG,
               format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

def writelogs(username,msglevel,msg):
    logger1=lg.getLogger(username)
    if msglevel=='DEBUG' or msglevel=='debug':
        logger1.debug(msg)
    if msglevel=='INFO' or msglevel=='info':
        logger1.info(msg)
    if msglevel=='WARNING' or msglevel=='warning':
        logger1.warning(msg)
    if msglevel=='ERROR' or msglevel=='error':
        logger1.error(msg)
    if msglevel=='CRITICAL' or msglevel=='critical':
        logger1.critical(msg)
    if msglevel=='EXCEPTION' or msglevel=='exception':
        logger1.exception(msg)

#writelogs('Testing','debug','debug message')