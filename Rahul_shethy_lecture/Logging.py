import logging

def test_loggerDemo():
        logger=logging.getLogger(__name__)
        # filehandler=logging.FileHandler('logfile.log')
        # formatter=logging.Formatter("%(asctime)s :%(lavelname)s :%(name)s :%(message)s")
        # filehandler.setFormatter(formatter)
        # logger.addHandler(filehandler)

        #logger.setLevel("Logging Info")
        logger.debug("A debug statement is executed")
        logger.info("Information statement is executed")
        logger.warning("Something went is wrong in file")
        logger.error("Majaor issue in test case")
        logger.critical("Critical issue")