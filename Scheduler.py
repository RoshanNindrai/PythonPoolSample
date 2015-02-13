__author__ = 'Roshan'

import os
import copy_reg
import types
from executioner import Executioner, Job
from multiprocessing import  Pool

def _pickle_method(m):
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)

copy_reg.pickle(types.MethodType, _pickle_method)


pool = Pool(processes=2)


class Scheduler:

    def __init__(self):
        self.executioner = Executioner()
        pass

    def scheduler_task(self, task):
        pool.map_async(self.executioner.execution, (Job(task),))