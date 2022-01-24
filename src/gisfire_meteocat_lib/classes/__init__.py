#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .weather_station import *
from .variable import *
from .relations import *

