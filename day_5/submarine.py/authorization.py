import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LaunchAuthorizationSystem:
   
    AUTH_PATTERN = r"^AUTH-[A-Z0-9]{6}-\d{4}-SECURE$"

    @staticmethod
    def validate_code(code):
       
        if re.match(LaunchAuthorizationSystem.AUTH_PATTERN, code):
            logging.info("Authorization Code Validated Successfully!")
            return True
        else:
            logging.warning("Invalid Authorization Code!")
            return False
