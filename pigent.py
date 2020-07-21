#!/usr/bin/env python3

import sys
import os
import logging
import config
import web
import traceback

# Logging
LOG_LEVEL = logging.INFO
logging.basicConfig(
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S %z',
        level=LOG_LEVEL
)

if config.debug:
    logging.warning("==============================")
    logging.warning("WARNING: DEBUG MODE IS ENABLED")
    logging.warning("WARNING: SOME APIs(ex. sensors) WILL BE RESPOND AS DUMMY!!!")
    logging.warning("==============================")
    LOG_LEVEL = logging.DEBUG

logging.info("Starting Pigent...")

# Start web API
try:
    web.start(config)
except Exception as ex:
    logging.fatal("Exception threw:")
    print(traceback.format_exc())
    sys.exit(1)
