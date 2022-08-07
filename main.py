from flask import Flask, jsonify, request
app=Flask(__name__)
@app.route("/")
def HelloWorld():
    return "Hello World"
tasks=[
    {
        'Contact':9987644456,
        'Name':'Raju',
        'done':False,
        'id':1
    },
    {
        'Contact':9876543222,
        'Name':'Rahul',
        'done':False,
        'id':2
    }
]
@app.route("/addData", methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status":"ERROR",
            "message":"Plese provide the data"
        }, 400)
    task={
        'Contact':request.json['Contact'],
        'Name':request.json['Name'],
        'done':False,
        'id':tasks[-1]["id"]+1
    }
    tasks.append(task)
    return jsonify({
        'status':"success",
        'message':"Task added successfuly"
    })
@app.route("/getData")
def get():
    return jsonify({
        'data':tasks
    })
if __name__=="__main__":
    app.run()
