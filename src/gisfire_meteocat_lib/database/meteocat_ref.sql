
CREATE TABLE public.meteocat_references
(
  id bigserial,
  _codi integer NOT NULL,
  _nom varchar NOT NULL,
  admin_level integer NOT NULL,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc'),
  UNIQUE (admin_level, _codi),
  CONSTRAINT pk_reference PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_references
  OWNER TO gisfireuser
;
SELECT AddGeometryColumn ('public', 'meteocat_references', 'geom', 25831, 'MULTIPOLYGON', 2)
;
