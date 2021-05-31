#!/bin/bash
export POSTGRES_HOST=$(echo $DB_SECRET | jq -r .host)
export POSTGRES_PORT=$(echo $DB_SECRET | jq -r .port)
export POSTGRES_USER=$(echo $DB_SECRET | jq -r .username)
export POSTGRES_PASSWORD=$(echo $DB_SECRET | jq -r .password)
export POSTGRES_DB=analyzer

python3 -m app
