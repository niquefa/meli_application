import os
from analyzer import config
import logging
from datetime import datetime

DEFAULT_POSTGRESQL_TIMEOUT_IN_MILLISECONDS = 10000


def get_dna_id(dna):
    session = config.Session()
    sql_query_string = f"""
        SET statement_timeout TO {DEFAULT_POSTGRESQL_TIMEOUT_IN_MILLISECONDS}; commit;
        SELECT id as dna_id FROM stats.dna s WHERE s.dna_code = ARRAY{dna}
        """
    query_result = session.execute(sql_query_string)
    session.close()
    return query_result.first()["dna_id"]


# Here we assume that two calls with the same dna code will be only counted as one register.
def save_detection(dna, is_mutant):
    session = config.Session()
    sql_query_string = f"""
        SET statement_timeout TO {DEFAULT_POSTGRESQL_TIMEOUT_IN_MILLISECONDS}; commit;
        INSERT INTO stats.dna (dna_code, is_mutant, created_at, updated_at)            
        VALUES (ARRAY {dna}, {is_mutant}, NOW(), NOW())             
        ON CONFLICT (dna_code)         
        DO NOTHING
        """
    insert_result = session.execute(sql_query_string)
    session.commit()
    session.close()


def get_human_count():
    session = config.Session()
    query_result = session.execute(
        f"""
        SET statement_timeout TO {DEFAULT_POSTGRESQL_TIMEOUT_IN_MILLISECONDS}; commit;
        SELECT count(*) as total_rows 
        FROM stats.dna s
        WHERE s.is_mutant = false
        """
    )
    session.close()
    return query_result.first()["total_rows"]


def get_mutant_count():
    session = config.Session()
    query_result = session.execute(
        f"""
        SET statement_timeout TO {DEFAULT_POSTGRESQL_TIMEOUT_IN_MILLISECONDS}; commit;
        SELECT count(*) as total_rows 
        FROM stats.dna s
        WHERE s.is_mutant = true
        """
    )
    session.close()
    return query_result.first()["total_rows"]


def get_processed_dna_count():
    session = config.Session()
    query_result = session.execute(
        f"""
        SET statement_timeout TO {DEFAULT_POSTGRESQL_TIMEOUT_IN_MILLISECONDS}; commit;
        SELECT count(*) as total_rows 
        FROM stats.dna
        """
    )
    session.close()
    return query_result.first()["total_rows"]
