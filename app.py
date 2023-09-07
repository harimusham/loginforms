import sqlite3
from flask import Flask,render_template,request, redirect, url_for
app = Flask(__name__)

@app.route('/insertfac-data', methods=['POST','GET'])
def insert_data():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        names = request.form.get('name')
        department = request.form.get('department')
        designation=request.form.get('designation')
        mobile=request.form.get('mobilenumber')
        email=request.form.get('email')
        specification=request.form.get('specification')
        conn = sqlite3.connect('mycampushub.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO facultys (username,password,names, department,designation,mobile,email,specification) VALUES (?,?,?,?,?,?,?,?)', (username,password,names, department,designation,mobile,email,specification))
        conn.commit()
        cursor.close()
        conn.close()
    return render_template('details.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('logins.html')

@app.route("/faculty-login", methods=["POST"])
def flogin():
    username = request.form.get('username')
    password = request.form.get("password")
    connection = sqlite3.connect('mycampushub.db')
    cursor = connection.cursor()
    print(username, password)
    
    # Use parameterized query to prevent SQL injection
    query = "SELECT username, password FROM facultys WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    
    results = cursor.fetchall()
    cursor.close()
    print(results)
    if len(results) == 0:
        print("Please provide valid login details")
    else:
        return render_template('welcome.html')
    
    return redirect(url_for('login'))

@app.route('/insertstu-data', methods=['POST'])
def insertstu_data():
    if  request.method == 'POST':
        username=request.form.get('susername')
        password=request.form.get('spassword')
        name = request.form.get('sname')
        fathername = request.form.get('sfathername')
        mothername=request.form.get('smothername')
        mobilenumber=request.form.get('smobilenumber')
        email=request.form.get('semail')
        course=request.form.get('scourse')
        address=request.form.get('saddress')
        intermarks=request.form.get('sintermarks')
        aadharnumber=request.form.get('saadharnumber')
        conn = sqlite3.connect('mycampushub.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (username,password,name,fathername,mothername,mobilenumber,email,course,address,intermarks,aadharnumber) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (username,password,name,fathername,mothername,mobilenumber,email,course,address,intermarks,aadharnumber))
        conn.commit()
        cursor.close()
        conn.close()
    return render_template('studentdetails.html')

@app.route('/student-login',methods=['POST'])
def stulogin():
    if request.method == 'POST':
        username=request.form.get("username")
        password=request.form.get("password")
        connection=sqlite3.connect('mycampushub.db')
        cursor=connection.cursor()
        print(username,password)
        query = "SELECT * FROM students WHERE username = ? AND password = ?"
        # query="SELECT username,password FROM students where  username="+username+" password="+password+";"
        cursor.execute(query, (username, password))
        results=cursor.fetchall()
        print(results)
        cursor.close()
        if(len(results)==0):
            print("please provide valid login details")
        else:
            return render_template('welcomestudent.html')
    return redirect(url_for('login'))


@app.route('/parent-login',methods=['GET','POST'])
def parentLogin():
    if request.method == 'POST':
        username=request.form.get("username")
        password=request.form.get("password")
        connection=sqlite3.connect('mycampushub.db')
        cursor=connection.cursor()
        print(username,password)
        query = "SELECT * FROM students WHERE username = ? AND password = ?"
        # query="SELECT username,password FROM students where  username="+username+" password="+password+";"
        cursor.execute(query, (username, password))
        results=cursor.fetchall()
        print(results)
        cursor.close()
        if(len(results)==0):
            print("please provide correct parent login details")
        else:
            return render_template('welcomeparent.html',name=username)
    return redirect(url_for('login'))



          
if __name__ == '__main__':
    app.run(debug=True) 