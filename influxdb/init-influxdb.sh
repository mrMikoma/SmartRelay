#!/bin/sh
influx -execute 'CREATE DATABASE nordpool'
influx -execute 'CREATE USER "nordpool_user" WITH PASSWORD '\''your_strong_password'\'' WITH ALL PRIVILEGES'
