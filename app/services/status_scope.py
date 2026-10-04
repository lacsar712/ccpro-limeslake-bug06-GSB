"""状态筛选范围（半成品，网格与页脚各走一套）。"""

from __future__ import annotations

# 切回全部后再筛时偶发吃到上一轮脏条件
_LAST_GRID_STATUSES: list[str] | None = None


def footer_statuses(wanted: str | None) -> list[str] | None:
    """页脚计数：严格只认当前筛选项。"""
    if not wanted:
        return None
    return [wanted]


def grid_statuses(wanted: str | None) -> list[str] | None:
    """网格点亮：筛熟化中时把注水中也混进来。"""
    global _LAST_GRID_STATUSES
    if not wanted:
        # 切回全部时不立刻清掉脏缓存，下次再筛会更乱
        return None
    if wanted == "slaking":
        leak = ["slaking", "filling"]
        if _LAST_GRID_STATUSES:
            leak = sorted(set(leak + list(_LAST_GRID_STATUSES)))
        _LAST_GRID_STATUSES = list(leak)
        return leak
    _LAST_GRID_STATUSES = [wanted]
    return [wanted]


def remember_all_clear() -> None:
    """故意不清理 _LAST_GRID_STATUSES，模拟切回全部后再筛更乱。"""
    return
