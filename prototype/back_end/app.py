from flask import Flask,request,render_template,jsonify
import datetime
import mysql.connector
app = Flask(__name__)

@app.route('/')
def hello_world():
    response = jsonify({'test': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
#    return render_template('index.html')
# app.add_url_rule('/', 'hello', hello_world)这个是重定向  就是把hello这个路由映射成/，所以你看上去没变化

def get_conn():
    # 这里是通过pymysql这个第三方库（一般是别人写好共享出来，便于而大家使用的工具方法，有兴趣可以看他的源码）
    return mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='Hikeleftstation12', database='app_server')
    
def add_user(user_name, user_id, user_instagram_connection, user_custom_id, user_email,  user_password, user_location, user_study_time, is_user_studying, json_object):
    db = get_conn()

    cursor = db.cursor()

    # adding users to profile 

    sql = ('''INSERT INTO user_profile(user_name, user_id, user_instagram_connection, user_custom_id, user_email, user_password,user_location, user_study_time, is_user_studying ,json_object) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''')

    val = (user_name, user_id, user_instagram_connection, user_custom_id,user_email,user_password, user_location, user_study_time, is_user_studying, json_object )

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

    db = get_conn()

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
    # 
    # Input user id to return all user relationships 
    #
    db = get_conn()

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
    #
    # returns user info in a list
    #

    db = get_conn()

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
    # input user info to remove user 

    db = get_conn()

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

def change_user_info(user_id,user_name = None, user_instagram_connection = None, user_custom_id= None , user_email = None,  user_password = None , user_location = None, user_study_time = None , is_user_studing = None, json_object = None  ): 
   # Input user id and what you would like to change to update user info
    
   ls = [user_name ,user_instagram_connection, user_custom_id, user_email,  user_password, user_location, user_study_time, is_user_studing, json_object ]
   lss = ["user_name", "user_instagram_connection", "user_custom_id", "user_email", "user_password", "user_location", "user_study_time", "is_user_studying" ,"json_object" ]
   for num in range(len(ls)): 
        if ls[num] != None: 

            db = get_conn()

            cursor = db.cursor()

            # adding users to profile 
            print(lss[num])
            query1 = "UPDATE user_profile SET %s = '%s'  WHERE user_id = %s ;" % (lss[num],ls[num],user_id) 
        
            
            cursor.execute(query1)

            db.commit()

            cursor.close()

            db.close()


def change_friend_status(user_id,friend_id,friend_relation): 
        # insert user_id, friend_id, and Friend_relation to update current existing relationships 
        db = get_conn()
        cursor = db.cursor()

        # adding users to profile 

        query1 = '''UPDATE friend_list SET friend_relation = '%s' WHERE user_id = %s AND friend_id = %s;''' % (friend_relation,user_id,friend_id) 
        
        cursor.execute(query1)

        db.commit()

        cursor.close()

        db.close()


@app.route('/add_friend', methods=['POST'])
def add_friend_route():
    friend_data = request.get_json()
    add_friend(
        friend_data['user_id'],
        friend_data['friend_id'],
        friend_data['friend_relation']
    )
    return jsonify({"message": "Friend added successfully"}), 201

@app.route('/add_user', methods=['POST'])
def add_user_route():
    user_data = request.get_json()
    add_user(
        user_data['user_name'],
        user_data['user_instagram_connection'],
        user_data['user_custom_id']
    )
    return jsonify({"message": "User added successfully"}), 201

# @app.route('/find_all_friends/<int:user_id>', methods=['GET'])
# def find_all_friends_route(user_id):
#     friends = find_all_friends(user_id)
#     return jsonify(friends)

#
# @app.route('/remove_user/<int:user_id>', methods=['DELETE'])
# def remove_user_route(user_id):
#     remove_user(user_id)
#     return jsonify({"message": "User removed successfully"}), 200

@app.route('/find_all_friends/<int:user_id>', methods=['GET'])
def find_all_friends_route(user_id):
    friends = find_all_friends(user_id)
    return jsonify(friends)


@app.route('/update_user/<int:user_id>', methods=['POST'])
def update_user_route(user_id):
    user_name = request.json.get('user_name')
    user_instagram_connection = request.json.get('user_instagram_connection')
    user_custom_id = request.json.get('user_custom_id')
    user_email = request.json.get('user_email')
    user_password = request.json.get('user_password')
    user_location = request.json.get('user_location')
    user_study_time = request.json.get('user_study_time')
    is_user_studying = request.json.get('is_user_studying')
    json_object = request.json.get('json_object')

    try:
        change_user_info(user_id, user_name, user_instagram_connection, user_custom_id, user_email, user_password,
                         user_location, user_study_time, is_user_studying, json_object)
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    
@app.route('/update_user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    user_name = request.json.get('user_name')
    user_instagram_connection = request.json.get('user_instagram_connection')
    user_custom_id = request.json.get('user_custom_id')
    user_email = request.json.get('user_email')
    user_password = request.json.get('user_password')
    user_location = request.json.get('user_location')
    user_study_time = request.json.get('user_study_time')
    is_user_studying = request.json.get('is_user_studying')
    json_object = request.json.get('json_object')

    change_user_info(user_id, user_name, user_instagram_connection, user_custom_id, user_email, user_password,
                     user_location, user_study_time, is_user_studying, json_object)
    return jsonify({'status': 'success'}), 200


@app.route('/login')
def login():
   username = request.form.get("username")
   pass

@app.route('/submit')
def submit():
   address = request.form.get("address")
   studytime = request.form.get("studytime")
   pass

add_user("spencer", "3","swag","spencedawg","@gmail","hello123","mugar","1000-01-01 00:00:00", True,'{"name":"John", "age":30, "car":null}'  )
add_user("bowen",2,"rags","boatbowen",'@yahoo.com',"not a password","questrom","1000-01-01 00:00:00", False, '{"name":"John", "age":30, "car":null}' )
add_user("jared",4,"haoisdjf","aphajared","@verizon","securepassword","GSU","1000-01-01 00:00:20", True, '{"name":"John", "age":30, "car":null}')


if  __name__ == '__main__':
    app.run()


# my hero: https://stackoverflow.com/questions/26980713/solve-cross-origin-resource-sharing-with-flask
