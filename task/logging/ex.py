import logging
logging.basicConfig(level=logging.INFO,filename="log.log",filemode="w",
                    format="%(asctime)s - %(levelname)s -%(message)s",datefmt="%Y/%m/%d  %H:%M.%S")

logging.debug("debug")
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")

#logging variable value-----------------------
x=2
logging.info(f"the value of x is {x}")


name="hello word"
logging.critical(f"crotical error")

#logging expection---------------------
try:
    1/0

except ZeroDivisionError as e:
    logging.error("ZeroDivisionError")



