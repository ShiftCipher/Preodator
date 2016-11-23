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
  foreign key ("userID") references
  users("userID")
);

CREATE TABLE redemptions(
  "redemptionID" SERIAL,
  "userID" INTEGER,
  "rewardID" INTEGER,
  "create_at" TIMESTAMP,
  primary key ("redemptionID")
  foreign key ("userID") references
  users("userID")
  foreign key ("rewardID") references
  rewards("rewardID")
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
  "x" TEXT,
  "y" TEXT,
  "z" TEXT,
  primary key ("venueID")
);
