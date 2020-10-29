
INSERT INTO `records` (userid, testid, questionid, createdate, result)
VALUES
(1,20200922222103,2,'2020-09-22',0);


INSERT INTO `records` (userid, testid, questionid, createdate, result)
VALUES
(1,20200922222103,2,'2020-09-22',1);



select * from records

CREATE table users  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    level INTEGER,
    age INTEGER,
    gender TEXT,
    datejoined DATETIME,
    active INTEGER
)


CREATE table questions  (
    qid INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    anwer TEXT NOT NULL,
    explain TEXT,
    level INTEGER,
    type TEXT,
    datecreated DATETIME,
    active INTEGER
)


INSERT INTO
users (firstname,lastname,username,password,level, age, gender,
datejoined,active)
VALUES
('Luna','Mulas','luna','test',0,9,'female','2020-09-09', 1),
('Erika','Zhuang','erika','test',0,29,'female','2020-09-09', 1)

select * from users



delete from questions where qid = 332

ALTER TABLE questions ADD COLUMN explain

select * from users

select * from records where userid = 1

update records set result = -1 where result = 0

select * from questions order by qid desc
