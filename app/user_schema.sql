drop table if exist Users;
create table Users(
    id integer primary key not null,
    login text,
    password text,
    first_name text,
    last_name text
);