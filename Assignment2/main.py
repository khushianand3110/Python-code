import json
import logging
import os
from base_validator import BaseValidator


class PolicyValidator(BaseValidator):

    def __init__(self, file_path):
        self.file_path = file_path
        self.policies = []
        self.errors = {}
        self.duplicate_ids = []

    def setup_logging(self):
        if not os.path.exists("logs"):
            os.makedirs("logs")

        log_file = os.path.join("logs", "my_test.log")

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            filemode="a",
        )

    def load_policies(self):
        try:
            with open(self.file_path, "r") as f:
                self.policies = json.load(f)
            logging.info("Policies loaded successfully")
        except Exception:
            logging.error("Error loading policies")

    def duplicate_detection(self, policy):
        logging.info("Duplicate detection detected")
        errors = []
        if policy["policy_id"] in self.duplicate_ids:
            errors.append("Duplicate policy_id")
        else:
            self.duplicate_ids.append(policy["policy_id"])
        return errors

    def name_validation(self, policy):
        logging.info("Name validation detected")
        errors = []
        if policy["name"] == "":
            errors.append("Name is empty")
        return errors

    def enabled_check(self, policy):
        logging.info("Enabled check detected")
        errors = []
        if not isinstance(policy["enabled"], bool):
            errors.append("Enabled is not boolean")
        return errors

    def min_validation(self, policy):
        logging.info("Minimum validation detected")
        errors = []
        if policy["min_length"] < 6:
            errors.append("min_length < 6")
        return errors

    def max_validation(self, policy):
        logging.info("Maximum validation detected")
        errors = []
        if policy["max_attempts"] <= 0:
            errors.append("max_attempts <= 0")
        return errors

    def validate_all(self):
         for policy in self.policies:
             id = policy["policy_id"]
             self.errors[id] = []

             self.errors[id] += self.duplicate_detection(policy)
             self.errors[id] += self.name_validation(policy)
             self.errors[id] += self.enabled_check(policy)
             self.errors[id] += self.min_validation(policy)
             self.errors[id] += self.max_validation(policy)


security = PolicyValidator("Data.json")
security.setup_logging()
security.load_policies()
security.validate_all()