from abc import ABC, abstractmethod

class Report(ABC):
    
    @abstractmethod
    def canvas_config():
        pass

    @abstractmethod
    def add_header():
        pass

    @abstractmethod
    def generate_report():
        pass

class DailyReport(Report):
    
    def __init__(file_path):
        pass

class WeeklyReport(Report):
    pass

class MonthlyReport(Report):
    pass