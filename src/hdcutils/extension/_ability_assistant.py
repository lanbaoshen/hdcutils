from hdcutils import adb_mapping
from hdcutils.extension._base import ExtensionBase

_REFER_CHAIN = 'HDCClient().device().aa'
_DOC = 'https://developer.huawei.com/consumer/en/doc/harmonyos-guides/aa-tool#'


class AbilityAssistant(ExtensionBase):
    @adb_mapping(cmd='adb shell am', refer_chain=_REFER_CHAIN, doc=_DOC)
    def cmd(self, cmd: list[str], timeout: int = 5) -> tuple[str, str]:
        """Execute an ability assistant command on the device.

        Args:
            cmd: The command to execute, as a list of strings.
            timeout: Timeout for the command execution in seconds.

        Returns:
            stdout, stderr
        """
        return self._device.shell(['aa'] + cmd, timeout=timeout)

    @adb_mapping(cmd='adb shell am start', refer_chain=_REFER_CHAIN, doc=f'{_DOC}start-command')
    def start(self, bundle: str, *, ability: str = 'EntryAbility', timeout: int = 5) -> tuple[str, str]:
        """Start an ability in a specified bundle.

        Args:
            bundle: The name of the bundle.
            ability: The name of the ability to start.
            timeout: Timeout for the command execution in seconds.

        Returns:
            stdout, stderr
        """
        return self.cmd(['start', '-b', bundle, '-a', ability], timeout=timeout)

    @adb_mapping(cmd='adb shell am force-stop', refer_chain=_REFER_CHAIN, doc=f'{_DOC}force-stop-command')
    def force_stop(self, bundle: str, timeout: int = 5) -> tuple[str, str]:
        """Force stop a bundle.

        Args:
            bundle: The name of the bundle to force stop.
            timeout: Timeout for the command execution in seconds.

        Returns:
            stdout, stderr
        """
        return self.cmd(['force-stop', bundle], timeout=timeout)
