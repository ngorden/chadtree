from os import linesep
from typing import AbstractSet, Optional

from pynvim import Nvim
from pynvim_pp.lib import write

from ..registry import rpc
from ..settings.types import Settings
from ..state.types import State
from .types import Stage


def _sys_search(args: str, cwd: str, sep: str) -> AbstractSet[str]:
    raise Exception()


@rpc(blocking=False)
def _search(nvim: Nvim, state: State, settings: Settings, is_visual: bool) -> Stage:
    """
    New search params
    """

    cwd = state.root.path
    pattern: Optional[str] = nvim.funcs.input("new_search", "")
    results = _sys_search(pattern or "", cwd=cwd, sep=linesep)
    write(nvim, results)

    return Stage(state)
