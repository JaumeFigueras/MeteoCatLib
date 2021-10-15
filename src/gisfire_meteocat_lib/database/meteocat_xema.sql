CREATE TABLE public.meteocat_metadata_variables
(
  id bigserial,
  _codi int NOT NULL,
  _nom varchar NOT NULL,
  _unitat varchar NOT NULL,
  _acronim varchar NOT NULL,
  _tipus varchar NOT NULL,
  _decimals int NOT NULL,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  UNIQUE (_codi),
  CONSTRAINT pk_meteocat_metadata_variables PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_metadata_variables
  OWNER TO gisfireuser
;

CREATE TABLE public.meteocat_weather_stations
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
  CONSTRAINT pk_meteocat_weather_stations PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_weather_stations
  OWNER TO gisfireuser
;
SELECT AddGeometryColumn ('public', 'meteocat_weather_stations', 'geom', 4258, 'POINT', 2)
;

CREATE TABLE public.meteocat_weather_stations_status
(
  id bigserial,
  _codi int NOT NULL,
  _data_inici timestamp with time zone NOT NULL,
  _data_fi timestamp with time zone,
  meteocat_weather_stations_id bigint,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  UNIQUE (meteocat_weather_stations_id, _data_inici),
  CONSTRAINT pk_meteocat_weather_stations_status PRIMARY KEY (id),
  CONSTRAINT fk_meteocat_weather_stations_id_weather_stations_status FOREIGN KEY (meteocat_weather_stations_id) REFERENCES meteocat_weather_stations(id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_weather_stations_status
  OWNER TO gisfireuser
;

CREATE TABLE public.meteocat_measures
(
  id bigserial,
  _data timestamp with time zone NOT NULL,
  _valor double precision NOT NULL,
  _estat varchar NOT NULL,
  _base_horaria varchar NOT NULL,
  meteocat_weather_stations_id bigint,
  meteocat_metadata_variables_id bigint,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc') NOT NULL,
  CONSTRAINT pk_meteocat_measures PRIMARY KEY (id),
  CONSTRAINT fk_meteocat_weather_stations_id_measures FOREIGN KEY (meteocat_weather_stations_id) REFERENCES meteocat_weather_stations(id),
  CONSTRAINT fk_meteocat_metadata_variables_id_measures FOREIGN KEY (meteocat_metadata_variables_id) REFERENCES meteocat_metadata_variables(id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_weather_stations_status
  OWNER TO gisfireuser
;
