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
   # add_user is a function that allows us to add users to our database 
   # the User_id is our primary key and each entry must have a unique user_id 
   # while every other entry is optional, but please fill it in plz pretty plz 
   # -Spencer Yeh 
   # 
   # Donham Fun Fact: the Rafik B. Hariri where Questrom is located is named after the Former Prime Minister of Lebanon.
   # Hariri was accused of corruption that plagued Lebanon during the Syrian occupation. Among the allegations made against him was that
   # his wealth grew from less than $1 billion when he was appointed prime minister in 1992, to over $16 billion when he died.
    
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



def add_friend(user_id, friend_id, friend_relation):
    # this function adds user relationships to our user Friend List 
    # below are a few rules how our friends list works 
    #
    # 1. There are 6 options for a friend relation,  
    #'1 friend 2' , '2 friend 1', 'friend both', '1 block 2', '2 block 1', 'block both'
    # 
    # 2. USER_id > friend_id 
    # the user_id must be larger than friend_id therefore we get no duplicates 
    # 
    # in theory user_id can equal friend_id, but dont be stupid and do that 
    # 
    # - Spencer Yeh 
    # 
    # Donham Fun Fact: The Yawkey building in Kenmore is named after Thomas Yawkey president of the Boston Red Sox in 1933 for 44 seasons 
    # The Red Sox were the first MLB team to sign a Mexican-born player, fielding Mel Almada on September 8, 1933. However, they were 
    # the last major league team to add a black player to their roster allegedly due to Yawkey and the managers he hired being racists. 
    # These claims have been disputed by some journalists and researchers. In his biography of Yawkey, Bill Nowlin states that there is 
    # no evidence that Yawkey ever made a racist statement or was "personally racist." Furthermore, a 2006 article in The Boston Globe 
    # commented that Yawkey "was not overtly racist, but members of his inner circle were."

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

def find_user(user_id): 
    # This function allows us to find a user in the user profile list and returns their info in a list which in than is a in a tuple. 
    # Enter a user_id that does exist, or else it will give an error/not return anything 
    # 
    # - Spencer Yeh 
    # 
    # Donham Fun Fact: Jon Westling was the Eighth President of Boston University from 1996 - 2002. 
    # During the Court Case, Guckenberger v. Boston University, he was accused of making controversial statements 
    # about students with learning disabilities. "President Westling referred to students with learning disabilities as "a plague," 
    # and an indication of "a silent genetic catastrophe," and he has made similar statements in letters to the New York Times, 
    # the Boston Globe, campus newspapers, and students' parents.

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


def find_all_friends(user_id):
    # This function finds all the friends a certain user has, if they have any
    #
    # Input the user id and it will output a list of tuples of all the friends and their relationship status  
    # Hopefully pretty simple 
    #
    # -Spencer Yeh 
    #
    # Donham Fun Fact: The Law building was named after Sumner M Redstone was an American billionaire businessman and media magnate. 
    # He was the founder and chairman of the second incarnation of Viacom, chairman of CBS Corporation,and the majority owner and chairman
    # of the National Amusements theater chain. He also taught law at BU for a bit. 
    # In July 2010, Redstone was caught on tape trying to find the source of an apparently embarrassing leak within MTV.
    # Redstone offered money and protection to a journalist if he would give up his source. Redstone had been pushing MTV 
    # management to give more airtime to the band the Electric Barbarellas. On the message, Redstone tells the reporter that 
    # "we're not going to kill" the source, adding "We just want to talk to him". The 87-year-old Redstone also told the reporter 
    # he would be "well rewarded and well protected" if he would reveal the source. 

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


def find_all_friends_with_user_info(user_id):
    # This function finds all the friends a certain user has, if they have any, and returns their user info into a list 
    #
    # Input the user id and it will output a list of tuples of all their friends info from user_profile 
    # Hopefully pretty simple 
    #
    # -Spencer Yeh 
    #
    # Donham Fun Fact: 

    db = get_conn()

    cursor = db.cursor()

    # adding users to profile 

    query  = ('''SELECT * FROM friend_list WHERE user_id = %s OR friend_id = %s ;''' % (user_id,user_id) )
    
    cursor.execute(query)
    
    ls = []

    for info in cursor: 
        ls.append(info)
    
    # this loop allows us to collect a list of unique friendds it could be combined but im lazy 
     
    lss = []
    for i in ls: 
        if(i[0] != user_id):
            lss.append(i[0])
        else: 
            lss.append(i[1])


    # this loop uses the find user function and allows us to get all of our user info and put it into a list 

    deets = [] 
    for i in lss: 
        temp = find_user(i)
        deets.append(temp[0])
    cursor.close()
    db.close()
    return deets 
    # looking for a nutty joke 

def remove_user(user_id):
    # input existing user_id to remove user from both friends list and user_list.   
    # 
    # -Spencer Yeh 
    # 
    # Donham Fun Fact: John Silber was the seventh president of Boston University. In 2002, Silber ordered that the Boston University Academy, 
    # a prep school operated by BU, disband its gay–straight alliance, a student club that staged demonstrations to publicize the 
    # deleterious effects of homophobia. Silber dismissed the stated purpose of the club—to serve as a support group for gay students 
    # and to promote tolerance and understanding between gay and straight students—accusing the club of being a vehicle for 
    #"homosexual recruitment." Silber denounced the group for "evangelism" and "homosexual militancy" with the purpose of promoting gay sex.

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
   # All fields are optional besides user_id
   # this proably could be done eaiser by creating multiple functions for each customized column but that would make this file 10X longer
   # just count carefully 
   # - Spencer Yeh 
   #
   # Donham Fun Fact:  BU is a major research institution seeking knowledge and creating breakthroughs in everything from 
   # African studies 
   #to zebrafish genetics.
    
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
        # please only put in relationships that already exist 
        # - Spencer Yeh 
        #
        # Donham Fun Fact: 
        #  
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
    print("friends " + str(friends))
    response = jsonify(friends)
    print("response" + str(response))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/find_all_friends_with_user_info/<int:user_id>', methods=['GET'])
def find_all_friends_with_user_info_route(user_id):
    print(1)
    friends = find_all_friends_with_user_info(user_id)
    print(str(2) + " the result is: " + str(friends))
    response = jsonify({'data': friends})
    # response = jsonify({'result': 'this is the result'})
    print(3)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

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

# add_user("spencer", 3,"swag","spencedawg","@gmail","hello123","mugar","2023-01-01 00:00:00", True,'{"location":"GSU", "Time":"12:45"}'  )
# add_user("bowen",2,"rags","boatbowen",'@yahoo.com',"not a password","questrom","2023-01-01 00:00:00", False, '{"location":"GSU", "Time":"12:45"}' )
# add_user("jared",4,"haoisdjf","aphajared","@verizon","securepassword","GSU","2023-01-01 00:00:20", True, '{"location":"GSU", "Time":"12:45"}')

#'1 friend 2' , '2 friend 1', 'friend both', '1 block 2', '2 block 1', 'block both'
#add_friend(2,4,'friend both')
#add_friend(3,4,'1 friend 2')

# print(find_all_friends(4))

if  __name__ == '__main__':
    app.run()


# my hero: https://stackoverflow.com/questions/26980713/solve-cross-origin-resource-sharing-with-flask
