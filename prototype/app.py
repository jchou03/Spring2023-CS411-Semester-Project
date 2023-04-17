from flask import Flask,request,render_template,jsonify
app = Flask(__name__)




@app.route('/')
def hello_world():
   return render_template('index.html')

#Database connection
def connect_to_db():
    return mysql.connector.connect(
        user='root',
        host='127.0.0.1',
        port=3306,
        password='Hikeleftstation12',
        database='app_server'
    )

#Test version
def add_user(user_name, user_id, user_instagram_connection, user_custom_id):
    db = connect_to_db()
    cursor = db.cursor()

    sql = ('''INSERT INTO user_profile(user_name, user_id, user_instagram_connection, user_custom_id) VALUES (%s, %s, %s, %s)''')
    val = (user_name, user_id, user_instagram_connection, user_custom_id)

    cursor.execute(sql, val)
    db.commit()

    print(cursor.rowcount, "record inserted.")
    cursor.close()
    db.close()
      
      

def add_friend(user_id, friend_id, friend_relation):
    db = connect_to_db()
    cursor = db.cursor()

    sql = ('''INSERT INTO friend_list(user_id, friend_id, friend_relation) VALUES (%s, %s, %s)''')
    val = (user_id, friend_id, friend_relation)

    cursor.execute(sql, val)
    db.commit()

    print(cursor.rowcount, "record inserted.")
    cursor.close()
    db.close()

   
def find_all_friends(user_id):
    db = connect_to_db()
    cursor = db.cursor()

    query = ('''SELECT * FROM friend_list WHERE user_id = %s OR friend_id = %s;''' % (user_id, user_id))
    cursor.execute(query)

    ls = []

    for info in cursor:
        ls.append(info)

    cursor.close()
    db.close()
    return ls

def find_user(user_id):
    db = connect_to_db()
    cursor = db.cursor()

    query = ('''SELECT * FROM user_profile WHERE user_id = %s;''' % (user_id))
    cursor.execute(query)

    ls = []

    for info in cursor:
        ls.append(info)

    cursor.close()
    db.close()
    return ls

@app.route('/add_user', methods=['POST'])
def add_user_route():
    user_data = request.get_json()
    add_user(
        user_data['user_name'],
        user_data['user_id'],
        user_data['user_instagram_connection'],
        user_data['user_custom_id']
    )
    return jsonify({"message": "User added successfully"}), 201
   
 
@app.route('/find_all_friends/<int:user_id>', methods=['GET'])
def find_all_friends_route(user_id):
    friends = find_all_friends(user_id)
    return jsonify(friends)


@app.route('/remove_user/<int:user_id>', methods=['DELETE'])
def remove_user_route(user_id):
    remove_user(user_id)
    return jsonify({"message": "User removed successfully"}), 200


@app.route('/login')
def login():
   username = request.form.get("username")
   pass


@app.route('/submit')
def submit():
   address = request.form.get("address")
   studytime = request.form.get("studytime")
  
   pass


@app.route('/query')
def query_friend():
   result = {
      'code':200,
      'msg':'请求成功'
   }

   
   data = []
   data.append({
      'username':'Jared',
      'address':'GSU',
      'studytime':'11:20'
   })
   data.append({
      'username': 'Spencer',
      'address': 'Questrom',
      'studytime': '1:45'
   })
   data.append({
      'username': 'Bowen',
      'address': 'CDS',
      'studytime': '2:15'
   })
   result['data']= data
   return jsonify(result)

if __name__ == '__main__':
   app.run()
