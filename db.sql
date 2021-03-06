CREATE TABLE users(
  "id" SERIAL PRIMARY KEY,
  "data" JSONB,
  "create_at" TIMESTAMP default current_timestamp
);

CREATE TABLE admins(
  "id" SERIAL PRIMARY KEY,
  "data" JSONB,
  "create_at" TIMESTAMP default current_timestamp
);

CREATE TABLE campaigns(
  "id" SERIAL PRIMARY KEY,
  "data" JSONB,
  "create_at" TIMESTAMP default current_timestamp
);

CREATE TABLE rewards(
  "id" SERIAL PRIMARY KEY,
  "data" JSONB,
  "create_at" TIMESTAMP default current_timestamp
);

CREATE TABLE venues(
  "id" SERIAL PRIMARY KEY,
  "data" JSONB,
  "create_at" TIMESTAMP default current_timestamp
);

CREATE TABLE receipts(
  "id" SERIAL PRIMARY KEY,
  "user_id" INTEGER,
  "create_at" TIMESTAMP default current_timestamp,
  FOREIGN KEY ("user_id") references users("id")
);

CREATE TABLE redemptions(
  "id" SERIAL PRIMARY KEY,
  "user_id" INTEGER,
  "reward_id" INTEGER,
  "position" JSONB,
  "create_at" TIMESTAMP default current_timestamp,
  FOREIGN KEY ("user_id") references users("id"),
  FOREIGN KEY ("reward_id") references rewards("id")
);
