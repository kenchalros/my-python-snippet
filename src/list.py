from bisect import bisect_left
from operator import lt, le
def find_nearst_value(sorted_lst, val, left=True):
    """ソート済のリストから，valに最も近い要素を返す.
    :param lst: ソート済のリスト
    :param left:
        lv < val < rv，val-lv == rv-val のとき，
        Trueならばlvを，Falseならばrvを選択する
    :return もっともvalに値が近いlstの要素
    """
    pos = bisect_left(sorted_lst, val)
    if pos == 0: return sorted_lst[0]
    if pos == len(sorted_lst): return sorted_lst[-1]
    lv, rv = sorted_lst[pos-1:pos+1]
    op = le if left else lt
    return lv if op(val-lv, rv-val) else rv