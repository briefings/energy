
CREATE DATABASE IF NOT EXISTS baseline;

USE baseline;

CREATE TABLE IF NOT EXISTS baseline.country
(
 iso31661alpha2 CHAR(2) NOT NULL UNIQUE PRIMARY KEY COMMENT 'The alpha-2-country-code of a country.  This should be CHAR(2) because the ISO 3166-1 alpha-2 codes are always 2 letter codes.',
 iso31661alpha3 CHAR(3) NOT NULL UNIQUE,
 country_code SMALLINT NOT NULL UNIQUE,
 region_code SMALLINT NOT NULL,
 continent_code SMALLINT NOT NULL,
 country_eng VARCHAR(1023) NOT NULL,
 region_eng VARCHAR(255),
 continent_eng VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS baseline.internal_geography
(
 iso31661alpha2 char(2) NOT NULL UNIQUE COMMENT 'The alpha-2-country-code of a country.',
 region_code SMALLINT NOT NULL,
 region_name VARCHAR(1023) NOT NULL,
 FOREIGN KEY (iso31661alpha2) REFERENCES baseline.country (iso31661alpha2)
);

CREATE TABLE IF NOT EXISTS baseline.wesp
(
 iso31661alpha2 CHAR(2) NOT NULL UNIQUE COMMENT 'The alpha-2-country-code of a country.',
 wesp_code SMALLINT NOT NULL COMMENT 'This consists of three distinct codes for the three broad categories of World Economic Situation and Prospects',
 wesp_name VARCHAR(63) NOT NULL COMMENT 'Developed, Transitioning, Developing Economies',
 income_level_code SMALLINT NOT NULL,
 income_level_name VARCHAR(31) NOT NULL COMMENT 'High, Upper Middle, Lower Middle, Low',
 fuel_exporting BOOLEAN NOT NULL DEFAULT FALSE,
 least_developed BOOLEAN NOT NULL,
 heavily_indebted_poor BOOLEAN NOT NULL DEFAULT FALSE,
 small_island_developing BOOLEAN NOT NULL DEFAULT FALSE,
 land_locked_developing BOOLEAN NOT NULL DEFAULT FALSE,
 FOREIGN KEY (iso31661alpha2) REFERENCES baseline.country (iso31661alpha2)
);
