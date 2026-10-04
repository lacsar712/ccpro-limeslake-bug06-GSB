"""状态筛选范围：网格点亮与页脚计数共用的无状态判定。"""

from __future__ import annotations


def allowed_statuses(wanted: str | None) -> list[str] | None:
    """返回当前筛选允许的状态集合。

    无筛选时返回 None（表示全部点亮、全部计数）；否则只包含所选状态。
    必须为纯函数：不得持有模块级状态，以免并发请求互相污染。
    """
    if not wanted:
        return None
    return [wanted]
