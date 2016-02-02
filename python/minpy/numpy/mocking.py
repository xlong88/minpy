#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import sys
import importlib

from ..utils import log
from ..dispatch import registry
from ..dispatch import policy
from ..array_variants import * # import all array_variants names

'''
# TODO why not globals() ?
_old_definitions = {
    '__name__': __name__,
    '__package__': __package__,
    '__file__': __file__,
}

try:
    _old_definitions['__cached__'] = __cached__
    _old_definitions['__loader__'] = __loader__
    _old_definitions['__spec__'] = __loader__
except NameError:
    pass
'''

class DynamicLookupError(KeyError):
    pass

class Module(object):
    """Module level dynamic lookup."""

    _registry = registry.Registry()
    _policy = policy.Policy()

    def __init__(self, old, name=None):
        self._logger = log.get_logger(name)
        self._old = old
        #for var in variants:
            #mod = importlib.import_module('minpy.array_variants.{}'.format(var))
            #print mod
            #print mod.__dict__
            #print mod.def_grads
    
    def dispatch(self, name, *args, **kargs):
        pass

    def __getattr__(self, name):
        self._logger.info('Look up name {}'.format(name))
        # Special members for internal use.
        if name == '__registry__':
            return self._registry
        elif name in self._old:
            return self._old[name]
        elif self._registry.has_name(name):
            return None  # TODO policy here
        else:
            raise DynamicLookupError()