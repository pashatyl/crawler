CREATE TABLE edges (
    v1 VARCHAR NOT NULL,
    v2 VARCHAR NOT NULL
);

CREATE TABLE pages (
    id VARCHAR PRIMARY KEY,
    path VARCHAR NOT NULL
);

CREATE TABLE processed (
    id VARCHAR
) WITHOUT ROWID;
