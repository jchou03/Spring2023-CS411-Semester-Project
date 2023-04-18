from flask import Flask,request,render_template,jsonify
import pymysql
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')
# app.add_url_rule('/', 'hello', hello_world)这个是重定向  就是把hello这个路由映射成/，所以你看上去没变化

def get_conn():
    # 这里是通过pymysql这个第三方库（一般是别人写好共享出来，便于而大家使用的工具方法，有兴趣可以看他的源码）
    return pymysql.connect(host="127.0.0.1", user="root", password="bw20011215", database="space_missions", port=3306,
                           charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


def add_user(user_name, user_instagram_connection, user_custom_id):
    db = get_conn()
    cursor = db.cursor()

    sql = (
        '''INSERT INTO user_profile(user_name,  user_instagram_connection, user_custom_id) VALUES (%s,  %s, %s)''')
    val = (user_name,  user_instagram_connection, user_custom_id)

    cursor.execute(sql, val)
    db.commit()

    print(cursor.rowcount, "record inserted.")
    cursor.close()
    db.close()


def add_friend(user_id, friend_id, friend_relation):
    db = get_conn()
    cursor = db.cursor()

    sql = ('''INSERT INTO friend_list(user_id, friend_id, friend_relation) VALUES (%s, %s, %s)''')
    val = (user_id, friend_id, friend_relation)

    cursor.execute(sql, val)
    db.commit()

    print(cursor.rowcount, "record inserted.")
    cursor.close()
    db.close()

def find_all_friends(user_id):
    db = get_conn()
    cursor = db.cursor()

    query = ('''SELECT * FROM friend_list WHERE user_id = %s OR friend_id = %s;''' % (user_id, user_id))
    # 这里其实跟调用方法一样 ， execute就是方法名 只不过这个方法是cursor的
    # cursor1 = new cursor1()
    # cursor1.execute(sql)
    cursor.execute(query)

    ls = []

    for info in cursor:
        ls.append(info)

    cursor.close()
    db.close()
    return ls

def find_user(user_id):
    db = get_conn()
    cursor = db.cursor()

    query = ('''SELECT * FROM user_profile WHERE user_id = %s;''' % (user_id))
    cursor.execute(query)

    ls = []

    for info in cursor:
        ls.append(info)

    cursor.close()
    db.close()
    return ls

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







@app.route('/login')
def login():
   username = request.form.get("username")
   pass

#这就是从前端获取参数，地址时间+当前用户，一起保存到数据库
@app.route('/submit')
def submit():
   address = request.form.get("address")
   studytime = request.form.get("studytime")
   #获取当前用户，然后一起保存到数据库，后面自己完善一下，再返回给前端是否成功的消息
   pass

# 可以先写这块逻辑




# 这个是flask框架的入口方法，
# 相当于你双击了一个应用,你点的桌面上这些应用图标就相当于执行了这个命令，只是每个应用命令不一样而已，这个能懂吧

# 每个带@app.route的方法，都是你对外暴露的方法，提供给别人调用的，不管是前端还是服务端都可以调用，但是要确保别人能访问到你的电脑，
# 你可以返回数据return jsonify(result)，也可以返回页面return render_template('index.html')
# def get_conn(): 这个方法就是创建一个数据库链接，等于将你这个应用和数据库搭了一个桥梁，你可以通过这个桥梁从数据库里拿数据
if __name__ == '__main__':
   app.run()