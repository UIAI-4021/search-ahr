import time


class Time:
    start_time: float
    end_time: float

    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def Time_starting_(self):
        self.start_time = time.time()

    def Time_Ending_(self):
        self.end_time = time.time()

    def Execution(self):
        return self.end_time - self.start_time
