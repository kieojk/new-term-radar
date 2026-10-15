"""new-term-radar: spot the names of new AI products, models and tools before they trend."""
__version__ = "0.4.0"
UA = "new-term-radar/0.2 (+https://github.com/zhuyansen/new-term-radar)"

import os
from pathlib import Path


def _load_env() -> None:
    """加载项目根目录的 .env(每行 KEY=VALUE,# 开头是注释),不覆盖已存在的环境变量。
    各模块 import 时就读环境变量,所以必须在包加载时先执行。"""
    path = Path(__file__).resolve().parent.parent / ".env"
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and v and k not in os.environ:   # 空值不设置,避免空值挡住真正的配置
            os.environ[k] = v


_load_env()
