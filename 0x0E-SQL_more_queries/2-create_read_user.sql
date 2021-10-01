-- creates user user_0d_1 
CREATE IF NOT EXISTS USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
GRANT SELECT PRIVILEGES ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;

