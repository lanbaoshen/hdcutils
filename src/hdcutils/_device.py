from typing import TYPE_CHECKING

from hdcutils import adb_mapping
from hdcutils._hilog import HiLog
from hdcutils._uitest import UITest

if TYPE_CHECKING:
    from hdcutils._hdc import HDC


_REFER_CHAIN = 'HDCClient().device()'
_DOC = 'https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#'


class HDCDevice:
    def __init__(self, *, connect_key: str | None = None, hdc: 'HDC'):
        self._connect_key = connect_key
        self._hdc = hdc
        self._hilog = HiLog(self)
        self._uitest = UITest(self)

    @property
    def connect_key(self) -> str:
        return self._connect_key

    @property
    def hilog(self) -> 'HiLog':
        return self._hilog

    @property
    def uitest(self) -> 'UITest':
        return self._uitest

    @adb_mapping(cmd='adb -s', refer_chain=_REFER_CHAIN, doc=_DOC)
    def cmd(self, cmd: list[str], timeout: int = 5) -> tuple[str, str]:
        """
        Execute a HDC command on the device.

        Args:
            cmd: The command to execute, as a list of strings.
            timeout: The timeout for the command execution in seconds.

        Returns:
            stdout, stderr
        """
        cmd = ['-t', self._connect_key] + cmd if self._connect_key else cmd
        return self._hdc.cmd(cmd, timeout=timeout)

    @adb_mapping(cmd='adb -s shell', refer_chain=_REFER_CHAIN, doc=f'{_DOC}hdc-debugging-logs')
    def shell(self, cmd: list[str], timeout: int = 5) -> tuple[str, str]:
        """
        Execute a HDC shell command on the device.

        Args:
            cmd: The command to execute, as a list of strings.
            timeout: The timeout for the command execution in seconds.

        Returns:
            stdout, stderr
        """
        cmd = ['-t', self._connect_key, 'shell'] + cmd if self._connect_key else ['shell'] + cmd
        return self._hdc.cmd(cmd, timeout=timeout)
