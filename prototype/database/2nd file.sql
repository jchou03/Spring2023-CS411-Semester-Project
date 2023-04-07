# your commands herer
CREATE DATABASE app_server;
show databases;
use app_server;
show databases;

CREATE TABLE user_profile(

    user_name VARCHAR(255), 

    user_id INT NOT NULL PRIMARY KEY,
    
    user_instagram_connection VARCHAR(255),
    
    user_custom_id VARCHAR(255)
    
 --   user_study_time DATETIME
    );
    
CREATE TABLE friend_list(

    user_id INT NOT NULL,
    
    friend_id INT NOT NULL,
    
    friend_relation ENUM('1 friend 2' , '2 friend 1', 'friend both', '1 block 2', '2 block 1', 'block both' ),

    
    CONSTRAINT relationship PRIMARY KEY(user_id, friend_id), 
    
    CHECK(user_id < friend_id)

    );


    

INSERT INTO user_profile(user_name, user_id, user_instagram_connection, user_custom_id) 
-- 1000-01-01 00:00:00'
VALUES ('Spencer', 1, 'zuck.com','spencedawg'); 

-- ENUM('1 friend 2' , '2 friend 1', 'friend both', '1 block 2', '2 block 1', 'block both' )
INSERT INTO friend_list(user_id, friend_id, friend_relation) 

VALUES ( 2, 4, '1 friend 2'); 



-- SELECT s.user_name, d.destination_name, m.description 
-- FROM  user_profile s,destinations d, missions m 
-- WHERE s.sid = m.sid and d.did = m.did; 

-- SELECT s.user_id from user_profile s;

-- SELECT s.user_name, d.destination_name 
-- FROM  user_profile s,destinations d 

SELECT * From friend_list 


