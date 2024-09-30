from mangum import Mangum
from app.router import app

lambda_handler = Mangum(app)