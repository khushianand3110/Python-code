class BaseValidator:
    def __init__(self):
        self.REQUIRED_FIELDS = []

    def check_required_fields(self, policy):
        self.REQUIRED_FIELDS = ["policy_id", "name", "enabled", "min_length", "max_attempts"]
        miss = []
        for field in self.REQUIRED_FIELDS:
            if field not in policy:
                miss.append(field)
        return miss
