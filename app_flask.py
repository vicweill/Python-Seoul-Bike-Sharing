from flask import Flask, render_template, request
import flask
import numpy as np
import pickle as pkl
import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
f_path = dir_path + '\model.pkl'
# this is the path of the model

app = Flask(__name__)
with open(f_path, 'rb') as f:
	model = pkl.load(f)


@app.route("/")
def home():
	return render_template('main.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
	pred=''
	if flask.request.method == 'POST':
		Hour = int(request.form.get('hour'))
		Temperature = int(request.form.get('temperature'))
		Humidity = int(request.form.get('humidity'))
		Wind_speed = int(request.form.get('wind_speed'))
		Visibility = int(request.form.get('visibility'))
		Solar_radiation = int(request.form.get('solar_radiation'))
		Rainfall = int(request.form.get('rainfall'))
		Snowfall = int(request.form.get('snowfall'))
		Holiday = str(request.form.get('holiday'))
		Functioning_day = str(request.form.get('functioning_day'))
		Day = str(request.form.get('day'))
		Month = str(request.form.get('month'))

		# We must check all our string variables and convert them
		# to compute the prediction
		if Day == 'Monday':
			Day = 1
		elif Day == 'Tuesday':
			Day = 2
		elif Day == 'Wednesday':
			Day = 3
		elif Day == 'Thursday':
			Day = 4
		elif Day == 'Friday':
			Day = 5
		elif Day == 'Saturday':
			Day = 6
		elif Day == 'Sunday':
			Day = 7
		else:
			Day = random.randint(1, 7)
		# we randomly choose the variable value if the input is wrong

		if Month == 'January':
			Month = 1
		elif Month == 'February':
			Month = 2
		elif Month == 'March':
			Month = 3
		elif Month == 'April':
			Month = 4
		elif Month == 'May':
			Month = 5
		elif Month == 'June':
			Month = 6
		elif Month == 'July':
			Month = 7
		elif Month == 'August':
			Month = 8
		elif Month == 'September':
			Month = 9
		elif Month == 'October':
			Month = 10
		elif Month == 'November':
			Month = 11
		elif Month == 'December':
			Month = 12
		else:
			Month = random.randint(1, 12)

		if Holiday == 'Yes':
			Holiday = 1
		elif Holiday == 'No':
			Holiday = 0
		else:
			Holiday = random.randint(0, 1)

		if Functioning_day == 'Yes':
			Functioning_day = 1
		elif Functioning_day == 'No':
			Functioning_day = 2
		else:
			Functioning_day = random.randint(0, 1)

		arr = np.array([Hour, Temperature, Humidity, Wind_speed, Visibility,
						Solar_radiation, Rainfall, Snowfall, Holiday,
						Functioning_day, Day, Month]).reshape(1, -1)
		predict = model.predict(arr)

		output = int(predict[0])
		pred="The number of rented bikes must be {}".format(output)

	return render_template('home.html', prediction_text=pred)


@app.route("/short", methods=['GET', 'POST'])
def predictshort():
	pred=''
	if flask.request.method == 'POST':
		# We take the mean value for the variables we're not asking.
		Hour = int(request.form.get('hour2'))
		Temperature = int(request.form.get('temperature2'))
		Humidity = int(request.form.get('humidity2'))
		Wind_speed = int(request.form.get('wind_speed2'))
		Visibility = 1437
		Solar_radiation = 0.57
		Rainfall = int(request.form.get('rainfall2'))
		Snowfall = int(request.form.get('snowfall2'))
		Holiday = 0
		Functioning_day = 1
		Day = str(request.form.get('day2'))
		Month = str(request.form.get('month2'))

		# We must check all our string variables and convert them
		# to compute the prediction
		if Day == 'Monday':
			Day = 1
		elif Day == 'Tuesday':
			Day = 2
		elif Day == 'Wednesday':
			Day = 3
		elif Day == 'Thursday':
			Day = 4
		elif Day == 'Friday':
			Day = 5
		elif Day == 'Saturday':
			Day = 6
		elif Day == 'Sunday':
			Day = 7
		else:
			Day = random.randint(1, 7)
		# we randomly choose the variable value if the input is wrong

		if Month == 'January':
			Month = 1
		elif Month == 'February':
			Month = 2
		elif Month == 'March':
			Month = 3
		elif Month == 'April':
			Month = 4
		elif Month == 'May':
			Month = 5
		elif Month == 'June':
			Month = 6
		elif Month == 'July':
			Month = 7
		elif Month == 'August':
			Month = 8
		elif Month == 'September':
			Month = 9
		elif Month == 'October':
			Month = 10
		elif Month == 'November':
			Month = 11
		elif Month == 'December':
			Month = 12
		else:
			Month = random.randint(1, 12)

		arr = np.array([Hour, Temperature, Humidity, Wind_speed, Visibility,
						Solar_radiation, Rainfall, Snowfall, Holiday,
						Functioning_day, Day, Month]).reshape(1, -1)
		predict = model.predict(arr)

		output = int(predict[0])
		pred = "The number of rented bikes must be {}".format(output)

	return render_template('short.html', prediction_text=pred)


if __name__ == "__main__":
    app.run(port=666, debug=True)