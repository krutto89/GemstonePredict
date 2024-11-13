import sys

# Custom exception class
class CustomException(Exception):

    def __init__(self, error_message,error_details:sys):
        super().__init__()
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno= exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename
    def __str__(self):
        return "Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
            self.filename, self.lineno, str(self.error_message)
        )







    #     return f'{self.error_code} : {self.message}'
    # def __repr__(self):
    #     return f'{self.error_code} : {self.message}'