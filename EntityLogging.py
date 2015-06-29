import ConfigAnalyser
import logging
import config
import os


class EntityLogging(ConfigAnalyser):
    def __init__(self, name, level=logging.DEBUG, file_record = True, console_record = True):
        super.__init__(self)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.loglevel = level
        self.logFormat(self.log_format)
        if file_record:
            self.writeLogFile(self.log_file)
            self.logger.addHandler(self.fh)
        if console_record:
            self.wirteToConsole()
            self.logger.addHandler(self.ch)
    
    
    def writeLogFile(self,file_path):
        self.fh = logging.FileHandler(file_path)
        fh.setLevel(self.loglevel)
        
    
    
    def wirteToConsole(self):
        self.ch = logging.StreamHandler()
        ch.setLevel(self.loglevel)  
        
    
    def logFormat(self,formatPattern):
        if not formatPattern:
            formatPattern = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(formatPattern)
        if self.fh:
            self.fh.setFormatter(formatter)
        if self.ch:
            self.ch.setFormatter(formatter)
            
    
    def recordLog(self, log_string):
        self.logger.log(log_string)
        
        
        