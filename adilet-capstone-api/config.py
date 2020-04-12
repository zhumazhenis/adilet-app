import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    UPLOAD_FOLDER = "image-file"
    CSRF_ENABLED = True
    DEBUG = False

    # Enter your API Key and Custom Classifier ID below
    API_KEY = "Y6ftVJqnQh3iOJslwZ9_gZCsOYT7rZq52bWZ_PLxWD-3"
    CLASSIFIER_ID = "FurnitureClassifier_2069579328"
