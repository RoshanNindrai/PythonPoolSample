__author__ = 'Roshan'
from multiprocessing import  Lock
import time, os

ios_lock = Lock()
android_lock = Lock()

class Job():

    def __init__(self, job_id):
        self.job_id = job_id

class Executioner:

    def execution(self, job):

        print job.job_id , 'issued to', os.getpid()

        if(job.job_id == 'ios'):
            #at on point of time their can be one worker using the device
            ios_lock.acquire()
            time.sleep(6)
            ios_lock.release()
        else:
            android_lock.acquire()
            time.sleep(1)
            android_lock.release()

        print job.job_id , 'finished by', os.getpid()