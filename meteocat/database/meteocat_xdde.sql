-- meteocat_xdde.sql

CREATE TABLE public.xdde_request
(
   request_date timestamp with time zone NOT NULL,
   http_status_code integer NOT NULL DEFAULT 200,
   number_of_lightnings integer DEFAULT NULL,
   ts timestamp with time zone DEFAULT (now() at time zone 'utc'),
   CONSTRAINT pk_xdde_request PRIMARY KEY (request_date)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.xdde_request
  OWNER TO gisfire_user
;
GRANT SELECT on public.xdde_request to gisfire_remoteuser;

CREATE TABLE public.lightning
(
  id bigserial,
  _id bigint NOT NULL,
  _data timestamp with time zone NOT NULL,
  _corrent_pic double precision NOT NULL,
  _chi2 double precision NOT NULL,
  _ellipse_eix_major double precision NOT NULL,
  _ellipse_eix_menor double precision NOT NULL,
  _ellipse_angle double precision DEFAULT NULL,
  _num_sensors integer NOT NULL,
  _nuvol_terra boolean NOT NULL,
  _id_municipi integer DEFAULT NULL,
  _coordenades_latitud double precision NOT NULL,
  _coordenades_longitud double precision NOT NULL,
  ts timestamp with time zone DEFAULT (now()),
  CONSTRAINT pk_lightning PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.lightning
  OWNER TO gisfire_user
;
GRANT SELECT on public.lightning to gisfire_remoteuser;
SELECT AddGeometryColumn ('public', 'lightning', 'geom', 4258, 'POINT', 2)
;
CREATE INDEX ON public.lightning (_data)
;
