
-- migrate:up
CREATE SCHEMA IF NOT EXISTS stats;

CREATE TABLE IF NOT EXISTS stats.dna(
	id BIGSERIAL PRIMARY KEY,
	dna_code TEXT[] UNIQUE NOT NULL,
	is_mutant BOOLEAN NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
	updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE UNIQUE INDEX IF NOT EXISTS dna_code_index ON stats.dna(dna_code);

CREATE OR REPLACE FUNCTION trigger_set_timestamp_to_analyzer()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_timestamp_dna
BEFORE UPDATE ON stats.dna
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp_to_analyzer();

-- migrate:down
