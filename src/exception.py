import sys
from src.logger import logging # will ensure the errors get logged in into the logs file

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomException(Exception):
    '''
    When the class is run, this will inherit the Exception from the parent exception. Whatever the error message is coming from the above function will come here and will initialize to the CustomException variable
    '''
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) ## inherit the exception class
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self): ## To get the error message when you print it
        return self.error_message
    
'''
## To check if the exception.py is working properly
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)
'''