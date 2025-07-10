from pathlib import Path
from typing import TYPE_CHECKING

from hdcutils import adb_mapping
from hdcutils.extension import AbilityAssistant, BundleManager, HiLog, UITest

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
        self._bm = BundleManager(self)
        self._aa = AbilityAssistant(self)

    @property
    def connect_key(self) -> str:
        return self._connect_key

    @property
    def hilog(self) -> 'HiLog':
        return self._hilog

    @property
    def uitest(self) -> 'UITest':
        return self._uitest

    @property
    def bm(self) -> 'BundleManager':
        return self._bm

    @property
    def aa(self) -> 'AbilityAssistant':
        return self._aa

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

    @adb_mapping(cmd='adb install', refer_chain=_REFER_CHAIN, doc=f'{_DOC}commands')
    def install(self, path: str | Path, *, replace: bool = False, shared: bool = False) -> tuple[str, str]:
        """Send package(s) to device and install them

        Args:
            path: Single or multiple packages and directories
            replace: If True, replace existing application
            shared: If True, install shared bundle for multi-apps

        Returns:
            stdout, stderr
        """
        cmd = ['install']
        if replace:
            cmd.append('-r')
        if shared:
            cmd.append('-s')
        cmd.append(path)
        return self.cmd(cmd, timeout=10)

    @adb_mapping(cmd='adb uninstall', refer_chain=_REFER_CHAIN, doc=f'{_DOC}commands')
    def uninstall(self, package: str, *, keep: bool = False, shared: bool = False) -> tuple[str, str]:
        """Remove application package from device

        Args:
            package: The package to uninstall.
            keep: If True, keep the data and cache directories.
            shared: If True, remove shared bundle.

        Returns:
            stdout, stderr
        """
        cmd = ['uninstall']
        if keep:
            cmd.append('-k')
        if shared:
            cmd.append('-s')
        cmd.append(package)
        return self.cmd(cmd, timeout=10)
