CREATE TYPE weather_station_state_category AS ENUM('ACTIVE', 'DISMANTLED', 'REPAIR');
ALTER TYPE weather_station_state_category
  OWNER TO gisfire_user
;

CREATE TYPE weather_station_category AS ENUM('AUTO', 'OTHER');
ALTER TYPE weather_station_state_category
  OWNER TO gisfire_user
;

CREATE TABLE public.weather_station
(
  id bigserial,
  _codi varchar NOT NULL,
  _nom varchar NOT NULL,
  _tipus weather_station_category NOT NULL,
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
  ts timestamp with time zone DEFAULT (now()) NOT NULL,
  CONSTRAINT uk_weather_station_codi UNIQUE (_codi),
  CONSTRAINT pk_weather_station PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.weather_station
  OWNER TO gisfire_user
;
GRANT ALL ON public.weather_station
  TO gisfire_remoteuser
;
SELECT AddGeometryColumn ('public', 'weather_station', 'geom', 4258, 'POINT', 2)
;

CREATE TABLE public.weather_station_state
(
  id bigserial,
  _codi weather_station_state_category NOT NULL,
  _data_inici timestamp with time zone NOT NULL,
  _data_fi timestamp with time zone DEFAULT NULL,
  weather_station_id bigint,
  ts timestamp with time zone DEFAULT (now()) NOT NULL,
  UNIQUE (weather_station_id, _data_inici),
  CONSTRAINT pk_weather_station_state PRIMARY KEY (id),
  CONSTRAINT fk_weather_station_id_weather_stations_state FOREIGN KEY (weather_station_id) REFERENCES weather_station(id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.weather_station_state
  OWNER TO gisfire_user
;
GRANT ALL ON public.weather_station_state
  TO gisfire_remoteuser
;

CREATE TYPE variable_category AS ENUM('DAT', 'AUX', 'CMV');
ALTER TYPE variable_category
  OWNER TO gisfire_user
;
CREATE TYPE variable_state_category AS ENUM('DISMANTLED', 'ACTIVE', 'REPAIR');
ALTER TYPE variable_state_category
  OWNER TO gisfire_user
;
CREATE TYPE variable_time_base_category AS ENUM('HO', 'SH', 'DM', 'MI', 'D5');
ALTER TYPE variable_time_base_category
  OWNER TO gisfire_user
;

CREATE TABLE public.variable
(
  id bigserial,
  _codi int NOT NULL,
  _nom varchar NOT NULL,
  _unitat varchar NOT NULL,
  _acronim varchar NOT NULL,
  _tipus variable_category NOT NULL,
  _decimals int NOT NULL,
  ts timestamp with time zone DEFAULT (now()) NOT NULL,
  CONSTRAINT uk_variable_codi UNIQUE (_codi),
  CONSTRAINT pk_variable PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.variable
  OWNER TO gisfire_user
;
GRANT ALL ON public.variable
  TO gisfire_remoteuser
;

CREATE TABLE public.variable_state
(
  id bigserial,
  _codi variable_state_category NOT NULL,
  _data_inici timestamp with time zone NOT NULL,
  _data_fi timestamp with time zone,
  ts timestamp with time zone DEFAULT (now()) NOT NULL,
  CONSTRAINT pk_variable_state PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.variable_state
  OWNER TO gisfire_user
;
GRANT ALL ON public.variable_state
  TO gisfire_remoteuser
;

CREATE TABLE public.variable_time_base
(
  id bigserial,
  _codi variable_time_base_category NOT NULL,
  _data_inici timestamp with time zone NOT NULL,
  _data_fi timestamp with time zone,
  ts timestamp with time zone DEFAULT (now()) NOT NULL,
  CONSTRAINT pk_variable_time_base PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.variable_time_base
  OWNER TO gisfire_user
;
GRANT ALL ON public.variable_time_base
  TO gisfire_remoteuser
;

CREATE TABLE public.assoc_station_variable_state
(
  weather_station_id bigint,
  variable_id bigint,
  variable_state_id bigint,
  ts timestamp with time zone DEFAULT (now()) NOT NULL,
  CONSTRAINT pk_assoc_station_variable_state PRIMARY KEY (weather_station_id, variable_id, variable_state_id),
  CONSTRAINT fk_weather_station_id_assoc_station_variable_state FOREIGN KEY (weather_station_id) REFERENCES weather_station(id),
  CONSTRAINT fk_variable_id_assoc_station_variable_state FOREIGN KEY (variable_id) REFERENCES variable(id),
  CONSTRAINT fk_variable_state_id_assoc_station_variable_state FOREIGN KEY (variable_state_id) REFERENCES variable_state(id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.assoc_station_variable_state
  OWNER TO gisfire_user
;
GRANT ALL ON public.assoc_station_variable_state
  TO gisfire_remoteuser
;

CREATE TABLE public.assoc_station_variable_time_base
(
  weather_station_id bigint,
  variable_id bigint,
  variable_time_base_id bigint,
  ts timestamp with time zone DEFAULT (now()) NOT NULL,
  CONSTRAINT pk_association_station_variable_time_base PRIMARY KEY (weather_station_id, variable_id, variable_time_base_id),
  CONSTRAINT fk_weather_station_id_assoc_station_variable_time_base FOREIGN KEY (weather_station_id) REFERENCES weather_station(id),
  CONSTRAINT fk_variable_id_assoc_station_variable_time_base FOREIGN KEY (variable_id) REFERENCES variable(id),
  CONSTRAINT fk_variable_time_base_id_assoc_station_variable_time_base FOREIGN KEY (variable_time_base_id) REFERENCES variable_time_base(id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.assoc_station_variable_time_base
  OWNER TO gisfire_user
;
GRANT ALL ON public.assoc_station_variable_time_base
  TO gisfire_remoteuser
;

CREATE TYPE measure_time_base_type AS ENUM('HO', 'SH', 'DM', 'MI', 'D5');
ALTER TYPE measure_time_base_type
  OWNER TO gisfire_user
;
CREATE TYPE measure_validity_type AS ENUM('PENDING', 'VALID', 'VALIDATING');
ALTER TYPE measure_validity_type
  OWNER TO gisfire_user
;

CREATE TABLE public.measure
(
  id bigserial,
  _id varchar DEFAULT NULL,
  _data timestamp with time zone NOT NULL,
  _data_extrem timestamp with time zone DEFAULT NULL,
  _valor double precision NOT NULL,
  _estat measure_validity_type NOT NULL,
  _base_horaria measure_time_base_type NOT NULL,
  weather_station_id bigint,
  variable_id bigint,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  CONSTRAINT pk_measure PRIMARY KEY (id),
  CONSTRAINT fk_weather_station_id_measure FOREIGN KEY (weather_station_id) REFERENCES weather_station(id),
  CONSTRAINT fk_variable_id_measure FOREIGN KEY (variable_id) REFERENCES variable(id),
  CONSTRAINT uq_measure_station_variable_date UNIQUE (weather_station_id, variable_id, _data)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.measure
  OWNER TO gisfire_user
;
GRANT ALL ON public.measure
  TO gisfire_remoteuser
;
CREATE INDEX idx_measure_data on measure(_data);
CREATE INDEX idx_measure_data_weather_station_id on measure(_data, weather_station_id);
