class Chart:
    LINE = "line"
    BAR = "bar"
    RADAR = "radar"
    DOUGHNUT = "doughnut"
    PIE = "pie"
    POLAR_AREA = "polarArea"
    BUBBLE = "bubble"
    SCATTER = "scatter"  # Needs an x and y in dataset

    def __init__(self, chart_type, data_x, data_y, label, color):
        self.chart_type = chart_type
        self.x = data_x
        self.y = data_y
        self.label = label
        self.color = color

    def get_type(self):
        pass

    def get_data(self):
        pass

    def get_options(self):
        pass

    def get_config(self):
        return self.get_type(), self.get_data(), self.get_options()