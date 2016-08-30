drop table if exists Tasks;

create table Tasks(
     tasks_id integer primary key autoincrement,
     name text not null,
     shot text not null,
     seq text not null,
     reel text not null,
     start_date text not null,
     end_date text not null,
     duration text not null

);

create table WorkFlow(
     id integer primary key autoincrement,
     status text not null,
     date text not null, 
     tasks_id integer,
     FOREIGN KEY (tasks_id) REFERENCES Tasks(tasks_id)
);