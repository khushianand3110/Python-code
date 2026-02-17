import json
import logging
import os
from base_validator import BaseValidator


class PolicyValidator(BaseValidator):
    """
    PolicyValidator loads security policies from a JSON file
    and validates them using multiple checks.
    """

    def __init__(self, file_path):
        """
        Initialize validator with file path.
        """
        self.file_path = file_path
        self.policies = []
        self.errors = {}
        self.duplicate_ids = []

    def setup_logging(self):
        """
        Setup logging configuration and ensure logs directory exists.
        """
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
        """
        Logs errors if file not found or JSON invalid.
        """
        try:
            with open(self.file_path, "r") as f:
                self.policies = json.load(f)
            logging.info("Policies loaded successfully")
        except Exception:
            logging.error("Error loading policies")

    def duplicate_detection(self, policy):
        """
        Detect duplicate policy_id.
        """
        logging.info("Duplicate detection detected")
        errors = []
        id = policy.get("policy_id")
        if id is None:
            return errors

        if policy["policy_id"] in self.duplicate_ids:
            errors.append("Duplicate policy_id")
        else:
            self.duplicate_ids.append(policy["policy_id"])
        return errors

    def name_validation(self, policy):
        """
        Validate policy name is not empty.
        """
        logging.info("Name validation detected")
        errors = []
        name = policy.get("name")
        if name is None:
            return errors

        if policy["name"] == "":
            errors.append("Name is empty")
        return errors

    def enabled_check(self, policy):
        """
        Validate enabled field must be boolean.
        """
        logging.info("Enabled check detected")
        errors = []
        check = policy.get("enabled")

        if check is not None and not isinstance(check, bool):
            errors.append("Enabled is not boolean")
        return errors

    def min_validation(self, policy):
        """
        Validate minimum length must be integer >= 6.
        """
        logging.info("Minimum validation detected")
        errors = []
        if policy["min_length"] < 6:
            errors.append("min_length < 6")
        return errors

    def max_validation(self, policy):
        """
        Validate max_attempts must be integer > 0.
        """
        logging.info("Maximum validation detected")
        errors = []
        if policy["max_attempts"] <= 0:
            errors.append("max_attempts <= 0")
        return errors

    def validate_all(self):
        """
        Run all validations on loaded policies.
        """
        for policy in self.policies:
             id = policy["policy_id"]
             self.errors[id] = []

             self.errors[id] += self.duplicate_detection(policy)
             self.errors[id] += self.name_validation(policy)
             self.errors[id] += self.enabled_check(policy)
             self.errors[id] += self.min_validation(policy)
             self.errors[id] += self.max_validation(policy)

        logging.info("Validation completed")

    def show_results(self):
        """
        Log validation summary such as:
        total policies
        valid count
        invalid count
        """

        if not self.errors:
            logging.warning("No validation results found. Run validate_all() first.")
            return

        valid = []
        invalid = []

        for pid, errs in self.errors.items():
            if errs:
                invalid.append(pid)
            else:
                valid.append(pid)

        logging.info("Total policies: %d", len(self.errors))
        logging.info("Valid policies (%d): %s", len(valid), ", ".join(valid) if valid else "None")
        logging.info("Invalid policies (%d): %s", len(invalid), ", ".join(invalid) if invalid else "None")

        for pid, errs in self.errors.items():
            if errs:
                for err in errs:
                    logging.info("%s : %s", pid, err)
            else:
                logging.info("%s : VALID", pid)


security = PolicyValidator("Data.json")
security.setup_logging()
security.load_policies()
security.validate_all()
security.show_results()