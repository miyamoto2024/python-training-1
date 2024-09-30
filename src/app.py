from mangum import Mangum
from router import app

lambda_handler = Mangum(app)