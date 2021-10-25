#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..src.gisfire_meteocat_lib.database.variable import Variable
from ..src.gisfire_meteocat_lib.database.variable import VariableStatus
from ..src.gisfire_meteocat_lib.database.variable import VariableTimeBasis
from ..src.gisfire_meteocat_lib.database.variable import WeatherStationVariableTimeBasisAssociation
from ..src.gisfire_meteocat_lib.database.weather_station import WeatherStation
from ..src.gisfire_meteocat_lib.database.weather_station import WeatherStationStatus
from ..src.gisfire_meteocat_lib.database.weather_station import WeatherStationVariableStatusAssociation
from ..src.gisfire_meteocat_lib.database.measures import Measure
from ..src.gisfire_meteocat_lib.database.meteocat_xema import get_weather_stations
from ..src.gisfire_meteocat_lib.database.meteocat_xema import get_variable
import datetime
import pytz


def test_add_variable_01(db_session, postgresql_schema):
    var = Variable(1, 'Pressió atmosfèrica màxima', 'hPa', 'Px', 'DAT', 1)
    db_session.add(var)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_variable')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_variable')
    record = cursor.fetchone()
    assert record[1] == 1
    assert record[2] == 'Pressió atmosfèrica màxima'
    assert record[3] == 'hPa'
    assert record[4] == 'Px'
    assert record[5] == 'DAT'
    assert record[6] == 1


def test_add_weather_station_01(db_session, postgresql_schema):
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    db_session.add(station)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_weather_station')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_weather_station')
    record = cursor.fetchone()
    assert record[1] == 'CC'
    assert record[2] == 'Orís'
    assert record[3] == 'A'
    assert record[4] == 42.075052799
    assert record[5] == 2.20980884646
    assert record[6] == 'Abocador comarcal'
    assert record[7] == 626
    assert record[8] == 81509
    assert record[9] == 'Orís'
    assert record[10] == 24
    assert record[11] == 'Osona'
    assert record[12] == 8
    assert record[13] == 'Barcelona'
    assert record[14] == 1
    assert record[15] == 'XEMA'
    cursor.execute('SELECT ST_X(geom), ST_Y(geom) FROM meteocat_weather_station')
    record = cursor.fetchone()
    assert record[0] == 2.20980884646
    assert record[1] == 42.075052799


def test_add_weather_station_02(db_session, postgresql_schema):
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    status = WeatherStationStatus(2, '2003-11-06T13:00Z')
    station.status.append(status)
    db_session.add(station)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_weather_station')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT count(*) FROM meteocat_weather_station_status')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_weather_station_status')
    record = cursor.fetchone()
    assert record[1] == 2
    assert record[2] == datetime.datetime(2003, 11, 6, 13, 0, tzinfo=pytz.UTC)
    assert record[3] is None
    assert record[4] == station.id


def test_add_weather_station_03(db_session, postgresql_schema):
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    status = WeatherStationStatus(2, '1997-09-17T15:00Z', '2003-02-24T21:00Z')
    station.status.append(status)
    status = WeatherStationStatus(3, '2003-02-24T21:00Z', '2004-12-03T12:00Z')
    station.status.append(status)
    status = WeatherStationStatus(2, '2004-12-03T12:00Z')
    station.status.append(status)
    db_session.add(station)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_weather_station')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT count(*) FROM meteocat_weather_station_status')
    record = cursor.fetchone()
    assert record[0] == 3
    cursor.execute('SELECT * FROM meteocat_weather_station_status')
    record = cursor.fetchone()
    assert record[1] == 2
    assert record[2] == datetime.datetime(1997, 9, 17, 15, 0, tzinfo=pytz.UTC)
    assert record[3] == datetime.datetime(2003, 2, 24, 21, 0, tzinfo=pytz.UTC)
    assert record[4] == station.id
    record = cursor.fetchone()
    assert record[1] == 3
    assert record[2] == datetime.datetime(2003, 2, 24, 21, 0, tzinfo=pytz.UTC)
    assert record[3] == datetime.datetime(2004, 12, 3, 12, 0, tzinfo=pytz.UTC)
    assert record[4] == station.id
    record = cursor.fetchone()
    assert record[1] == 2
    assert record[2] == datetime.datetime(2004, 12, 3, 12, 0, tzinfo=pytz.UTC)
    assert record[3] is None
    assert record[4] == station.id


def test_add_measure_01(db_session, postgresql_schema):
    variable = Variable(1, 'Pressió atmosfèrica màxima', 'hPa', 'Px', 'DAT', 1)
    db_session.add(variable)
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    db_session.add(station)
    db_session.commit()
    measure = Measure('2017-03-27T00:00Z', 8.3, 'V', 'SH')
    variable.measures.append(measure)
    station.measures.append(measure)
    db_session.add(measure)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_measure')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_measure')
    record = cursor.fetchone()
    assert record[1] == datetime.datetime(2017, 3, 27, 0, 0, tzinfo=pytz.UTC)
    assert record[2] == 8.3
    assert record[3] == 'V'
    assert record[4] == 'SH'
    assert record[5] == station.id
    assert record[6] == variable.id


