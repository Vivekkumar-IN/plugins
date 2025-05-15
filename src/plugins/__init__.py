import logging as _logging

_logger = _logging.getLogger(__name__)

def setup(*args, **kwds):
    _logger.error("Succesfully loaded plugins")