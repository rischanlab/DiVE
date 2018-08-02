#!/usr/bin/python
import psycopg2

def config_data(db):
	conn = psycopg2.connect(dbname=db, user= "postgres", password="zenvisage")
	cur = conn.cursor()
	return cur