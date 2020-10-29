-- SQLite
SELECT *
FROM record r 

select * from question

delete from question

select * from skill

delete from skill

select * from category

INSERT INTO 'skill' ( skill)
VALUES ('test');

alter table question add column skillid integer

update question set explain = 'test explain'

select * from user

-- SQLite
INSERT INTO `question` ( question, answer, level, questiontype)
VALUES ('math_2_001.png','E',1,'geometry');


SELECT qid, question, answer
FROM question q  LEFT join (select * from record where userid = 3 and result <> 1) r on  q.qid = r.questionid 
where r.questionid is NULL

insert into record(userid,questionid)
select 4,qid from question
where qid <> 100

 where questionid IN (13,100, 78)
P
select * from record where userid =4