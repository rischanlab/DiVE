


DROP TABLE IF EXISTS weather_au;

CREATE TABLE weather_au (
	Tanggal date,
	Location varchar(25),
	MinTemp real,
	MaxTemp real,
	Rainfall real,
	WindGustDir varchar(17),
	WindGustSpeed real,
	WindDir9am varchar(17),
	WindDir3pm varchar(17),
	WindSpeed9am real,
	WindSpeed3pm real,
	Humidity9am real,
	Humidity3pm real,
	Pressure9am real,
	Pressure3pm real,
	Temp9am real,
	Temp3pm real,
	RainToday varchar(17),
	RISK_MM real,
	RainTomorrow varchar(17)
)

INSERT INTO weather_au (Tanggal,Location,MinTemp,MaxTemp,Rainfall,WindGustDir,WindGustSpeed,WindDir9am,WindDir3pm,WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Temp9am,Temp3pm,RainToday,RISK_MM,RainTomorrow)
VALUES


COPY sample_table
FROM 'C:\tmp\sample_data.csv' DELIMITER ',' CSV HEADER;