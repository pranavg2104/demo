from flask import Flask,json,jsonify
  
@app.route("/")
def getEmployeeList():
        # Initialize a employee list
    employeeList = []
        # create a instances for filling up employee list
    for i in range(0,2):
        empDict = {
        'firstName': 'Roy',
        'lastName': 'Augustine'}
        employeeList.append(empDict)
        # convert to json data
        jsonStr = json.dumps(employeeList)
    return jsonify(Employees=jsonStr)
