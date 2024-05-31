from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
  return render_template('index.html')

@app.route('/about',methods=['GET','POST'])
def about():
  return render_template('about.html')

@app.route('/food',methods=['GET','POST'])
def food():
  return render_template('food.html')

@app.route('/accessories',methods=['GET','POST'])
def accessories():
  return render_template('accessories.html')

if __name__ == '__main__':
  #DEBUG is SET to TRUE. CHANGE FOR PROD
  app.run(port=5000,debug=True)