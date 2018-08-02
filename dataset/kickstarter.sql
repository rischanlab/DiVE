DROP TABLE IF EXISTS kickstarter;

CREATE TABLE kickstarter (
	id varchar(25),
	name varchar(200),
	category varchar(70),
	main_category varchar(70),
	pledged real,
	state varchar(50),
	backers real,
	country varchar(10),
	usd_pledged_real real,
	usd_goal_real real
)


COPY kickstarter
FROM 'C:\tmp\kickstarter.csv' DELIMITER ',' CSV HEADER encoding 'windows-1251';