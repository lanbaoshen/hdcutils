from hdcutils import adb_mapping
from hdcutils.extension._base import ExtensionBase

_REFER_CHAIN = 'HDCClient().device().hidumper'
_DOC = 'https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hidumper#'


class HiDumper(ExtensionBase):
    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=_DOC)
    def cmd(self, cmd: list[str], timeout: int = 5) -> tuple[str, str]:
        """
        Execute a HiDumper command on the device.

        Args:
            cmd: The command to execute.
            timeout: The timeout for the command execution.

        Returns:
            stdout, stderr
        """
        return self._device.shell(['hidumper'] + cmd, timeout=timeout)

    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=_DOC)
    def display_manager_service(self) -> tuple[str, str]:
        """
        Get the Display information.

        Returns:
            stdout, stderr
        """
        return self.cmd(['-s', 'DisplayManagerService', '-a', '-a'])

    @adb_mapping(cmd='adb shell dumpsys activity', refer_chain=_REFER_CHAIN, doc=_DOC)
    def ability_manager_service(self) -> tuple[str, str]:
        """
        Get the AbilityManagerService information.

        Returns:
            stdout, stderr
        """
        return self.cmd(['-s', 'AbilityManagerService', '-a', '-l'])
