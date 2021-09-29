CREATE TABLE public.meteocat_metadata_variables
(
  id bigserial,
  _code int,
  _nom varchar NOT NULL,
  _unitat varchar NOT NULL,
  _acronim varchar NOT NULL,
  _tipus varchar NOT NULL,
  _decimals int NOT NULL,
  ts timestamp with time zone DEFAULT (now() at time zone 'utc'),
  CONSTRAINT pk_lightnings PRIMARY KEY (id)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE public.meteocat_metadata_variables
  OWNER TO gisfireuser
;

