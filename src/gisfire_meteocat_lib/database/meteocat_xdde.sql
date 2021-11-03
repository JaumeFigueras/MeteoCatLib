CREATE TABLE public.meteocat_xdde_request
(
   year integer,
   month integer,
   day integer,
   hour integer,
   result_code integer NOT NULL DEFAULT 200,
   number_of_lightnings integer DEFAULT NULL,
   ts timestamp with time zone DEFAULT (now() at time zone 'utc'),
   CONSTRAINT pk_xdde_requests PRIMARY KEY (year, month, day, hour)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_xdde_request
  OWNER TO gisfireuser
;

CREATE TABLE public.meteocat_lightning
(
  id bigserial,
  _id bigint,
  _data timestamp with time zone NOT NULL,
  _corrent_pic double precision NOT NULL,
  _chi2 double precision NOT NULL,
  _ellipse_eix_major double precision NOT NULL,
  _ellipse_eix_menor double precision NOT NULL,
  _ellipse_angle double precision NOT NULL,
  _num_sensors integer NOT NULL,
  _nuvol_terra boolean NOT NULL,
  _id_municipi integer,
  _coordenades_latitud double precision NOT NULL,
  _coordenades_longitud double precision NOT NULL,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc'),
  CONSTRAINT pk_lightnings PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_lightning
  OWNER TO gisfireuser
;
SELECT AddGeometryColumn ('public', 'meteocat_lightning', 'geom', 4258, 'POINT', 2)
;
