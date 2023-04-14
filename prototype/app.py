from flask import Flask,request,render_template,jsonify
app = Flask(__name__)




@app.route('/')
def hello_world():
   return render_template('index.html')
# app.add_url_rule('/', 'hello', hello_world)这个是重定向  就是把hello这个路由映射成/，所以你看上去没变化


\
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
