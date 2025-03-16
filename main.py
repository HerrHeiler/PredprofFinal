@app.route('/api/ping')
def ping():
    return ({'status':'ok'}, 200)

@app.route('api/business/auth/sign-up', methods=['POST'])
def b2b_sign_up():