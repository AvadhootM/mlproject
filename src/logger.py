## Any execution tha thappens, we should be able to log all that info somewhere and access it afterwards
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

## Whenever logging.info is used, it will create following file path and follow the specified format wrt to the message to be printed
logging.basicConfig(
filename=LOG_FILE_PATH, ## file path
format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", ## message format
level=logging.INFO,

)

'''
## To check if the looger.py is working properly
if __name__=="__main__":
    logging.info("Logging has started")
'''