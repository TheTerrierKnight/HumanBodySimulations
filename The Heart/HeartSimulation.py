import time
import math

class Heart:
    def __init__(self, max_heart_rate):
        self.max_heart_rate = max_heart_rate
        self.current_heart_rate = 0
        self.blood_flow = 0

    def simulate_heartbeat(self):
        # Simulate the electrical activity of the heart by calculating the heart rate
        self.current_heart_rate = (self.max_heart_rate / 2) + (self.max_heart_rate / 2) * math.sin(time.time())

        # Simulate blood flow using a simple mathematical model
        self.blood_flow = self.current_heart_rate * 10

heart = Heart(120) # Create a new heart object with a maximum heart rate of 120 beats per minute

while True:
    heart.simulate_heartbeat() # Simulate the heart's electrical activity and blood flow
    print("Current heart rate: {:.2f} bpm, blood flow: {:.2f} ml/min".format(heart.current_heart_rate, heart.blood_flow))
    time.sleep(1) # Wait for 1 second before simulating the next heartbeat