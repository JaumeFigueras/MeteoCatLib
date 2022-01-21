CREATE TYPE meteocat_weather_station_state_type AS ENUM('ACTIVE', 'DISMANTLED', 'REPAIR')

CREATE TABLE public.meteocat_weather_station_state
(
  id bigserial,
  _codi meteocat_weather_station_state_type NOT NULL,
  _data_inici timestamp with time zone NOT NULL,
  _data_fi timestamp with time zone DEFAULT NULL,
  meteocat_weather_station_id bigint,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  UNIQUE (meteocat_weather_station_id, _data_inici),
  CONSTRAINT pk_meteocat_weather_station_status PRIMARY KEY (id),
  CONSTRAINT fk_meteocat_weather_station_id_weather_stations_status FOREIGN KEY (meteocat_weather_station_id) REFERENCES meteocat_weather_station(id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_weather_station_state
  OWNER TO gisfireuser
;

CREATE TABLE public.meteocat_weather_station
(
  id bigserial,
  _codi varchar NOT NULL,
  _nom varchar NOT NULL,
  _tipus varchar NOT NULL,
  _coordenades_latitud double precision NOT NULL,
  _coordenades_longitud double precision NOT NULL,
  _emplacament varchar NOT NULL,
  _altitud double precision NOT NULL,
  _municipi_codi int NOT NULL,
  _municipi_nom varchar NOT NULL,
  _comarca_codi int NOT NULL,
  _comarca_nom varchar NOT NULL,
  _provincia_codi int NOT NULL,
  _provincia_nom varchar NOT NULL,
  _xarxa_codi int NOT NULL,
  _xarxa_nom varchar NOT NULL,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  UNIQUE (_codi),
  CONSTRAINT pk_meteocat_weather_station PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_weather_station
  OWNER TO gisfireuser
;
SELECT AddGeometryColumn ('public', 'meteocat_weather_station', 'geom', 4258, 'POINT', 2)
;







CREATE TYPE variable_type AS ENUM('DAT', 'AUX', 'CMV');

CREATE TABLE public.meteocat_variable
(
  id bigserial,
  _codi int NOT NULL,
  _nom varchar NOT NULL,
  _unitat varchar NOT NULL,
  _acronim varchar NOT NULL,
  _tipus variable_type NOT NULL,
  _decimals int NOT NULL,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  UNIQUE (_codi),
  CONSTRAINT pk_meteocat_variable PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_variable
  OWNER TO gisfireuser
;


CREATE TABLE public.meteocat_measure
(
  id bigserial,
  _data timestamp with time zone NOT NULL,
  _data_extrem timestamp with time zone DEFAULT NULL,
  _valor double precision NOT NULL,
  _estat varchar NOT NULL,
  _base_horaria varchar NOT NULL,
  meteocat_weather_station_id bigint,
  meteocat_variable_id bigint,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  CONSTRAINT pk_meteocat_measure PRIMARY KEY (id),
  CONSTRAINT fk_meteocat_weather_station_id_measure FOREIGN KEY (meteocat_weather_station_id) REFERENCES meteocat_weather_station(id),
  CONSTRAINT fk_meteocat_variable_id_measure FOREIGN KEY (meteocat_variable_id) REFERENCES meteocat_variable(id),
  CONSTRAINT uq_meteocat_measure_station_variable_date UNIQUE (meteocat_weather_station_id, meteocat_variable_id, _data)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_measure
  OWNER TO gisfireuser
;

CREATE TABLE public.meteocat_variable_status
(
  id bigserial,
  _codi int NOT NULL,
  _data_inici timestamp with time zone NOT NULL,
  _data_fi timestamp with time zone,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  CONSTRAINT pk_meteocat_variable_status PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_variable_status
  OWNER TO gisfireuser
;


CREATE TABLE public.meteocat_station_variable_status_association
(
  meteocat_weather_station_id bigint,
  meteocat_variable_id bigint,
  meteocat_variable_status_id bigint,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  CONSTRAINT pk_meteocat_station_variable_status_association PRIMARY KEY (meteocat_weather_station_id, meteocat_variable_id, meteocat_variable_status_id),
  CONSTRAINT fk_meteocat_weather_station_id_station_variable_status_association FOREIGN KEY (meteocat_weather_station_id) REFERENCES meteocat_weather_station(id),
  CONSTRAINT fk_meteocat_variable_id_station_variable_status_association FOREIGN KEY (meteocat_variable_id) REFERENCES meteocat_variable(id),
  CONSTRAINT fk_meteocat_variable_status_id_station_variable_status_association FOREIGN KEY (meteocat_variable_status_id) REFERENCES meteocat_variable_status(id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_station_variable_status_association
  OWNER TO gisfireuser
;

CREATE TABLE public.meteocat_variable_time_basis
(
  id bigserial,
  _codi varchar NOT NULL,
  _data_inici timestamp with time zone NOT NULL,
  _data_fi timestamp with time zone,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  CONSTRAINT pk_meteocat_variable_time_basis PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_variable_time_basis
  OWNER TO gisfireuser
;

CREATE TABLE public.meteocat_station_variable_time_association
(
  meteocat_weather_station_id bigint,
  meteocat_variable_id bigint,
  meteocat_variable_time_basis_id bigint,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  CONSTRAINT pk_meteocat_station_variable_time_association PRIMARY KEY (meteocat_weather_station_id, meteocat_variable_id, meteocat_variable_time_basis_id),
  CONSTRAINT fk_meteocat_weather_station_id_station_variable_time_association FOREIGN KEY (meteocat_weather_station_id) REFERENCES meteocat_weather_station(id),
  CONSTRAINT fk_meteocat_variable_id_station_variable_time_association FOREIGN KEY (meteocat_variable_id) REFERENCES meteocat_variable(id),
  CONSTRAINT fk_meteocat_variable_time_basis_id_station_variable_time_association FOREIGN KEY (meteocat_variable_time_basis_id) REFERENCES meteocat_variable_time_basis(id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_station_variable_time_association
  OWNER TO gisfireuser
;

