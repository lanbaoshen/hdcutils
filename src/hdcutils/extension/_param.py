from hdcutils import adb_mapping
from hdcutils.extension._base import ExtensionBase

_REFER_CHAIN = 'HDCClient().device().param'
_DOC = 'https://developer.huawei.com/consumer/en/doc/harmonyos-guides/param-tool#'


class Param(ExtensionBase):
    def cmd(self, cmd: list[str], timeout: int = 5) -> tuple[str, str]:
        """Execute a param command on device

        Args:
            cmd: The command to execute
            timeout: Timeout for the command execution in seconds

        Returns:
            stdout, stderr
        """
        return self._device.shell(['param'] + cmd, timeout=timeout)

    @adb_mapping(cmd='adb shell getprop', refer_chain=_REFER_CHAIN, doc=f'{_DOC}get')
    def get(self, name: str = None) -> tuple[str, str]:
        """Get system parameter

        Args:
            name: The name of the parameter to get, if not provided, all parameters will be returned.

        Returns:
            stdout, stderr
        """
        cmd = ['get']
        if name:
            cmd.append(name)
        return self.cmd(cmd)

    @adb_mapping(cmd='adb shell setprop', refer_chain=_REFER_CHAIN, doc=f'{_DOC}set-name-value')
    def set(self, name: str, value: str) -> tuple[str, str]:
        """Set system parameter

        Args:
            name: The name of the parameter to set.
            value: The value to set for the parameter.

        Returns:
            stdout, stderr
        """
        return self.cmd(['set', name, value])

    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=f'{_DOC}wait-name')
    def wait(self, name: str, value: str, timeout: int = 60) -> tuple[str, str]:
        """Wait system parameter

        Args:
            name: The name of the parameter to wait for.
            value: The value to wait for.
            timeout: The maximum time to wait in seconds.

        Returns:
            stdout, stderr
        """
        return self.cmd(['wait', name, value, str(timeout)])

    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=f'{_DOC}save')
    def save(self) -> tuple[str, str]:
        """Save all persist parameters in workspace

        Returns:
            stdout, stderr
        """
        return self.cmd(['save'])
