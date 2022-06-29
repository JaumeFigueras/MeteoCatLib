CREATE TYPE meteocat_weather_station_state_type AS ENUM('ACTIVE', 'DISMANTLED', 'REPAIR');
ALTER TYPE meteocat_weather_station_state_type
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
  CONSTRAINT uk_meteocat_weather_station_codi UNIQUE (_codi),
  CONSTRAINT pk_meteocat_weather_station PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_weather_station
  OWNER TO gisfireuser
;
GRANT ALL ON public.meteocat_weather_station
  TO remotegisfireuser
;
SELECT AddGeometryColumn ('public', 'meteocat_weather_station', 'geom', 4258, 'POINT', 2)
;

CREATE TABLE public.meteocat_weather_station_state
(
  id bigserial,
  _codi meteocat_weather_station_state_type NOT NULL,
  _data_inici timestamp with time zone NOT NULL,
  _data_fi timestamp with time zone DEFAULT NULL,
  meteocat_weather_station_id bigint,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  UNIQUE (meteocat_weather_station_id, _data_inici),
  CONSTRAINT pk_meteocat_weather_station_state PRIMARY KEY (id),
  CONSTRAINT fk_meteocat_weather_station_id_weather_stations_state FOREIGN KEY (meteocat_weather_station_id) REFERENCES meteocat_weather_station(id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_weather_station_state
  OWNER TO gisfireuser
;
GRANT ALL ON public.meteocat_weather_station_state
  TO remotegisfireuser
;

CREATE TYPE variable_type AS ENUM('DAT', 'AUX', 'CMV');
ALTER TYPE variable_type
  OWNER TO gisfireuser
;
CREATE TYPE variable_state_type AS ENUM('DISMANTLED', 'ACTIVE', 'REPAIR');
ALTER TYPE variable_state_type
  OWNER TO gisfireuser
;
CREATE TYPE variable_time_base_type AS ENUM('HO', 'SH', 'DM', 'MI', 'D5');
ALTER TYPE variable_time_base_type
  OWNER TO gisfireuser
;

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
  CONSTRAINT uk_meteocat_variable_codi UNIQUE (_codi),
  CONSTRAINT pk_meteocat_variable PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_variable
  OWNER TO gisfireuser
;
GRANT ALL ON public.meteocat_variable
  TO remotegisfireuser
;

CREATE TABLE public.meteocat_variable_state
(
  id bigserial,
  _codi variable_state_type NOT NULL,
  _data_inici timestamp with time zone NOT NULL,
  _data_fi timestamp with time zone,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  CONSTRAINT pk_meteocat_variable_state PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_variable_state
  OWNER TO gisfireuser
;
GRANT ALL ON public.meteocat_variable_state
  TO remotegisfireuser
;

CREATE TABLE public.meteocat_variable_time_base
(
  id bigserial,
  _codi variable_time_base_type NOT NULL,
  _data_inici timestamp with time zone NOT NULL,
  _data_fi timestamp with time zone,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  CONSTRAINT pk_meteocat_variable_time_base PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_variable_time_base
  OWNER TO gisfireuser
;
GRANT ALL ON public.meteocat_variable_time_base
  TO remotegisfireuser
;

CREATE TABLE public.meteocat_station_variable_state_assoc
(
  meteocat_weather_station_id bigint,
  meteocat_variable_id bigint,
  meteocat_variable_state_id bigint,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  CONSTRAINT pk_meteocat_station_variable_state_assoc PRIMARY KEY (meteocat_weather_station_id, meteocat_variable_id, meteocat_variable_state_id),
  CONSTRAINT fk_meteocat_weather_station_id_station_variable_state_assoc FOREIGN KEY (meteocat_weather_station_id) REFERENCES meteocat_weather_station(id),
  CONSTRAINT fk_meteocat_variable_id_station_variable_state_assoc FOREIGN KEY (meteocat_variable_id) REFERENCES meteocat_variable(id),
  CONSTRAINT fk_meteocat_variable_state_id_station_variable_state_assoc FOREIGN KEY (meteocat_variable_state_id) REFERENCES meteocat_variable_state(id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_station_variable_state_assoc
  OWNER TO gisfireuser
;
GRANT ALL ON public.meteocat_station_variable_state_assoc
  TO remotegisfireuser
;

CREATE TABLE public.meteocat_station_variable_time_assoc
(
  meteocat_weather_station_id bigint,
  meteocat_variable_id bigint,
  meteocat_variable_time_base_id bigint,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  CONSTRAINT pk_meteocat_station_variable_time_assoc PRIMARY KEY (meteocat_weather_station_id, meteocat_variable_id, meteocat_variable_time_base_id),
  CONSTRAINT fk_meteocat_weather_station_id_station_variable_time_assoc FOREIGN KEY (meteocat_weather_station_id) REFERENCES meteocat_weather_station(id),
  CONSTRAINT fk_meteocat_variable_id_station_variable_time_assoc FOREIGN KEY (meteocat_variable_id) REFERENCES meteocat_variable(id),
  CONSTRAINT fk_meteocat_variable_time_base_id_station_variable_time_assoc FOREIGN KEY (meteocat_variable_time_base_id) REFERENCES meteocat_variable_time_base(id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_station_variable_time_assoc
  OWNER TO gisfireuser
;
GRANT ALL ON public.meteocat_station_variable_time_assoc
  TO remotegisfireuser
;

CREATE TYPE measure_time_base_type AS ENUM('HO', 'SH', 'DM', 'MI', 'D5');
ALTER TYPE measure_time_base_type
  OWNER TO gisfireuser
;
CREATE TYPE measure_validity_type AS ENUM('PENDING', 'VALID', 'VALIDATING');
ALTER TYPE measure_validity_type
  OWNER TO gisfireuser
;

CREATE TABLE public.meteocat_measure
(
  id bigserial,
  _meteocat_id varchar DEFAULT NULL,
  _data timestamp with time zone NOT NULL,
  _data_extrem timestamp with time zone DEFAULT NULL,
  _valor double precision NOT NULL,
  _estat measure_validity_type NOT NULL,
  _base_horaria measure_time_base_type NOT NULL,
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
GRANT ALL ON public.meteocat_measure
  TO remotegisfireuser
;
CREATE INDEX idx_meteocat_measure_data on meteocat_measure(_data);
CREATE INDEX idx_meteocat_measure_data_weather_station_id on meteocat_measure(_data, meteocat_weather_station_id);
