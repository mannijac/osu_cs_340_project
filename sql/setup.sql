CREATE OR REPLACE DATABASE 'cartridge_collector';
SHOW DATABASES;
CREATE USER 'cs340' IDENTIFIED BY 'collector';
SELECT User FROM mysql.user;
GRANT ALL PRIVILEGES ON cartridge_collector.* TO 'cs340';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'cs340';