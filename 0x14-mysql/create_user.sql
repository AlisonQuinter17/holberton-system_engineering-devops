-- Create a MySQL user named holberton_user.
-- holberton_user has permission to check the primary/replica status of your databases.
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON * . * TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
