import os

class Branch(object):
    def __init__(self, name):
        self.name = name

    def push(self):
        os.system('git push origin %s' % self.name)

print 'branching'

