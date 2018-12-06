drop table if exists projects;
create table entries (
    id integer primary key autoincrement,
    title string not null,
    text string not null,
    author string not null,
    supervisor string not null,
    image_url string not null,
    url string not null
);
