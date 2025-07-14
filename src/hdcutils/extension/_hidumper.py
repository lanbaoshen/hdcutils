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
            A tuple containing the standard output and standard error of the command.
        """
        return self._device.shell(['hidumper'] + cmd, timeout=timeout)

    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=_DOC)
    def display_manager_service(self) -> tuple[str, str]:
        """
        Get the Display information.

        Returns:
            A tuple containing the standard output and standard error of the command.
        """
        return self.cmd(['-s', 'DisplayManagerService', '-a', '-a'])
