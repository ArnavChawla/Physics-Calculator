# -*- coding: utf-8 -*-
import math
import flask
from flask import Flask
from flask import make_response
from flask import render_template, request, send_from_directory
from flask import redirect, Response
from momentum import collision
import xlsxwriter
import os
from flask import request
from flask import jsonify
from kinimatics import kinematics
from flask import Flask, url_for, render_template, request, redirect, session
import requests
from fields import fields
import efields
app = Flask(__name__)



def round_up(number, ndigits=None):
    # start by just rounding the number, as sometimes this rounds it up
    result = round(number, ndigits if ndigits else 0)
    if result < number:
        # whoops, the number was rounded down instead, so correct for that
        if ndigits:
            # use the type of number provided, e.g. float, decimal, fraction
            Numerical = type(number)
            # add the digit 1 in the correct decimal place
            result += Numerical(10) ** -ndigits
            # may need to be tweaked slightly if the addition was inexact
            result = round(result, ndigits)
        else:
            result += 1 # same as 10 ** -0 for precision of zero digits
    return result
class cord():
    def __init__(self,xpos,ypos,time,theta,heightInitial, heightFinal, velocityInitial, timeInterval):
        self.x = xpos
        self.y = ypos
        self.t = time
        self.theta = theta
        self.hi = heightInitial
        self.hf = heightFinal
        self.vi = velocityInitial
        self.ti = timeInterval



        #prompt the users for the theta, the initial height, the final height, the initial velocity, and the time interval in seconds


    def run(self):
        xpos  = []
        ypos = []
        time = []
        yvels = []
        xvels = []
        yaccs = []
        xaccs = []

        g = 9.807
        self.t = 0
        xvel = 0
        yvel = 0
        yacc = g
        xacc = 0
        self.t =0
        self.theta = math.radians(self.theta)
        vInitialY = self.vi * math.sin(self.theta)
        vInitialX = self.vi * math.cos(self.theta)


        a = -.5 * g
        b = vInitialY
        c = self.hi - self.hf
        test = (((math.pow(b, 2) - 4 * a * c)) <0)

        if (test == True):
            return True
        tyMax = round((-1 * b) / (2 * a),3)
        yMax = round((a * math.pow(tyMax, 2) + b * tyMax + c),3)
        xPosYmax = round(vInitialX * tyMax,3)
        endTime = (-1 * b - math.sqrt(math.pow(b, 2) - 4 * a * c))/(2 * a)

        xMax = round(vInitialX * endTime,3)

        while(self.t <= endTime + self.ti):

            p1 = (self.vi* math.sin(self.theta) * self.t)
            p2 = 0.5 * g * (self.t**2)
            p3 = (p1 - p2)+self.hi
            self.y = round(p3,3)
            yvel = (self.vi * math.sin(self.theta)) - (g * self.t)
            yvel = round(yvel, 3)
            yacc = round(-1*g,3)
            self.x = round(vInitialX * self.t,3)
            xvel = round(vInitialX,3)
            xacc = 0





            print("time: {}  x position: {} y position: {} y velocity: {} x velocity: {} y acceleration: {} x acceleration: {}".format(self.t,self.x,self.y,yvel,xvel,yacc,xacc))

            xpos.append(self.x)
            ypos.append(self.y)
            time.append(self.t)
            yvels.append(yvel)
            xvels.append(xvel)
            yaccs.append(yacc)
            xaccs.append(xacc)
            self.t += self.ti
        # df = columnsv2Frame({"Time":time, "X postion": xpos, "Y position":ypos,"Y velocity":yvels,"X velocity": xvels, "Y velocity": yvels, "X acceleration": xaccs, "Y acceleration": yaccs})
        # df.to_excel('test.xlsx',sheet_name='sheet1', index=False)
        workbook = xlsxwriter.Workbook('test.xlsx')
        text_format = workbook.add_format({'text_wrap': True})
        worksheet = workbook.add_worksheet()
        headings = ['Time', 'X Position', 'Y Position', 'X Velocity', "Y Velocity","X acceleration", "Y acceleration"]

        data = [
            time,
            xpos,
            ypos,
            xvels,
            yvels,
            xaccs,
            yaccs
        ]
        worksheet.write_row('A1', headings, text_format)
        worksheet.write_column('A2', data[0], text_format)
        worksheet.write_column('B2', data[1], text_format)
        worksheet.write_column('C2', data[2], text_format)
        worksheet.write_column('D2', data[3], text_format)
        worksheet.write_column('E2', data[4], text_format)
        worksheet.write_column('F2', data[5], text_format)
        worksheet.write_column('G2', data[6], text_format)
        print(len(time))

        chart1 = workbook.add_chart({'type': 'scatter'})
        chart1.add_series({
        'categories': '=Sheet1!$B$2:$B${}'.format(len(time)+1),
        'values':     '=Sheet1!$C$2:$C${}'.format(len(time)+1),
        })
        chart1.set_title ({'name': 'Y Postion Vs X Position'})
        # Add x-axis label
        chart1.set_x_axis({'name': 'X Position (m)'})

        # Add y-axis label
        chart1.set_y_axis({'name': 'Y position (m)'})
        worksheet.insert_chart('I2', chart1)

        chart2 = workbook.add_chart({'type': 'scatter'})
        chart2.add_series({
        'categories': '=Sheet1!$A$2:$A${}'.format(len(time)+1),
        'values':     '=Sheet1!$C$2:$C${}'.format(len(time)+1),
        })
        chart2.set_title ({'name': 'Y Postion Vs Time'})
        # Add x-axis label
        chart2.set_x_axis({'name': 'Time (s)'})

        # Add y-axis label
        chart2.set_y_axis({'name': 'Y position(m)'})
        worksheet.insert_chart('Q2', chart2)

        chart3 = workbook.add_chart({'type': 'scatter'})
        chart3.add_series({
        'categories': '=Sheet1!$A$2:$A${}'.format(len(time)+1),
        'values':     '=Sheet1!$B$2:$B${}'.format(len(time)+1),
        })
        chart3.set_title ({'name': 'X Postion Vs Time'})
        # Add x-axis label
        chart3.set_x_axis({'name': 'Time (s)'})

        # Add y-axis label
        chart3.set_y_axis({'name': 'X position (m)'})
        worksheet.insert_chart('Q20', chart3)

        chart4 = workbook.add_chart({'type': 'scatter'})
        chart4.add_series({
        'categories': '=Sheet1!$A$2:$A${}'.format(len(time)+1),
        'values':     '=Sheet1!$E$2:$E${}'.format(len(time)+1),
        })
        chart4.set_title ({'name': 'Y Velocity Vs Time'})
        # Add x-axis label
        chart4.set_x_axis({'name': 'Time (s)'})

        # Add y-axis label
        chart4.set_y_axis({'name': 'Y Velocity (m/s)'})
        worksheet.insert_chart('Y2', chart4)

        chart5 = workbook.add_chart({'type': 'scatter'})
        chart5.add_series({
        'categories': '=Sheet1!$A$2:$A${}'.format(len(time)+1),
        'values':     '=Sheet1!$D$2:$D${}'.format(len(time)+1),
        })
        chart5.set_title ({'name': 'X Velocity Vs Time'})
        # Add x-axis label
        chart5.set_x_axis({'name': 'Time(s)'})

        # Add y-axis label
        chart5.set_y_axis({'name': 'X Xelocity(m/s)'})
        worksheet.insert_chart('Y20', chart5)


        chart6 = workbook.add_chart({'type': 'scatter'})
        chart6.add_series({
        'categories': '=Sheet1!$A$2:$A${}'.format(len(time)+1),
        'values':     '=Sheet1!$G$2:$G${}'.format(len(time)+1),
        })
        chart6.set_title ({'name': 'Y acceleration Vs Time'})
        # Add x-axis label
        chart6.set_x_axis({'name': 'Time (s)'})

        # Add y-axis label
        chart6.set_y_axis({'name': 'Y acceleration (m/s^2)'})
        worksheet.insert_chart('I20', chart6)

        chart7 = workbook.add_chart({'type': 'scatter'})
        chart7.add_series({
        'categories': '=Sheet1!$A$2:$A${}'.format(len(time)+1),
        'values':     '=Sheet1!$F$2:$F${}'.format(len(time)+1),
        })
        chart7.set_title ({'name': 'X acceleration Vs Time'})
        # Add x-axis label
        chart7.set_x_axis({'name': 'Time (s)'})

        # Add y-axis label
        chart7.set_y_axis({'name': 'X acceleration (m/s^2)'})
        worksheet.insert_chart('I37', chart7)


        headersv2= ["Ending Time", "Ending X Position","Ending Y positon","Time At Max Height", "X Position At Max Height","Max Height"]
        columnsv2 = [
            [round(endTime,5)],
            [xMax],
            [self.hf],
            [tyMax],
            [xPosYmax],
            [yMax]


        ]
        worksheet.write_row('A{}'.format(len(time)+2), headersv2,text_format)
        worksheet.write_column('A{}'.format(len(time)+3), columnsv2[0],text_format)
        worksheet.write_column('B{}'.format(len(time)+3), columnsv2[1],text_format)
        worksheet.write_column('C{}'.format(len(time)+3), columnsv2[2],text_format)
        worksheet.write_column('D{}'.format(len(time)+3), columnsv2[3],text_format)
        worksheet.write_column('E{}'.format(len(time)+3), columnsv2[4],text_format)
        worksheet.write_column('F{}'.format(len(time)+3), columnsv2[5],text_format)
        workbook.close()
        print("Maximum height:",yMax,"Time at max height:",tyMax,"X position at max height:",xPosYmax)
        print("Ending time:",round(endTime,5),"Y position:",self.hf,"X maximum:",xMax)
        return False

