from entities.additional.dates.TimeWindow import TimeWindow

class DailyTime:
    def __init__(self, availability) -> None:
        self.day = availability["day"]
        self.__init_daily_time(availability["hours"])

    def __init_daily_time(self, time_windows):
        self.time_window = []
        for time_window in time_windows:
            self.time_window.append(TimeWindow(time_window))