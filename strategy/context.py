class CounselorFilter:
    def __init__(self):
        self.strategy = None

    # Set the filter strategy
    def set_strategy(self, strategy):
        self.strategy = strategy

    def filter(self, counselors):
        if not self.strategy:
            raise Exception("Please set a filter strategy before filtering.")
        return self.strategy.filter(counselors)
