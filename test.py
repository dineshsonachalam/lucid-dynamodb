import os
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
if __name__ == "__main__":
    print(len(AWS_ACCESS_KEY_ID))
    print(len(AWS_SECRET_ACCESS_KEY))