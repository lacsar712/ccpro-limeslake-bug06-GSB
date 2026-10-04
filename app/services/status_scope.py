"""状态筛选范围：网格点亮与页脚统计共用同一套口径，保证两者永不打架。"""

from __future__ import annotations

from app.models import Pond

_VALID_STATUSES = frozenset(Pond.STATUS_CHOICES)


def scoped_statuses(wanted: str | None) -> frozenset[str] | None:
    """返回当前筛选允许的状态集合；None 表示不筛选（全部点亮）。

    纯函数、无请求间缓存：网格点亮与页脚计数都以此为准，
    切回全部再筛、以及多人几乎同时改状态时都不会残留上一轮条件。
    """
    if wanted in _VALID_STATUSES:
        return frozenset({wanted})
    return None
