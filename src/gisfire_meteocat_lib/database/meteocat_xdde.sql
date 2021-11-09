CREATE TABLE public.meteocat_xdde_request
(
   request_date timestamp with time zone NOT NULL,
   result_code integer NOT NULL DEFAULT 200,
   number_of_lightnings integer DEFAULT NULL,
   ts timestamp with time zone DEFAULT (now() at time zone 'utc'),
   CONSTRAINT pk_xdde_requests PRIMARY KEY (request_date)
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
  _id bigint NOT NULL,
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
  CONSTRAINT pk_lightnings PRIMARY KEY (id),
  CONSTRAINT uq_lightnings UNIQUE (_id)
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
