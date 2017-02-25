"""
Copyright 2017 Vendasta Technologies Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



vSlack
"""
import os

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'VERSION')) as f:
    __version__ = f.read().strip()


__all__ = []

# W0401: 71,0: Wildcard import
# W0403: 71,0: Relative import
# E0602: 77,11: Undefined variable
# matching how Guido does it in NDB
# pylint: disable=W0401,W0403,E0602,wrong-import-position
from core import *
__all__ += core.__all__
