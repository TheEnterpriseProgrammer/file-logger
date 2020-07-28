import logging

def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='/temp/myapp.log',
                        filemode="w")
    # Create the logger
    logger = logging.getLogger("TEST-APP")
        #self._function_map = dict(debug = "write_debug")
    #fh = logging.FileHandler("test-log.log")
    #fh.setLevel(logging.DEBUG)
    #fh.format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s"
    #logging.getLogger('').addHandler(fh)

    logger.debug("Our first debug message")

if __name__ == '__main__':
    main()