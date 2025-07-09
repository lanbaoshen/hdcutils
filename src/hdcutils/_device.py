from typing import TYPE_CHECKING

from hdcutils._hilog import HiLog

if TYPE_CHECKING:
    from hdcutils._hdc import HDC


class HDCDevice:
    def __init__(self, *, connect_key: str | None = None, hdc: 'HDC'):
        self._connect_key = connect_key
        self._hdc = hdc
        self._hilog = HiLog(self)

    @property
    def connect_key(self) -> str:
        return self._connect_key

    @property
    def hilog(self) -> 'HiLog':
        return self._hilog

    def cmd(self, cmd: list[str], timeout: int = 5) -> tuple[str, str]:
        cmd = ['-t', self._connect_key] + cmd if self._connect_key else cmd
        return self._hdc.cmd(cmd, timeout=timeout)

    def shell(self, cmd: list[str], timeout: int = 5) -> tuple[str, str]:
        cmd = ['-t', self._connect_key, 'shell'] + cmd if self._connect_key else ['shell'] + cmd
        return self._hdc.cmd(cmd, timeout=timeout)
