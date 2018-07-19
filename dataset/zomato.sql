DROP TABLE IF EXISTS zomato;

CREATE TABLE zomato (
	id varchar(25),
	name varchar(200),
	country_code varchar(25),
	city varchar(70),
	address varchar(250),
	locality varchar(100),
	locality_verbose varchar(100),
	longitude real,
	latitude real,
	cuisines varchar(200),
	average_cost_for_two real,
	currency varchar(50),
	has_table_booking varchar(25),
	has_online_delivery varchar(25),
	is_delivering_now varchar(25),
	switch_to_order_menu varchar(25),
	price_range real,
	aggregate_rating real,
	rating_color varchar(50),
	rating_text varchar(50),
	votes real
)


COPY zomato
FROM 'C:\tmp\zomate_import.csv' DELIMITER ',' CSV HEADER encoding 'windows-1251';