@app.route('/')
def password():
    return render_template('projectile.html')
@app.route('/badjob')
def returnBad():
    return render_template('badnumbers.html')
@app.route('/check',methods=["POST"])
def checking():
    print(request.form)
    data = {
        "email":request.form["email"],
        "password":request.form["password"]
    }
    r = requests.post("http://www.redmond2828.club/login",data = data)

    if r.text == "True" :
        print("here")
        response = make_response(redirect('/home'))
        response.set_cookie('Logged In', 'me')
        return response
    else:
        return render_template('newlogin.html')
@app.route('/Kin')
def kin():
    return render_template("K(arl)in.html")
@app.route('/home')
def getuserinput():
    f = open("ip.txt","a")
    f.write("{}\n".format(request.environ.get('HTTP_X_REAL_IP', request.remote_addr)))
    f.close()
    response = make_response(render_template('projectile.html'))
    return response
@app.route('/tickerDirect')
def cookiesecure():
    response = make_response(redirect('/ticker'))
    response.set_cookie("physdig", "code")
    return response
@app.route('/ticker')
def tick():
    response = make_response(render_template('ticker.html'))
    return response
@app.route('/home1')
def homebett():
    response = make_response(redirect('/home'))
    response.set_cookie('Logged In', 'me')
    return response
