from hdcutils import adb_mapping
from hdcutils.extension._base import ExtensionBase

_REFER_CHAIN = 'HDCClient().device().bm'
_DOC = 'https://developer.huawei.com/consumer/en/doc/harmonyos-guides/bm-tool#'


class BundleManager(ExtensionBase):
    @adb_mapping(cmd='adb shell pm', refer_chain=_REFER_CHAIN, doc=_DOC)
    def cmd(self, cmd: list[str], timeout: int = 5) -> tuple[str, str]:
        """Execute a bundle manager command on the device.

        Args:
            cmd: The command to execute.
            timeout: The timeout for the command execution.

        Returns:
            stdout, stderr
        """
        return self._device.shell(['bm'] + cmd, timeout=timeout)

    @adb_mapping(cmd='adb shell pm list packages', refer_chain=_REFER_CHAIN, doc=f'{_DOC}dump')
    def dump_all_installed_bundles(self) -> tuple[str, str]:
        """Dump all bundles installed in the system.

        Returns:
            stdout, stderr
        """
        return self.cmd(['dump', '-a'])

    @adb_mapping(cmd='adb shell dumpsys package', refer_chain=_REFER_CHAIN, doc=f'{_DOC}dump')
    def dump_bundle(self, bundle: str, *, shortcut: bool = False):
        """Dump the details of a bundle

        Args:
            bundle: The name of the bundle to dump.
            shortcut: Displays the shortcut information.

        Returns:
            stdout, stderr
        """
        cmd = ['dump', '-n', bundle]
        if shortcut:
            cmd.append('-s')
        return self.cmd(cmd)

    @adb_mapping(cmd='adb shell pm clear', refer_chain=_REFER_CHAIN, doc=f'{_DOC}clean')
    def clean_cache(self, bundle: str) -> tuple[str, str]:
        """Clean the cache of a bundle.

        Args:
            bundle: The name of the bundle to clean.

        Returns:
            stdout, stderr
        """
        return self.cmd(['clean', '-c', '-n', bundle])

    @adb_mapping(cmd='adb shell pm clear', refer_chain=_REFER_CHAIN, doc=f'{_DOC}clean')
    def clean_data(self, bundle: str) -> tuple[str, str]:
        """Clean the data of a bundle.

        Args:
            bundle: The name of the bundle to clean.

        Returns:
            stdout, stderr
        """
        return self.cmd(['clean', '-d', '-n', bundle])

    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=f'{_DOC}clean')
    def get_udid(self) -> tuple[str, str]:
        """Obtains the UDID of a device

        Returns:
            stdout, stderr
        """
        return self.cmd(['get', '-u'])
