CREATE USER preo WITH PASSWORD 'preodator';
GRANT ALL PRIVILEGES ON DATABASE preodator to preo;

CREATE DATABASE preodator;

CREATE TABLE users(
  "userID" SERIAL,
  "DNI" INTEGER,
  "name" TEXT,
  "phone" INTEGER,
  "email" TEXT,
  "create_at" TIMESTAMP,
  primary key ("userID")
);

CREATE TABLE receipts(
  "receiptID" SERIAL,
  "userID" INTEGER,
  "create_at" TIMESTAMP,
  primary key ("receiptID")
);

CREATE TABLE redemptions(
  "redemptionID" SERIAL,
  "userID" INTEGER,
  "rewardID" INTEGER,
  "create_at" TIMESTAMP,
  primary key ("redemptionID")
);

CREATE TABLE rewards(
  "rewardID" SERIAL,
  "name" TEXT,
  "price" NUMERIC,
  primary key ("rewardID")
);

CREATE TABLE venues(
  "venueID" SERIAL,
  "name" TEXT,
  "geolocation" TEXT,
  primary key ("venueID")
);
