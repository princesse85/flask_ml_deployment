from flask import Flask,render_template, request
import numpy as np
from prediction import predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
          'home.html'
     )


@app.route('/predict', methods=['POST'])
def predict_route():
    if request.method == 'POST':
        precipitation = request.form['precipitation']
        apparent_temperature = request.form['apparent_temperature']

        input_data=np.array([[int(precipitation),int(apparent_temperature)]])

        result=predict(input_data)

        # For now, just display the inputs
        return f"Precipitation: {precipitation} mm, Apparent Temperature: {apparent_temperature} °C prediction:{result}"


if __name__ =='__main__':
    app.run(debug=True)
