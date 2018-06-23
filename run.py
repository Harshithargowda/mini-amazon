from flask import Flask, request,jsonify,send_from_directory


app = Flask('Amazon')

products=[]


@app.route('/', methods=['GET'])
def index():
    print("index")
    return send_from_directory('static', 'index.html')


@app.route('/amazon/product', methods=['GET', 'POST'])
def amzprod():
    if request.method == 'GET':
        query=request.args['name']
        for prod in products:
            if prod['name']== query:
                return jsonify(prod)
        return 'No_products'


    elif request.method == 'POST':
        if request.form['op_type'] == "add":
            name = request.form['name']
            desc = request.form['desc']
            price = request.form['price']
            prob={'name':name,
                  'desc':desc,
                  'price':price
                  }
            products.append(prob)
            return send_from_directory('static','index.html')

        else:
            if request.form['op_type'] == "update":
                for prod in products:
                    if request.form['name'] == prod['name']:
                        prod['desc'] = request.form['desc']
                        prod['price'] = request.form['price']
                        return jsonify(prod)

                return "no product found"





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5005)
