DROP TABLE IF EXISTS student;

CREATE TABLE student (
	school varchar(250),
	sex varchar(50),
	age real,
	address varchar(100),
	family_size varchar(200),
	living_status varchar(200),
	mother_edu varchar(200),
	father_edu varchar(200),
	mother_job varchar(200),
	father_job varchar(200),
	reason_here varchar(200),
	guardian varchar(50),
	traveltime varchar(200),
	studytime varchar(200),
	failures varchar(200),
	school_support varchar(100),
	family_edu_support varchar(100),
	extra_paid varchar(100),
	extracurricular varchar(100),
	nursery varchar(100),
	want_continue_study varchar(100),
	internet_at_home varchar(100),
	has_relationship varchar(100),
	family_relationship varchar(100),
	free_time varchar(100),
	going_out varchar(100),
	workday_alcohol varchar(100),
	weekend_alcohol varchar(100),
	curr_health_status varchar(100),
	absences real,
	first_grade real,
	second_grade real,
	final_grade real
)


COPY student
FROM 'C:\tmp\student.csv' DELIMITER ',' CSV HEADER;


UPDATE 
   student
SET 
   school = REPLACE (
   school,
 'GP',
 'Staten_Island'
   );

less than 2 hours
2 to 5 hours
5 to 10 hours
more than 10 hours




UPDATE 
   student
SET 
   studytime = REPLACE (
   studytime,
 '2',
 '2 to 5 hours'
   );

UPDATE 
   student
SET 
   studytime = REPLACE (
   studytime,
 '1',
 'less than 2 hours'
   );
   
UPDATE 
   student
SET 
   studytime = REPLACE (
   studytime,
 '3',
 '5 to 10 hours'
   );

UPDATE 
   student
SET 
   studytime = REPLACE (
   studytime,
 '4',
 'more than 10 hours'
   );