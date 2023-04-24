# your commands herer
CREATE DATABASE app_server;
show databases;
use app_server;
show databases;

CREATE TABLE user_profile(

    user_name VARCHAR(255), 

    user_id INT NOT NULL PRIMARY KEY,
    
    user_instagram_connection VARCHAR(255),
    
    user_custom_id VARCHAR(255),
    
    user_email VARCHAR(255), 
    
    user_password VARCHAR(255), 
    
    user_location VARCHAR(255),
    
    user_study_time DATETIME,

    is_user_studying BOOLEAN,

    json_object NVARCHAR(4000)

    );
    
CREATE TABLE friend_list(

    user_id INT NOT NULL,
    
    friend_id INT NOT NULL,
    
    friend_relation ENUM('1 friend 2' , '2 friend 1', 'friend both', '1 block 2', '2 block 1', 'block both' ),

    CONSTRAINT relationship PRIMARY KEY(user_id, friend_id), 
    
    CHECK(user_id < friend_id)

    );



