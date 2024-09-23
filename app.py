import pyautogui
import cv2
import numpy as np
import time
from flask import Flask, request, jsonify

app = Flask(__name__)
is_running = False

def locate_gem(image_path):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread(image_path, 0)
    res = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.8:  # 设定一个阈值
        return max_loc
    return None

def auto_mine(image_path):
    global is_running
    while is_running:
        pos = locate_gem(image_path)
        if pos:
            pyautogui.click(pos[0], pos[1])
        time.sleep(5)

@app.route('/start', methods=['POST'])
def start_mining():
    global is_running
    if not is_running:
        is_running = True
        image_path = request.json.get('image_path')
        auto_mine(image_path)
        return jsonify({"status": "started"}), 200
    return jsonify({"status": "already running"}), 400

@app.route('/stop', methods=['POST'])
def stop_mining():
    global is_running
    if is_running:
        is_running = False
        return jsonify({"status": "stopped"}), 200
    return jsonify({"status": "not running"}), 400

@app.route('/')
def index():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)