@app.route('/action', methods=["POST"])
def start():
    form = request.form
    ak = None
    if("xdis" not in form):
        ak = cord(0,float(form["ih"]),0,float(form["angle"]),float(form["ih"]),float(form["fh"]),float(form["iv"]),float(form["ti"]))
    else:
        velocityX = (float(form["xdis"])) / (float(form["dots"])-1)
        velocityX = velocityX/(float(form["ti"]))
        velocityInital = velocityX/ (math.cos(math.radians(float(form["angle"]))))

        print(velocityInital)
        ak = cord(0,float(form["ih"]),0,float(form["angle"]),float(form["ih"]),float(form["fh"]),velocityInital,float(form["ti"]))
    resp = ak.run()
    if(resp != True):
        response = make_response(send_from_directory(directory=os.getcwd(), filename='test.xlsx',as_attachment=True))
        response.headers['x-suggested-filename'] = "solution.xlsx"
        return response
    else:
        response= make_response(render_template('badnumbers.html'))
        return response
@app.route('/kinact',methods=["POST"])
def second():
    form = request.form
    a=kinematics(form["dist"],form["vi"],form["vf"],form["acc"],form["time"])
    return a.solve()
@app.route('/momentum')
def mom():
    return render_template('momentum.html')
@app.route('/momact',methods=["POST"])
def runthis():
    form = request.form
    print(form)
    a=collision(form["collisionType"],form["m1"],form["v1"],form["m2"],form["v2"],form["vf"],form["vi"],form["v2f"],form["v1f"])
    return a.run()
@app.route('/signup')
def signupsheet():
    return render_template("signup.html")
@app.route('/register',methods = ["POST"])
def register():
    print(request.form)
    data = {
        "email":request.form["email"],
        "password":request.form["password"]
    }
    r = requests.post("http://www.redmond2828.club/register",data=data)
    print(r.text)
    if(r.text == "sucess"):
        return render_template('passwordv3.html')
    else:
        return render_template('signup.html')
@app.route('/gfs',methods= ["GET","POST"])
def bust():
    if request.method == "GET":
        return render_template('gfs.html')
    else:
        a = fields(request.form["m1"],request.form["m2"],request.form["r"],request.form["f"])
        return a.solve()
@app.route('/efs',methods= ["GET","POST"])
def bustdown():
    if request.method == "GET":
        return render_template('gfs.html')
    else:
        a = efields.fields(request.form["m1"],request.form["m2"],request.form["r"],request.form["f"])
        return a.solve()

if __name__ == "__main__":
    app.run("0.0.0.0",port="5000")
