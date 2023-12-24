# local library
from application.app import app, db
from application.tests import tests_job, tests_applicant



if __name__ == "__main__":
    app.run()