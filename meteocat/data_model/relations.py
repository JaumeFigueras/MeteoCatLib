#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

from meteocat.data_model import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import func


class AssociationStationVariableState(Base):
    """
    Class container for the association table between weather stations, variables and the state of the variable.
    Provides the SQL Alchemy access to the ternary relation
    """
    __tablename__ = 'assoc_station_variable_state'
    weather_station_id: Mapped[int] = mapped_column("weather_station_id", ForeignKey("weather_station.id"), primary_key=True)
    variable_id: Mapped[int] = mapped_column("variable_id", ForeignKey("variable.id"), primary_key=True)
    variable_state_id: Mapped[int] = mapped_column("variable_state_id", ForeignKey("variable_state.id"), primary_key=True)
    ts: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    station: Mapped["WeatherStation"] = relationship(foreign_keys=[weather_station_id])
    variable: Mapped["Variable"] = relationship(foreign_keys=[variable_id])
    state: Mapped["VariableState"] = relationship(foreign_keys=[variable_state_id])


class AssociationStationVariableTimeBase(Base):
    """
    Class container for the association table between weather stations, variables and the time basis of the variable.
    Provides the SQL Alchemy access to the ternary relation
    """
    __tablename__ = 'assoc_station_variable_time_base'
    weather_station_id: Mapped[int] = mapped_column(ForeignKey('weather_station.id'), primary_key=True)
    variable_id: Mapped[int] = mapped_column(ForeignKey('variable.id'), primary_key=True)
    variable_time_base_id: Mapped[int] = mapped_column(ForeignKey('variable_time_base.id'), primary_key=True)
    ts: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    station: Mapped["WeatherStation"] = relationship(foreign_keys=[weather_station_id])
    variable: Mapped["Variable"] = relationship(foreign_keys=[variable_id])
    time_base: Mapped["VariableTimeBase"] = relationship(foreign_keys=[variable_time_base_id])
