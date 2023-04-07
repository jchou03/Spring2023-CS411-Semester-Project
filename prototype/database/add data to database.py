

import datetime
import mysql.connector


def add_user(user_name, user_id, user_instagram_connection, user_custom_id, user_email,  user_password, user_location, user_study_time):
    db = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='Hikeleftstation12', database='app_server')

    cursor = db.cursor()

    # adding users to profile 

    sql = ('''INSERT INTO user_profile(user_name, user_id, user_instagram_connection, user_custom_id, user_email, user_password,user_location, user_study_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''')

    val = (user_name, user_id, user_instagram_connection, user_custom_id,user_email,user_password, user_location, user_study_time)

    cursor.execute(sql,val)


    db.commit()

    print(cursor.rowcount, "record inserted.")

    cursor.close()

    db.close()

#ENUM('1 friend 2' , '2 friend 1', 'friend both', '1 block 2', '2 block 1', 'block both' )

def add_friend(user_id, friend_id, friend_relation):
    # RULES 
    # USER_id > friend_id 
    # no two of the same records 

    db = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='Hikeleftstation12', database='app_server')

    cursor = db.cursor()

    # adding users to profile 

    sql = ('''INSERT INTO friend_list(user_id, friend_id, friend_relation)  VALUES (%s, %s, %s)''')

    val = (user_id, friend_id, friend_relation)
    
    cursor.execute(sql,val)

    db.commit()

    print(cursor.rowcount, "record inserted.")

    cursor.close()

    db.close()

def find_all_friends(user_id):
    db = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='Hikeleftstation12', database='app_server')

    cursor = db.cursor()

    # adding users to profile 

    query  = ('''SELECT * FROM friend_list WHERE user_id = %s OR friend_id = %s ;''' % (user_id,user_id) )
    
    cursor.execute(query)

    ls = []

    for info in cursor: 
        print(type(info))
        ls.append(info)

    cursor.close()

    db.close()
    return ls

def find_user(user_id): 
    db = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='Hikeleftstation12', database='app_server')

    cursor = db.cursor()

    # adding users to profile 

    query  = ('''SELECT * FROM user_profile WHERE user_id = %s;''' % (user_id) )
    
    cursor.execute(query)

    ls = []

    for info in cursor: 
        print(type(info))
        ls.append(info)

    cursor.close()

    db.close()
    return ls

def remove_user(user_id):
    db = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='Hikeleftstation12', database='app_server')

    cursor = db.cursor()

    # adding users to profile 

    query1  = ('''DELETE FROM friend_list WHERE user_id = %s OR friend_id = %s ;''' % (user_id,user_id) )
    
    query2  = ('''DELETE FROM user_profile WHERE user_id = %s;''' % (user_id) )
    
    cursor.execute(query1)

    db.commit()

    cursor.execute(query2)

    db.commit()

    cursor.close()

    db.close()

def change_user_info(user_id,user_name = None, user_instagram_connection = None, user_custom_id= None , user_email = None,  user_password = None , user_location = None, user_study_time = None ): 
    ls = [user_name ,user_instagram_connection, user_custom_id, user_email,  user_password, user_location, user_study_time]
    lss = ["user_name", "user_instagram_connection", "user_custom_id", "user_email", "user_password", "user_location", "user_study_time"]
    for num in range(len(ls)): 
        if ls[num] != None: 

            #sql = ('''UPDATE user_profile SET %s = %s WHERE user_id = %s VALUES (%s, %s, %s)''')

            print(ls[num], lss[num], user_id)

            
change_user_info ( 1 ,"hat")
#add_friend(1,2,'friend both')
#print(find_all_friends(2))

#remove_user(2)
#print(find_user(2))
#add_friend(3,2,'2 friend 1' )

#add_user("spencer", "3","swag","spencedawg","@gmail","hello123","mugar","1000-01-01 00:00:00" )
#add_user("bowen",2,"rags","boatbowen",'@yahoo.com',"not a password","questrom","1000-01-01 00:00:00" )