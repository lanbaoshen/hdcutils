from typing import Literal

from hdcutils import adb_mapping
from hdcutils.extension._base import ExtensionBase

_REFER_CHAIN = 'HDCClient().device().power_shell'
_DOC = 'https://developer.huawei.com/consumer/en/doc/harmonyos-guides/power-shell#'


class PowerShell(ExtensionBase):
    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=_DOC)
    def cmd(self, cmd: list[str], timeout: int = 5) -> tuple[str, str]:
        """
        Execute a PowerShell command on the device.

        Args:
            cmd: The command to execute.
            timeout: The timeout for the command execution.

        Returns:
            stdout, stderr
        """
        return self._device.shell(['power-shell'] + cmd, timeout=timeout)

    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=f'{_DOC}setmode')
    def setmode(self, mode: Literal['normal', 'power-saving', 'perf', 'ultra-power-saving']) -> tuple[str, str]:
        """
        Set the power mode

        Args:
            mode: The power mode to set. Must be one of 'normal', 'power-saving', 'perf', or 'ultra-power-saving'.

        Returns:
            stdout, stderr
        """
        cmd = ['setmode']
        match mode:
            case 'normal':
                cmd.append('600')
            case 'power-saving':
                cmd.append('601')
            case 'perf':
                cmd.append('602')
            case 'ultra-power-saving':
                cmd.append('603')
            case _:
                raise ValueError(
                    f'Invalid mode: {mode}. Must be one of "normal", "power-saving", "perf", or "ultra-power-saving".'
                )
        return self.cmd(cmd)

    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=f'{_DOC}wakeup')
    def wakeup(self) -> tuple[str, str]:
        """
        Turns on the screen.

        Returns:
            stdout, stderr
        """
        return self.cmd(['wakeup'])

    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=f'{_DOC}suspend')
    def suspend(self) -> tuple[str, str]:
        """
        Turns off the screen.

        Returns:
            stdout, stderr
        """
        return self.cmd(['suspend'])

    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=f'{_DOC}timeout')
    def timeout(self, time: int) -> tuple[str, str]:
        """
        Set the screen timeout.

        Args:
            time: The timeout in milliseconds.

        Returns:
            stdout, stderr
        """
        return self.cmd(['timeout', '-o', str(time)])

    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=f'{_DOC}timeout')
    def restore_timeout(self):
        """
        Restores the automatic screen-off time in the current system settings.

        Returns:
            stdout, stderr
        """
        return self.cmd(['timeout', '-r'])
