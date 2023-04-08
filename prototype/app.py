from flask import Flask,request,render_template,jsonify
app = Flask(__name__)




@app.route('/')
def hello_world():
   return render_template('index.html')
# app.add_url_rule('/', 'hello', hello_world)这个是重定向  就是把hello这个路由映射成/，所以你看上去没变化


# 后面你就在这里定义各种接口，然后写对应的业务逻辑，后面你要看怎么从前端获取传过来的参数，通过这个对象，form是获取表单，args是参数（url上），json是json格式的参数
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
@app.route('/query')
def query_friend():
   result = {
      'code':200,
      'msg':'请求成功'
   }

   #我先构造一个加的数据，后面需要从数据库拿
   #返回这样的数据前端就可以调用你这个接口了
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