@app.route('/calculate', methods = ['POST','GET'])
def calculate():
    if request.method == 'GET':
        val1 = request.args.get('val1')
        val2 = request.args.get('val2')
    print(val1)
    return val1

@app.route('/', methods = ['POST','GET'])
def hello():
    f=open("index.html", 'r')
    val1 = request.args.get('val1')
    print(val1)
    return f