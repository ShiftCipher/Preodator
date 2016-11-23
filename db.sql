CREATE DATABASE preodator;

\c preodator;

CREATE TABLE users(
  "id" SERIAL,
  "dni" TEXT,
  "name" TEXT,
  "phone" TEXT,
  "email" TEXT,
  "create_at" TIMESTAMP default current_timestamp,
  primary key ("id")
);

CREATE TABLE receipts(
  "id" SERIAL,
  "userid" INTEGER references users("id"),
  "create_at" TIMESTAMP default current_timestamp,
  primary key ("id")
);

CREATE TABLE rewards(
  "id" SERIAL,
  "name" TEXT,
  "price" NUMERIC,
  "create_at" TIMESTAMP default current_timestamp,
  primary key ("id")
);

CREATE TABLE redemptions(
  "id" SERIAL,
  "userid" INTEGER references users("id"),
  "rewardid" INTEGER references rewards("id"),
  "create_at" TIMESTAMP default current_timestamp,
  primary key ("id")
);

CREATE TABLE venues(
  "id" SERIAL,
  "name" TEXT,
  "geolocation" POINT,
  "create_at" TIMESTAMP default current_timestamp,
  primary key ("id")
);