def test_add_station_variable_status_01(db_session, postgresql_schema):
    variable = Variable(1, 'Pressió atmosfèrica màxima', 'hPa', 'Px', 'DAT', 1)
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    status = VariableStatus(2, '2017-03-27T00:00Z')
    association = WeatherStationVariableStatusAssociation(variable=variable, station=station, status=status)
    db_session.add(association)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_station_variable_status_association')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_station_variable_status_association')
    record = cursor.fetchone()
    assert record[0] == station.id
    assert record[1] == variable.id
    assert record[2] == status.id
    variables = db_session.query(WeatherStationVariableStatusAssociation)\
        .filter(WeatherStationVariableStatusAssociation.meteocat_weather_station_id == station.id)\
        .all()
    assert len(variables) == 1
    assert variables[0].meteocat_variable_id == variable.id
    variables = db_session.query(WeatherStationVariableStatusAssociation)\
        .filter(WeatherStationVariableStatusAssociation.meteocat_weather_station_id == station.id)\
        .join(WeatherStationVariableStatusAssociation.status)\
        .filter(VariableStatus.code == 2)\
        .all()
    assert len(variables) == 1
    assert variables[0].meteocat_variable_id == variable.id


def test_add_station_variable_time_basis_01(db_session, postgresql_schema):
    variable = Variable(1, 'Pressió atmosfèrica màxima', 'hPa', 'Px', 'DAT', 1)
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    time_basis = VariableTimeBasis('SH', '2017-03-27T00:00Z')
    association = WeatherStationVariableTimeBasisAssociation(variable=variable, station=station, time_basis=time_basis)
    db_session.add(association)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_station_variable_time_association')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_station_variable_time_association')
    record = cursor.fetchone()
    assert record[0] == station.id
    assert record[1] == variable.id
    assert record[2] == time_basis.id
    variables = db_session.query(WeatherStationVariableTimeBasisAssociation)\
        .filter(WeatherStationVariableTimeBasisAssociation.meteocat_weather_station_id == station.id)\
        .all()
    assert len(variables) == 1
    assert variables[0].meteocat_variable_id == variable.id
    variables = db_session.query(WeatherStationVariableTimeBasisAssociation)\
        .filter(WeatherStationVariableTimeBasisAssociation.meteocat_weather_station_id == station.id)\
        .join(WeatherStationVariableTimeBasisAssociation.time_basis)\
        .filter(VariableTimeBasis.code == 'SH')\
        .all()
    assert len(variables) == 1
    assert variables[0].meteocat_variable_id == variable.id


def test_get_weather_stations_01(db_session):
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    status = WeatherStationStatus(2, '2003-11-06T13:00Z')
    station.status.append(status)
    db_session.add(station)
    db_session.commit()
    stations = get_weather_stations(db_session)
    assert len(stations) == 1
    assert stations[0].code == 'CC'
    assert len(stations[0].status) == 1


def test_get_weather_stations_02(db_session):
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    status = WeatherStationStatus(2, '2003-11-06T13:00Z')
    station.status.append(status)
    db_session.add(station)
    db_session.commit()
    stations = get_weather_stations(db_session, active_stations=True)
    assert len(stations) == 1


def test_get_weather_stations_03(db_session):
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    status = WeatherStationStatus(2, '2003-11-06T13:00Z', '2013-11-06T13:00Z')
    station.status.append(status)
    status = WeatherStationStatus(3, '2013-11-06T13:00Z', '2015-11-06T13:00Z')
    station.status.append(status)
    status = WeatherStationStatus(2, '2015-11-06T13:00Z')
    station.status.append(status)
    db_session.add(station)
    db_session.commit()
    stations = get_weather_stations(db_session)
    assert len(stations) == 1
    assert stations[0].code == 'CC'
    assert len(stations[0].status) == 3


def test_get_weather_stations_04(db_session):
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    status = WeatherStationStatus(2, '2003-11-06T13:00Z', '2013-11-06T13:00Z')
    station.status.append(status)
    status = WeatherStationStatus(3, '2013-11-06T13:00Z', '2015-11-06T13:00Z')
    station.status.append(status)
    db_session.add(station)
    db_session.commit()
    stations = get_weather_stations(db_session, True)
    assert len(stations) == 0


def test_get_weather_stations_05(db_session):
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    status = WeatherStationStatus(2, '2003-11-06T13:00Z', '2013-11-06T13:00Z')
    station.status.append(status)
    status = WeatherStationStatus(3, '2013-11-06T13:00Z', '2015-11-06T13:00Z')
    station.status.append(status)
    status = WeatherStationStatus(2, '2015-11-06T13:00Z')
    station.status.append(status)
    db_session.add(station)
    db_session.commit()
    stations = get_weather_stations(db_session, True, '2014-11-06T13:00Z')
    assert len(stations) == 0
    stations = get_weather_stations(db_session, True, '2016-11-06T13:00Z')
    assert len(stations) == 1
    stations = get_weather_stations(db_session, True, datetime.datetime(2018, 10, 10, 10, 0, 0))
    assert len(stations) == 1


def test_get_variable_01(db_session):
    variable = Variable(1, 'Pressió atmosfèrica màxima', 'hPa', 'Px', 'DAT', 1)
    db_session.add(variable)
    db_session.commit()
    var = get_variable(db_session, variable.code)
    assert var.code == variable.code


def test_get_variable_02(db_session):
    variable = Variable(1, 'Pressió atmosfèrica màxima', 'hPa', 'Px', 'DAT', 1)
    db_session.add(variable)
    db_session.commit()
    var = get_variable(db_session, 42)
    assert var is None
