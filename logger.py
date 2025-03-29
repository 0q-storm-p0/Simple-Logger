import datetime
import os

class Logger:
    def __init__(self, save: bool=True, set_date: bool=True, backup_location: str="./", date_format: str="%YY/%MM/%DD", time_format: str="%HH:%MM:%SS") -> None:
        self.save = save
        self.set_date = set_date
        self.backup_location = backup_location
        self.date_format = date_format
        self.time_format = time_format
        
        if ("%YY" or "%MM" or "%DD") not in date_format:
            raise Exception("Wrong date format! \nExample : \"%YY/%MM/%DD\"")
        if ("%HH" or "%MM" or "%SS") not in time_format:
            raise Exception("Wrong time format! \nExample : \"%HH:%MM:%SS\"")
                    
    def log(self, save: bool=None, message: str='') -> None:
        if save == None:
            save = self.save
            
        now = datetime.datetime.now()
        Y = str(now.year).zfill(2)
        M = str(now.month).zfill(2)
        D = str(now.day).zfill(2)
        h = str(now.hour).zfill(2)
        m = str(now.minute).zfill(2)
        s = str(now.second).zfill(2)

        LOG = None
        time = self.time_format
        time = time.replace("%HH", h).replace("%MM", m).replace("%SS", s)
        
        if self.set_date:
            date = self.date_format
            date = date.replace("%YY", Y).replace("%MM", M).replace("%DD", D)
            LOG = "[ " + date + ' - ' + time + ' ] ' + message
            
        else:
            LOG = "[ " + time + ' ] ' + message
                
        if save:
            bk_path = self.backup_location + 'Logs/' + Y + '/' + M + '/' + D + '/' + h + 'h/'
            if os.path.isdir(bk_path) == False:
                try:
                    os.makedirs(name=bk_path)
                except Exception as e:
                    print(e)
                
            with open(file=bk_path + m + 'm' + '.txt', mode='a') as log_file:
                log_file.write('[ ' + s + "s ] " + message + '\n')
        
        print(LOG)
        
logger = Logger(save=True, set_date=True)
logger.log(message='test')