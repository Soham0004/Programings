create table student (Name varchar(25), RollNo int(3), Discipline varchar(5), Marks int (3), Grade varchar(2));
Insert into student values ('Anil', 1, 'CSE', 86, 'A'),('Rathin', 2, 'CSE', 67, 'B'),('Sikha', 3, 'ECE', 54, 'C'),('Shyamal', 4, 'ECE', 45, 'D'),('Paresh', 5, 'ME', 49, 'D'),('Trisha', 6, 'ME', 64, 'B'),('Rina', 7, 'CSE', 54, 'C'),('Anik', 8, 'ECE', 54, 'C');
Select * from student where marks>50;
