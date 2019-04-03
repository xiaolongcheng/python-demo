import math
import cv2
import numpy as np
import roi_merge as roi_
import util_funs as util
from get_rects import *



print("test", math.sin(1))
print("test", math.pi)
print("test", math.e)
print("test", 3+4j + 5+8j)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            w = self.a
            self.a += 1
            return w
        else:
            raise StopIteration


myClass = MyNumbers()
myIter = iter(myClass)

for x in myIter:
    print(x)
