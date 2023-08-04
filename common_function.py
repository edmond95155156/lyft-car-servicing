from datetime import datetime




class CommonFunction:
    def dateConvert(date_str):
        return datetime.strptime(date_str, '%d-%m-%Y').date()