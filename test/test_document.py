#__author__ = 'jiangsp'
from random import random
from blog.models import *
from datetime import datetime
import settings
print settings


def random_int(base=None):
    if not base:
        base = 10
    return int(random()*base)

def random_float(base=None):
    if not base:
        base = 20
    return float(random()*base)

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
CHARS_LEN = len(CHARS)
def random_string(length=None):
    if not length:
        length = int(random()*10)
    ret = ""
    for i in xrange(length):
        ret += CHARS[int(CHARS_LEN*random())]
    return ret


for i in xrange(10):
    paint = Painting()
    paint.name = random_string(10)
    paint.author = Author()
    paint.author.name = random_string(10)
    paint.join_time = datetime.now()
    paint.end_time = datetime.now()
    paint.rating = random_float()
    paint.tee_count = random_int()
    paint.sweater_count = random_int()
    paint.comments = []
    for i in xrange(random_int(20)):
        comment = PaintingComment()
        comment.user_id = random_string(12)
        comment.nick_name = random_string(8)
        comment.content = random_string(30)
        comment.time = datetime.now()
        paint.comments.append(comment)
    paint.scorer = []
    for i in xrange(random_int(100)):
        scorer = Scorer()
        scorer.user_id = random_string(12)
        scorer.nick_name = random_string(8)
        scorer.grade = random_int(5)
        paint.scorer.append(scorer)
    paint.save()

for i in xrange(100):
    