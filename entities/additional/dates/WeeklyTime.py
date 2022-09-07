from entities.additional.dates.DailyTime import DailyTime


class WeeklyTime:
    def __init__(self,  availability) -> None:
        self.__init_weekly_days(availability)

    def __init_weekly_days(self,raw_availabilities):
        self.dailyAv = []
        for raw_availability in raw_availabilities:
            self.dailyAv.append(DailyTime(raw_availability))