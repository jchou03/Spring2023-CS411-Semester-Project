import facebook

# 设置应用程序 ID 和应用程序密钥
app_id = '135421432654185'
app_secret = 'cd832c0093d0dff304eda3058e58ee31'
access_token = app_id + '|' + app_secret


# 获取用户访问令牌
def get_access_token(code):
    graph = facebook.GraphAPI()
    token = graph.get_access_token_from_code(
        code, redirect_uri='https://jchou03.github.io/Spring2023-CS411-Semester-Project/', app_id=app_id, app_secret=app_secret)
    return token


# 获取用户信息
def get_user_info(token):
    graph = facebook.GraphAPI(access_token=token, version='3.0')
    user = graph.get_object('me', fields='id,name,email')
    return user


# 在登录后的回调中处理用户登录
def handle_login(request):
    code = request.GET.get('code', '')
    token = get_access_token(code)
    user = get_user_info(token)
    # 在此处处理用户登录逻辑
    return user
