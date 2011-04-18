#__author__ = 'jiangsp'
from random import random
from blog.models import *
from datetime import datetime
import settings
import time


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

def setup_data():
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

    for i in xrange(500):
        mer = Merchandise()
        mer.name = random_string(10)
        mer.catalog = random_int(10)
        mer.trade_mark = random_string(20)
        mer.sn = random_int(20)
        mer.detail = random_string(20)
        mer.join_time = datetime.now()
        mer.painting = MerchandisePainting()
        mer.painting.painting_id = random_string(12)
        mer.painting.painting_name = random_string(20)
        mer.painting.author_id = random_string(12)
        mer.painting.author_name = random_string(10)
        mer.subclass = MerchandiseSubClass()
        mer.subclass.subclass_id = random_string(12)
        mer.subclass.subclass_name = random_string(20)
        mer.subclass.gender = 0
        mer.subclass.color = random_int(10)
        mer.subclass.style = random_int(10)
        mer.subclass.s_left_count = random_int(100)
        mer.subclass.m_left_count = random_int(100)
        mer.subclass.l_left_count = random_int(100)
        mer.subclass.xl_left_count = random_int(100)
        mer.subclass.xxl_left_count = random_int(100)
        mer.subclass.xxxl_left_count = random_int(100)
        mer.subclass.original_price = random_float(50)
        mer.subclass.sell_price = random_float(50)
        mer.subclass.vip_price = random_float(50)
        mer.subclass.special_price = random_float(50)
        mer.rank0_count = random_int(200)
        mer.rank1_count = random_int(200)
        mer.rank2_count = random_int(200)
        mer.rank3_count = random_int(200)
        mer.rank4_count = random_int(200)
        mer.rank5_count = random_int(200)
        mer.scorers = []
        for i in xrange(random_int(100)):
            scorer = Scorer()
            scorer.user_id = random_string(12)
            scorer.nick_name = random_string(8)
            scorer.grade = random_int(5)
            mer.scorers.append(scorer)
        mer.save()

def test():
    t0 = time.time()
    merchandises = Merchandise.objects[30:50]
    t1 = time.time()
    print t1-t0


#setup_data()
test()