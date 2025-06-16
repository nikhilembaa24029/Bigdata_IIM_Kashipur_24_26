from flask import Flask, jsonify, render_template
import random
import time
from threading import Thread
import os
from fetch_data import fetch_latest_data

app = Flask(__name__)

real_stream_table = "real_stream"
pred_stream_table = "pred_stream"

# Biến lưu dữ liệu thời gian thực
data = []
predict_data = []

# Hàm tạo dữ liệu ngẫu nhiên
def generate_data():
    global data
    while True:
        # Get current time from system command
        # timestamp = os.popen("date +%s%3N").read().strip()  # Get timestamp in milliseconds

        # Add GMT+7 time zone offset (7 hours × 3600 seconds)
        # timestamp = int(timestamp)  # Convert to integer
        # timezone_offset = 7 * 3600 * 1000  # Convert to milliseconds
        # timestamp = timestamp + timezone_offset

        # value = random.uniform(20000, 100000)     # Random value
        try:
            real_stream = fetch_latest_data(real_stream_table)
            real_timestamp = real_stream["timestamp"]
            real_value = real_stream["close"]
            data.append([real_timestamp, real_value])
        except Exception as e:
            print(f"Error fetching data: {e}")
            continue
        try:
            pred_stream = fetch_latest_data(pred_stream_table)
            pred_timestamp = pred_stream["timestamp"]
            pred_value = pred_stream["close"]

            predict_data.append([pred_timestamp, pred_value])
        except Exception as e:
            print(f"Error fetching data: {e}")
            continue
        if len(data) > 100:  # Giữ tối đa 100 điểm
            data.pop(0)
        print(len(predict_data))
        if len(predict_data) > 100:
            predict_data.pop(0)
        time.sleep(1)


# API provides data
@app.route('/data')
def get_data():
    return jsonify({"data": data, "predict_data": predict_data})

# Main page
@app.route('/')
def index():
    return render_template('index.html')

# Start the data generation thread when the application launches
if __name__ == '__main__':
    Thread(target=generate_data, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
