#!/bin/sh
influx -execute 'CREATE DATABASE nordpool'
influx -execute 'CREATE USER "nordpool" WITH PASSWORD '\''nordpool'\'' WITH ALL PRIVILEGES'
