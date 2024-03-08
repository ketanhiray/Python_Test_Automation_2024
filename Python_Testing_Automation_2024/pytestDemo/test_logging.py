import logging

def test_logging():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)

    logger.debug("This is debug statement")
    logger.info("this is information statement ")
    logger.warning("This is warning")
    logger.error("this is error stat.")
    logger.critical("somthing is critical")