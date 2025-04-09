# %% [markdown]
# Logging with handlers can be a bit tricky.
# When adding a StreamHandler it works fine the first time the block is
# run, but running it twice will print the log message twice.

# %% Logging with logging module
import logging
import sys

print("Run more than once to see duplicates in the output.")


LOGFORMAT = "%(asctime)s|%(levelname)-8s| %(name)s:%(lineno)-4d| %(message)s"  # default logformat
DATEFMT_STREAM = "%H:%M:%S"  # default dateformat for console logger

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(logging.Formatter(fmt=LOGFORMAT, datefmt=DATEFMT_STREAM))
logger.addHandler(handler)


logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")


# %% [markdown]
# Lets restart the interactive window

# %% Logging with hhnk-research-tools
import hhnk_research_tools as hrt

logger = hrt.logging.get_logger(__name__, level="INFO")

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")


# %%
