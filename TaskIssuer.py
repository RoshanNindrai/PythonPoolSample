__author__ = 'Roshan'

from Scheduler import Scheduler
import time, random

scheduler = Scheduler()
task = ['ios', 'android']

#giving 20 random task
for i in range(0, 20):
    scheduler.scheduler_task(task[random.randint(0,1)])
    time.sleep(1)

