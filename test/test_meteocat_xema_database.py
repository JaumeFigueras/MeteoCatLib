#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..src.gisfire_meteocat_lib.database.variable import Variable
from ..src.gisfire_meteocat_lib.database.weather_station import WeatherStation
from ..src.gisfire_meteocat_lib.database.weather_station import WeatherStationStatus
from ..src.gisfire_meteocat_lib.database.measures import Measure
import datetime
import pytz


def test_add_variable_01(db_session, postgresql_schema):
    var = Variable(1, 'Pressió atmosfèrica màxima', 'hPa', 'Px', 'DAT', 1)
    db_session.add(var)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_metadata_variables')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_metadata_variables')
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
    cursor.execute('SELECT count(*) FROM meteocat_weather_stations')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_weather_stations')
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
    cursor.execute('SELECT ST_X(geom), ST_Y(geom) FROM meteocat_weather_stations')
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
    cursor.execute('SELECT count(*) FROM meteocat_weather_stations')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT count(*) FROM meteocat_weather_stations_status')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_weather_stations_status')
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
    cursor.execute('SELECT count(*) FROM meteocat_weather_stations')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT count(*) FROM meteocat_weather_stations_status')
    record = cursor.fetchone()
    assert record[0] == 3
    cursor.execute('SELECT * FROM meteocat_weather_stations_status')
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
    cursor.execute('SELECT count(*) FROM meteocat_measures')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_measures')
    record = cursor.fetchone()
    assert record[1] == datetime.datetime(2017, 3, 27, 0, 0, tzinfo=pytz.UTC)
    assert record[2] == 8.3
    assert record[3] == 'V'
    assert record[4] == 'SH'
    assert record[5] == station.id
    assert record[6] == variable.id


def test_add_station_variable_01(db_session, postgresql_schema):
    variable = Variable(1, 'Pressió atmosfèrica màxima', 'hPa', 'Px', 'DAT', 1)
    db_session.add(variable)
    station = WeatherStation('CC', 'Orís', 'A', 42.075052799, 2.20980884646, 'Abocador comarcal', 626, 81509, 'Orís',
                             24, 'Osona', 8, 'Barcelona', 1, 'XEMA')
    db_session.add(station)
    db_session.commit()
    station.variables.append(variable)
    db_session.commit()
    cursor = postgresql_schema.cursor()
    cursor.execute('SELECT count(*) FROM meteocat_station_variable_association')
    record = cursor.fetchone()
    assert record[0] == 1
    cursor.execute('SELECT * FROM meteocat_station_variable_association')
    record = cursor.fetchone()
    assert record[0] == station.id
    assert record[1] == variable.id
