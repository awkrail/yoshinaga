import xlrd

class SensorLoaderClass(object):
    def __init__(self):
        self.sensor_detail_dict = {}
        self.sensor_measure_dict = {}

    def load_excel(self, path):
        book = xlrd.open_workbook('sensor_data/', path)


