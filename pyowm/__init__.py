#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The PyOWM init file

**Author**: Claudio Sparpaglione, @csparpa <csparpa@gmail.com>

**Platform**: platform independent

"""

from pyowm import constants
from pyowm.utils import timeutils  # Convenience import


def OWM(API_key=None, version=constants.LATEST_OWM_API_VERSION,
        config_module=None):
    """
    A parametrized factory method returning a global OWM instance that
    represents the desired OWM web API version (or the currently supported one
    if no version number is specified)

    :param API_key: the OWM web API key (``None`` by default)
    :type API_key: str
    :param version: the OWM web API version. Defaults to ``None``, which means
        use the latest web API version
    :type version: str
    :returns: an instance of a proper *OWM* subclass
    :raises: *ValueError* when unsupported OWM API versions are provided
    """
    if version == "2.5":
        if config_module is None:
            config_module = "pyowm.webapi25.configuration25"
        cfg_module = __import__(config_module,  fromlist=[''])
        from webapi25.owm25 import OWM25
        return OWM25(cfg_module.parsers, API_key, cfg_module.cache)
    raise ValueError("Unsupported OWM web API version")
