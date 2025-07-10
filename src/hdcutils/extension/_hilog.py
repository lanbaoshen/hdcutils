from typing import Literal

from loguru import logger

from hdcutils import adb_mapping
from hdcutils.extension._base import ExtensionBase

TYPE = Literal['app', 'core', 'init', 'kmsg', 'only_prerelease']
# X means that loggable level is higher than the max level, no log could be printed.
LEVEL = Literal['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL', 'X']


_REFER_CHAIN = 'HDCClient().device().hilog'
_DOC = 'https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hilog#'


class HiLog(ExtensionBase):
    @adb_mapping(cmd='adb logcat', refer_chain=_REFER_CHAIN, doc=_DOC)
    def cmd(self, cmd: list[str], timeout: int = 5) -> tuple[str, str]:
        return self._device.shell(['hilog'] + cmd, timeout)

    @staticmethod
    def _format_domain_id(domain: str) -> str:
        """Gen domain id base on domain string

        If user wants to use -D option to filter OS logs,
        user should add 0xD0 as prefix to the printed domain: `hilog -D 0xD0xxxxx`
        The xxxxx is the domain string printed in logs.

        Returns:
            The domain id with 0xD0 prefix.
        """
        return domain if domain.startswith('0xD0') else f'0xD0{domain}'

    @adb_mapping(cmd='adb logcat -c', refer_chain=_REFER_CHAIN, doc=f'{_DOC}clearing-the-log-buffer')
    def remove_buffer_log(self, types: list['TYPE'] = None) -> tuple[str, str]:
        """Remove log in buffer

        Args:
            types: Remove specific type log in buffer, defaults to ['app', 'core', 'only_prerelease'].

        Returns:
            stdout, stderr.
        """
        types = types or ['app', 'core', 'only_prerelease']
        return self.cmd(['-r', '-t', ','.join(types)])

    @adb_mapping(cmd='adb logcat -g', refer_chain=_REFER_CHAIN, doc=f'{_DOC}displaying-the-log-buffer-size')
    def query_buffer_size(self, types: list['TYPE'] = None) -> tuple[str, str]:
        """Query buffer size

        Args:
            types: The types to query size for, defaults to ['app', 'core', 'only_prerelease'].

        Returns:
            stdout, stderr.
        """
        types = types or ['app', 'core', 'only_prerelease']
        return self.cmd(['-g', '-t', ','.join(types)])

    @adb_mapping(cmd='adb logcat -G', refer_chain=_REFER_CHAIN, doc=f'{_DOC}setting-the-log-buffer-size')
    def set_buffer_size(
        self, *, types: list['TYPE'] = None, size: float | int, unit: Literal['B', 'K', 'M', 'G']
    ) -> tuple[str, str]:
        """Set buffer size

        Size range: [64.0K,16.0M]

        Args:
            types: The types to set size for, defaults to ['app', 'core', 'only_prerelease'].
            size: The size to set, must be a float or int.
            unit: The unit of the size, must be one of 'B', 'K', 'M', 'G'.

        Returns:
            stdout, stderr.
        """
        types = types or ['app', 'core', 'only_prerelease']
        return self.cmd(['-G', f'{size}{unit}', '-t', ','.join(types)])

    @adb_mapping(cmd='adb shell setprop log', refer_chain=_REFER_CHAIN, doc=f'{_DOC}displaying-and-setting-log-levels')
    def set_log_level(self, log_level: 'LEVEL', *, domain: str = None, tag: str = None) -> tuple[str, str]:
        """Set global loggable level

        The priority is: tag level > domain level > global level
        It's a temporary configuration, will be lost after reboot

        Args:
            log_level: The log level to set.
            domain: Set specific domain loggable level.
            tag: Set specific tag loggable level.

        Returns:
            stdout, stderr.
        """
        cmd = ['-b', log_level]
        if domain:
            cmd.extend(['-D', self._format_domain_id(domain)])
        if tag:
            cmd.extend(['-T', tag])
        return self.cmd(cmd)

    @adb_mapping(cmd='adb logcat', refer_chain=_REFER_CHAIN, doc=f'{_DOC}displaying-logs-of-a-specified-level')
    def non_block_read(
        self,
        *,
        read_mode: Literal['all', 'head', 'tail'] = 'all',
        lines: int = None,
        types: list['TYPE'] = None,
        levels: list['LEVEL'] = None,
        domains: list[str] = None,
        tags: list[str] = None,
        pids: list[int] = None,
        regex: str = None,
        timeout: int = 30,
    ) -> tuple[str, str]:
        """Performs a non-blocking read of HiLog logs.

        Args:
            read_mode:
                all: Performs a non-blocking read and exits when all logs in buffer are printed.
                head: Show n lines logs on head of buffer.
                tail: Show n lines logs on tail of buffer.
            lines: When read_mode is 'head' or 'tail', the number of lines to read.
            types: Show specific type/types log, defaults to ['app', 'core', 'init', 'only_prerelease'].
                kmsg can't combine with others
            levels: Show specific level/levels log
            domains: Show specific domain/domains log, max count is 5
            tags: Show specific tag/tags log, max count is 10
            pids: Show specific pid/pids log, max count is 5
            regex: Show the log which match the regular expression
            timeout: Timeout for the command execution in seconds.

        Returns:
            stdout, stderr.
        """
        cmd = []

        if read_mode != 'all' and lines is None:
            raise ValueError('lines must be specified when read_mode is not "all"')
        elif read_mode == 'all' and lines:
            logger.warning('lines is ignored when read_mode is "all"')

        if types and len(types) > 1 and 'kmsg' in types:
            raise ValueError('kmsg cannot be combined with other types')
        if domains and len(domains) > 5:
            raise ValueError('The max domain count is 5')
        if tags and len(tags) > 10:
            raise ValueError('The max tag count is 10')
        if pids and len(pids) > 5:
            raise ValueError('The max pid count is 5')

        match read_mode:
            case 'all':
                cmd.append('-x')
            case 'head':
                cmd += ['-a', str(lines)]
            case 'tail':
                cmd += ['-z', str(lines)]

        types = types or ['app', 'core', 'only_prerelease']
        cmd.extend(['-t', ','.join(types)])

        if levels:
            cmd.extend(['-b', ','.join(levels)])
        if domains:
            cmd.extend(['-D', ','.join([self._format_domain_id(domain) for domain in domains])])
        if tags:
            cmd.extend(['-T', ','.join(tags)])
        if pids:
            cmd.extend(['-P', ','.join(map(str, pids))])
        if regex:
            cmd.extend(['-R', regex])

        return self.cmd(cmd, timeout=timeout)
