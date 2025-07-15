from pathlib import Path, PurePath
from typing import TYPE_CHECKING

from hdcutils import adb_mapping
from hdcutils.extension import AbilityAssistant, BundleManager, HiDumper, HiLog, Param, PowerShell, UITest

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
        self._param = Param(self)
        self._power_shell = PowerShell(self)
        self._hidumper = HiDumper(self)

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

    @property
    def param(self) -> 'Param':
        return self._param

    @property
    def power_shell(self) -> 'PowerShell':
        return self._power_shell

    @property
    def hidumper(self) -> 'HiDumper':
        return self._hidumper

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
        cmd.append(str(path))
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

    @adb_mapping(cmd='adb push', refer_chain=_REFER_CHAIN, doc=f'{_DOC}commands')
    def file_send(self, *, local: str | Path, remote: str | PurePath, timeout: int = 60) -> tuple[str, str]:
        """Send file to device

        Args:
            local: Local path.
            remote: Remote path.
            timeout: Timeout for the operation in seconds.

        Returns:
            stdout, stderr
        """
        return self.cmd(['file', 'send', str(local), str(remote)], timeout=timeout)

    @adb_mapping(cmd='adb pull', refer_chain=_REFER_CHAIN, doc=f'{_DOC}commands')
    def file_recv(
        self, *, remote: str | PurePath, local: str | Path, hold_timestamp: bool = False, timeout: int = 60
    ) -> tuple[str, str]:
        """Receive file from device

        Args:
            remote: Remote path.
            local: Local path.
            hold_timestamp: hold target file timestamp
            timeout: Timeout for the operation in seconds.

        Returns:
            stdout, stderr
        """
        cmd = ['file', 'recv']
        if hold_timestamp:
            cmd.append('-a')
        cmd = cmd + [str(remote), str(local)]
        return self.cmd(cmd, timeout=timeout)

    @adb_mapping(cmd='adb wait-for-device', refer_chain=_REFER_CHAIN, doc=f'{_DOC}commands')
    def wait(self, timeout: int = 60) -> tuple[str, str]:
        return self.cmd(['wait'], timeout=timeout)

    @adb_mapping(cmd='adb reboot', refer_chain=_REFER_CHAIN, doc=f'{_DOC}commands')
    def boot(self) -> tuple[str, str]:
        """
        Reboot the device.

        Returns:
            stdout, stderr
        """
        return self.cmd(['target', 'boot'])

    @adb_mapping(cmd='adb shell screencap', refer_chain=_REFER_CHAIN, doc=f'{_DOC}commands')
    def snapshot_display(self, *, display_id: int = 0, path: PurePath = None) -> tuple[str, str]:
        """Take a snapshot of the specified display and save it to the given device path.

        Only support jpeg

        Args:
            display_id: The ID of the display to snapshot. Default is 0.
            path: The path on the device where the snapshot will be saved.
                If None, it will save to /data/local/tmp/

        Returns:
            stdout, stderr
        """
        cmd = ['snapshot_display', '-i', str(display_id)]
        if path:
            cmd.extend(['-f', str(path.with_suffix('.jpeg'))])

        return self.shell(cmd)
