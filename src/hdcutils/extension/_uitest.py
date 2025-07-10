from typing import Literal

from hdcutils import adb_mapping
from hdcutils.extension._base import ExtensionBase

_REFER_CHAIN = 'HDCClient().device().uitest'
_DOC = 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkxtest-guidelines#'


class _KeyEvent:
    FN: str = '0'  # Function (Fn) key.
    UNKNOWN: str = '-1'  # Unknown key.

    HOME: str = '1'  # Home key.
    BACK: str = '2'  # Back key.
    HEADSETHOOK: str = '6'  # Wired headset play/pause key.
    SEARCH: str = '9'  # Search key.

    MEDIA_PLAY_PAUSE: str = '10'  # Media key: Play/Pause.<br/>**Atomic Service API:** Supported in atomic services from API version 12.  # noqa:E501
    MEDIA_STOP: str = '11'  # Media key: Stop.<br/>**Atomic Service API:** Supported in atomic services from API version 12.  # noqa:E501
    MEDIA_NEXT: str = '12'  # Media key: Next.<br/>**Atomic Service API:** Supported in atomic services from API version 12.  # noqa:E501
    MEDIA_PREVIOUS: str = '13'  # Media key: Previous.<br/>**Atomic Service API:** Supported in atomic services from API version 12.  # noqa:E501
    MEDIA_REWIND: str = '14'  # Media key: Rewind.<br/>**Atomic Service API:** Supported in atomic services from API version 12.  # noqa:E501
    MEDIA_FAST_FORWARD: str = '15'  # Media key: Fast forward.<br/>**Atomic Service API:** Supported in atomic services from API version 12.  # noqa:E501

    VOLUME_UP: str = '16'  # Volume up key.
    VOLUME_DOWN: str = '17'  # Volume down key.
    POWER: str = '18'  # Power key.
    CAMERA: str = '19'  # Camera key.
    VOLUME_MUTE: str = '22'  # Speaker mute key.
    MUTE: str = '23'  # Microphone mute key.

    BRIGHTNESS_UP: str = '40'  # Brightness adjustment key: Increase brightness.
    BRIGHTNESS_DOWN: str = '41'  # Brightness adjustment key: Decrease brightness.

    NUM_0: str = '2000'  # Key '0'.
    KEY_1: str = '2001'  # Key '1'.
    KEY_2: str = '2002'  # Key '2'.
    KEY_3: str = '2003'  # Key '3'.
    KEY_4: str = '2004'  # Key '4'.
    KEY_5: str = '2005'  # Key '5'.
    KEY_6: str = '2006'  # Key '6'.
    KEY_7: str = '2007'  # Key '7'.
    KEY_8: str = '2008'  # Key '8'.
    KEY_9: str = '2009'  # Key '9'.
    STAR: str = '2010'  # Key '*'.
    POUND: str = '2011'  # Key '#'.

    DPAD_UP: str = '2012'  # Navigation key: Up.
    DPAD_DOWN: str = '2013'  # Navigation key: Down.
    DPAD_LEFT: str = '2014'  # Navigation key: Left.
    DPAD_RIGHT: str = '2015'  # Navigation key: Right.
    DPAD_CENTER: str = '2016'  # Navigation key: Confirm.

    A: str = '2017'  # Key 'A'.
    B: str = '2018'  # Key 'B'.
    C: str = '2019'  # Key 'C'.
    D: str = '2020'  # Key 'D'.
    E: str = '2021'  # Key 'E'.
    F: str = '2022'  # Key 'F'.
    G: str = '2023'  # Key 'G'.
    H: str = '2024'  # Key 'H'.
    I: str = '2025'  # Key 'I'.
    J: str = '2026'  # Key 'J'.
    K: str = '2027'  # Key 'K'.
    L: str = '2028'  # Key 'L'.
    M: str = '2029'  # Key 'M'.
    N: str = '2030'  # Key 'N'.
    O: str = '2031'  # Key 'O'.
    P: str = '2032'  # Key 'P'.
    Q: str = '2033'  # Key 'Q'.
    R: str = '2034'  # Key 'R'.
    S: str = '2035'  # Key 'S'.
    T: str = '2036'  # Key 'T'.
    U: str = '2037'  # Key 'U'.
    V: str = '2038'  # Key 'V'.
    W: str = '2039'  # Key 'W'.
    X: str = '2040'  # Key 'X'.
    Y: str = '2041'  # Key 'Y'.
    Z: str = '2042'  # Key 'Z'.
    COMMA: str = '2043'  # Key ','.
    PERIOD: str = '2044'  # Key '.'.

    ALT_LEFT: str = '2045'  # Left Alt key.
    ALT_RIGHT: str = '2046'  # Right Alt key.
    SHIFT_LEFT: str = '2047'  # Left Shift key.
    SHIFT_RIGHT: str = '2048'  # Right Shift key.
    TAB: str = '2049'  # Tab key.
    SPACE: str = '2050'  # Space key.
    SYM: str = '2051'  # Symbol modifier key.
    EXPLORER: str = '2052'  # Browser function key, used to launch the browser application.
    ENVELOPE: str = '2053'  # Email function key, used to launch the email application.

    ENTER: str = '2054'  # Enter key.
    DEL: str = '2055'  # Backspace key.
    GRAVE: str = '2056'  # Key '`'.
    MINUS: str = '2057'  # Key '-'.
    EQUALS: str = '2058'  # Key: str =.
    LEFT_BRACKET: str = '2059'  # Key '['.
    RIGHT_BRACKET: str = '2060'  # Key ']'.
    BACKSLASH: str = '2061'  # Key '\'.
    SEMICOLON: str = '2062'  # Key ';'.
    APOSTROPHE: str = '2063'  # Key ''' (single quote).
    SLASH: str = '2064'  # Key '/'.
    AT: str = '2065'  # Key '@'.
    PLUS: str = '2066'  # Key '+'.

    MENU: str = '2067'  # Menu key.
    PAGE_UP: str = '2068'  # Page up key.
    PAGE_DOWN: str = '2069'  # Page down key.
    ESCAPE: str = '2070'  # Esc key.
    FORWARD_DEL: str = '2071'  # Delete key.
    CTRL_LEFT: str = '2072'  # Left Ctrl key.
    CTRL_RIGHT: str = '2073'  # Right Ctrl key.
    CAPS_LOCK: str = '2074'  # Caps Lock key.
    SCROLL_LOCK: str = '2075'  # Scroll Lock key.
    META_LEFT: str = '2076'  # Left Meta key.
    META_RIGHT: str = '2077'  # Right Meta key.
    FUNCTION: str = '2078'  # Function key.
    SYSRQ: str = '2079'  # System request/Print Screen key.
    BREAK: str = '2080'  # Break/Pause key.

    MOVE_HOME: str = '2081'  # Move cursor to start key.
    MOVE_END: str = '2082'  # Move cursor to end key.
    INSERT: str = '2083'  # Insert key.
    FORWARD: str = '2084'  # Forward key.

    MEDIA_PLAY: str = '2085'  # Media key: Play.<br/>**Atomic Service API:** Supported in atomic services from API version 12.  # noqa:E501
    MEDIA_PAUSE: str = '2086'  # Media key: Pause.<br/>**Atomic Service API:** Supported in atomic services from API version 12.  # noqa:E501
    MEDIA_CLOSE: str = '2087'  # Media key: Close.
    MEDIA_EJECT: str = '2088'  # Media key: Eject.
    MEDIA_RECORD: str = '2089'  # Media key: Record.

    F1: str = '2090'  # Key 'F1'.
    F2: str = '2091'  # Key 'F2'.
    F3: str = '2092'  # Key 'F3'.
    F4: str = '2093'  # Key 'F4'.
    F5: str = '2094'  # Key 'F5'.
    F6: str = '2095'  # Key 'F6'.
    F7: str = '2096'  # Key 'F7'.
    F8: str = '2097'  # Key 'F8'.
    F9: str = '2098'  # Key 'F9'.
    F10: str = '2099'  # Key 'F10'.
    F11: str = '2100'  # Key 'F11'.
    F12: str = '2101'  # Key 'F12'.

    NUM_LOCK: str = '2102'  # Num Lock key.
    NUMPAD_0: str = '2103'  # Numpad key '0'.
    NUMPAD_1: str = '2104'  # Numpad key '1'.
    NUMPAD_2: str = '2105'  # Numpad key '2'.
    NUMPAD_3: str = '2106'  # Numpad key '3'.
    NUMPAD_4: str = '2107'  # Numpad key '4'.
    NUMPAD_5: str = '2108'  # Numpad key '5'.
    NUMPAD_6: str = '2109'  # Numpad key '6'.
    NUMPAD_7: str = '2110'  # Numpad key '7'.
    NUMPAD_8: str = '2111'  # Numpad key '8'.
    NUMPAD_9: str = '2112'  # Numpad key '9'.
    NUMPAD_DIVIDE: str = '2113'  # Numpad key '/'.
    NUMPAD_MULTIPLY: str = '2114'  # Numpad key '*'.
    NUMPAD_SUBTRACT: str = '2115'  # Numpad key '-'.
    NUMPAD_ADD: str = '2116'  # Numpad key '+'.
    NUMPAD_DOT: str = '2117'  # Numpad key '.'.
    NUMPAD_COMMA: str = '2118'  # Numpad key ','.
    NUMPAD_ENTER: str = '2119'  # Numpad Enter key.
    NUMPAD_EQUALS: str = '2120'  # Numpad key: str =.
    NUMPAD_LEFT_PAREN: str = '2121'  # Numpad key '('.
    NUMPAD_RIGHT_PAREN: str = '2122'  # Numpad key ')'.

    VIRTUAL_MULTITASK: str = '2210'  # Virtual multitasking key.

    BUTTON_A: str = '2301'  # Gamepad button 'A'.
    BUTTON_B: str = '2302'  # Gamepad button 'B'.
    BUTTON_X: str = '2304'  # Gamepad button 'X'.
    BUTTON_Y: str = '2305'  # Gamepad button 'Y'.
    BUTTON_L1: str = '2307'  # Gamepad button 'L1'.
    BUTTON_R1: str = '2308'  # Gamepad button 'R1'.
    BUTTON_L2: str = '2309'  # Gamepad button 'L2'.
    BUTTON_R2: str = '2310'  # Gamepad button 'R2'.

    BUTTON_SELECT: str = '2311'  # Gamepad button 'Select'.
    BUTTON_START: str = '2312'  # Gamepad button 'Start'.
    BUTTON_MODE: str = '2313'  # Gamepad button 'Mode'.
    BUTTON_THUMBL: str = '2314'  # Gamepad button 'THUMBL'.
    BUTTON_THUMBR: str = '2315'  # Gamepad button 'THUMBR'.
    SLEEP: str = '2600'  # Sleep key.
    ZENKAKU_HANKAKU: str = '2601'  # Japanese full-width/half-width key.
    RO: str = '2603'  # Japanese Ro key.
    KATAKANA: str = '2604'  # Japanese Katakana key.
    HIRAGANA: str = '2605'  # Japanese Hiragana key.
    HENKAN: str = '2606'  # Japanese conversion key.
    KATAKANA_HIRAGANA: str = '2607'  # Japanese Katakana/Hiragana key.
    MUHENKAN: str = '2608'  # Japanese non-conversion key.
    LINEFEED: str = '2609'  # Line feed key.
    MACRO: str = '2610'  # Macro key.
    NUMPAD_PLUSMINUS: str = '2611'  # Plus/minus key on the numpad.
    SCALE: str = '2612'  # Scale key.
    HANGUEL: str = '2613'  # Japanese Hangul key.
    HANJA: str = '2614'  # Japanese Hanja key.
    YEN: str = '2615'  # Yen key.
    STOP: str = '2616'  # Stop key.
    AGAIN: str = '2617'  # Repeat key.
    PROPS: str = '2618'  # Props key.
    UNDO: str = '2619'  # Undo key.
    COPY: str = '2620'  # Copy key.
    OPEN: str = '2621'  # Open key.
    PASTE: str = '2622'  # Paste key.
    FIND: str = '2623'  # Find key.
    CUT: str = '2624'  # Cut key.
    HELP: str = '2625'  # Help key.
    CALC: str = '2626'  # Calculator special function key, used to launch the calculator application.
    FILE: str = '2627'  # File key.
    BOOKMARKS: str = '2628'  # Bookmarks key.
    NEXT: str = '2629'  # Next key.
    PLAYPAUSE: str = '2630'  # Play/Pause key.
    PREVIOUS: str = '2631'  # Previous key.
    STOPCD: str = '2632'  # CD stop key.
    CONFIG: str = '2634'  # Config key.
    REFRESH: str = '2635'  # Refresh key.
    EXIT: str = '2636'  # Exit key.
    EDIT: str = '2637'  # Edit key.
    SCROLLUP: str = '2638'  # Scroll up key.
    SCROLLDOWN: str = '2639'  # Scroll down key.
    NEW: str = '2640'  # New key.
    REDO: str = '2641'  # Redo key.
    CLOSE: str = '2642'  # Close key.
    PLAY: str = '2643'  # Play key.
    BASSBOOST: str = '2644'  # Bass boost key.
    PRINT: str = '2645'  # Print key.
    CHAT: str = '2646'  # Chat key.
    FINANCE: str = '2647'  # Finance key.
    CANCEL: str = '2648'  # Cancel key.
    KBDILLUM_TOGGLE: str = '2649'  # Keyboard backlight toggle key.
    KBDILLUM_DOWN: str = '2650'  # Keyboard backlight dim key.
    KBDILLUM_UP: str = '2651'  # Keyboard backlight brighten key.
    SEND: str = '2652'  # Send key.
    REPLY: str = '2653'  # Reply key.
    FORWARDMAIL: str = '2654'  # Forward mail key.
    SAVE: str = '2655'  # Save key.
    DOCUMENTS: str = '2656'  # Documents key.
    VIDEO_NEXT: str = '2657'  # Next video key.
    VIDEO_PREV: str = '2658'  # Previous video key.
    BRIGHTNESS_CYCLE: str = '2659'  # Backlight cycle key.
    BRIGHTNESS_ZERO: str = '2660'  # Brightness set to zero key.
    DISPLAY_OFF: str = '2661'  # Display off key.
    BTN_MISC: str = '2662'  # Miscellaneous buttons on the gamepad.
    GOTO: str = '2663'  # Go to key.
    INFO: str = '2664'  # Info key.
    PROGRAM: str = '2665'  # Program key.
    PVR: str = '2666'  # Personal Video Recorder (PVR) key.
    SUBTITLE: str = '2667'  # Subtitle key.
    FULL_SCREEN: str = '2668'  # Full screen key.
    KEYBOARD: str = '2669'  # Keyboard.
    ASPECT_RATIO: str = '2670'  # Screen aspect ratio adjustment key.
    PC: str = '2671'  # Port control key.
    TV: str = '2672'  # TV key.
    TV2: str = '2673'  # TV key 2.
    VCR: str = '2674'  # VCR key.
    VCR2: str = '2675'  # VCR key 2.
    SAT: str = '2676'  # SIM Application Toolkit (SAT) key.
    CD: str = '2677'  # CD key.
    TAPE: str = '2678'  # Tape key.
    TUNER: str = '2679'  # Tuner key.
    PLAYER: str = '2680'  # Player key.
    DVD: str = '2681'  # DVD key.
    AUDIO: str = '2682'  # Audio key.
    VIDEO: str = '2683'  # Video key.
    MEMO: str = '2684'  # Memo key.
    CALENDAR: str = '2685'  # Calendar key.
    RED: str = '2686'  # Red indicator.
    GREEN: str = '2687'  # Green indicator.
    YELLOW: str = '2688'  # Yellow indicator.
    BLUE: str = '2689'  # Blue indicator.
    CHANNELUP: str = '2690'  # Channel up key.
    CHANNELDOWN: str = '2691'  # Channel down key.
    LAST: str = '2692'  # Last key.
    RESTART: str = '2693'  # Restart key.
    SLOW: str = '2694'  # Slow key.
    SHUFFLE: str = '2695'  # Shuffle key.
    VIDEOPHONE: str = '2696'  # Video phone key.
    GAMES: str = '2697'  # Games key.
    ZOOMIN: str = '2698'  # Zoom in key.
    ZOOMOUT: str = '2699'  # Zoom out key.
    ZOOMRESET: str = '2700'  # Zoom reset key.
    WORDPROCESSOR: str = '2701'  # Word processor key.
    EDITOR: str = '2702'  # Editor key.
    SPREADSHEET: str = '2703'  # Spreadsheet key.
    GRAPHICSEDITOR: str = '2704'  # Graphics editor key.
    PRESENTATION: str = '2705'  # Presentation key.
    DATABASE: str = '2706'  # Database key.
    NEWS: str = '2707'  # News key.
    VOICEMAIL: str = '2708'  # Voicemail.
    ADDRESSBOOK: str = '2709'  # Address book.
    MESSENGER: str = '2710'  # Messenger key.
    BRIGHTNESS_TOGGLE: str = '2711'  # Brightness toggle key.
    SPELLCHECK: str = '2712'  # AL spell check.
    COFFEE: str = '2713'  # Terminal lock/screensaver.
    MEDIA_REPEAT: str = '2714'  # Media repeat key.
    IMAGES: str = '2715'  # Images key.
    BUTTONCONFIG: str = '2716'  # Button config key.
    TASKMANAGER: str = '2717'  # Task manager.
    JOURNAL: str = '2718'  # Journal key.
    CONTROLPANEL: str = '2719'  # Control panel key.
    APPSELECT: str = '2720'  # App select key.
    SCREENSAVER: str = '2721'  # Screensaver key.
    ASSISTANT: str = '2722'  # Smart key.
    KBD_LAYOUT_NEXT: str = '2723'  # Next keyboard layout key.
    BRIGHTNESS_MIN: str = '2724'  # Minimum brightness key.
    BRIGHTNESS_MAX: str = '2725'  # Maximum brightness key.
    KBDINPUTASSIST_PREV: str = '2726'  # Keyboard input Assist_Previous, view input method history.
    KBDINPUTASSIST_NEXT: str = '2727'  # Keyboard input Assist_Next, view input method extensions.
    KBDINPUTASSIST_PREVGROUP: str = '2728'  # Keyboard input Assist_Previous, switch to previous input method in group.
    KBDINPUTASSIST_NEXTGROUP: str = '2729'  # Keyboard input Assist_Next, switch to next input method in group.
    KBDINPUTASSIST_ACCEPT: str = '2730'  # Keyboard input Assist_Accept.
    KBDINPUTASSIST_CANCEL: str = '2731'  # Keyboard input Assist_Cancel.
    FRONT: str = '2800'  # Windshield defroster switch.
    SETUP: str = '2801'  # Setup key.
    WAKEUP: str = '2802'  # Wakeup key.
    SENDFILE: str = '2803'  # Send file key.
    DELETEFILE: str = '2804'  # Delete file key.
    XFER: str = '2805'  # File transfer (XFER) key.
    PROG1: str = '2806'  # Program key 1.
    PROG2: str = '2807'  # Program key 2.
    MSDOS: str = '2808'  # MS-DOS key (Microsoft Disk Operating System).
    SCREENLOCK: str = '2809'  # Screen lock key.
    DIRECTION_ROTATE_DISPLAY: str = '2810'  # Direction rotate display key.
    CYCLEWINDOWS: str = '2811'  # Windows cycle key.
    COMPUTER: str = '2812'  # Key.
    EJECTCLOSECD: str = '2813'  # Eject CD key.
    ISO: str = '2814'  # ISO key.
    MOVE: str = '2815'  # Move key.
    F13: str = '2816'  # Key 'F13'.
    F14: str = '2817'  # Key 'F14'.
    F15: str = '2818'  # Key 'F15'.
    F16: str = '2819'  # Key 'F16'.
    F17: str = '2820'  # Key 'F17'.
    F18: str = '2821'  # Key 'F18'.
    F19: str = '2822'  # Key 'F19'.
    F20: str = '2823'  # Key 'F20'.
    F21: str = '2824'  # Key 'F21'.
    F22: str = '2825'  # Key 'F22'.
    F23: str = '2826'  # Key 'F23'.
    F24: str = '2827'  # Key 'F24'.
    PROG3: str = '2828'  # Program key 3.
    PROG4: str = '2829'  # Program key 4.
    DASHBOARD: str = '2830'  # Dashboard.
    SUSPEND: str = '2831'  # Suspend key.
    HP: str = '2832'  # High-order path key.
    SOUND: str = '2833'  # Volume key.
    QUESTION: str = '2834'  # Question key.
    CONNECT: str = '2836'  # Connect key.
    SPORT: str = '2837'  # Sport key.
    SHOP: str = '2838'  # Shop key.
    ALTERASE: str = '2839'  # Alternate key.
    SWITCHVIDEOMODE: str = '2841'  # Cycle between available video outputs (monitor/LCD/TV-out/etc.).
    BATTERY: str = '2842'  # Battery key.
    BLUETOOTH: str = '2843'  # Bluetooth key.
    WLAN: str = '2844'  # Wireless LAN.
    UWB: str = '2845'  # Ultra-wideband (UWB).
    WWAN_WIMAX: str = '2846'  # WWAN WiMAX key.
    RFKILL: str = '2847'  # Key to control all radios.
    CHANNEL: str = '3001'  # Channel up key.
    BTN_0: str = '3100'  # Button 0.
    BTN_1: str = '3101'  # Button 1.
    BTN_2: str = '3102'  # Button 2.
    BTN_3: str = '3103'  # Button 3.
    BTN_4: str = '3104'  # Button 4.
    BTN_5: str = '3105'  # Button 5.
    BTN_6: str = '3106'  # Button 6.
    BTN_7: str = '3107'  # Button 7.
    BTN_8: str = '3108'  # Button 8.
    BTN_9: str = '3109'  # Button 9.
    DAGGER_CLICK: str = '3211'  # Smartwatch smart window button click.
    DAGGER_DOUBLE_CLICK: str = '3212'  # Smartwatch smart window button double-click.
    DAGGER_LONG_PRESS: str = '3213'  # Smartwatch smart window button long press.
    DIV: str = '3220'  # Smartwatch left button, only supported on smart wearable devices.


class UITest(ExtensionBase):
    def cmd(self, cmd: list[str], timeout: int = 5) -> tuple[str, str]:
        return self._device.shell(['uitest'] + cmd, timeout)

    @property
    def keyevent(self) -> type[_KeyEvent]:
        return _KeyEvent

    @adb_mapping(cmd='adb shell input text', refer_chain=_REFER_CHAIN, doc=f'{_DOC}injecting-simulated-ui-operations')
    def input_text(self, text: str, *, x: float | int, y: float | int) -> tuple[str, str]:
        """Input text at the current focus or at specified coordinates.

        If `x` and `y` are provided, the text will be input at the specified coordinates.

        Args:
            text: The text to input.
            x: The x coordinate.
            y: The y coordinate.

        Returns:
            stdout, stderr
        """
        # TODO: Although the documentation allows text to be entered directly,
        # TODO: the current hdc version does not support it.
        if x is not None and y is not None:
            return self.cmd(['uiInput', 'inputText', str(x), str(y), text])
        return self.cmd(['uiInput', 'text', text])

    @adb_mapping(
        cmd='adb shell input keyevent',
        refer_chain=_REFER_CHAIN,
        doc=f'{_DOC}injecting-simulated-ui-operations, https://gitee.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-input-kit/js-apis-keycode.md',
    )
    def inject_keyevent(self, keyevent: str | list[str]) -> tuple[str, str]:
        """Inject keyevent into the system.

        You can use self.keyevent.X to access predefined key events.

        Args:
            keyevent: A single keyevent string or a list of keyevent strings to inject. Max length is 3.

        Returns:
            stdout, stderr

        Examples:
            d.uitest.inject_keyevent(d.uitest.keyevent.HOME)
        """
        if isinstance(keyevent, list):
            if len(keyevent) > 3:
                raise ValueError('Max length of keyevent is 3.')
            return self.cmd(['uiInput', 'keyEvent'] + keyevent)
        return self.cmd(['uiInput', 'keyEvent', keyevent])

    @adb_mapping(cmd='adb shell input tap', refer_chain=_REFER_CHAIN, doc=f'{_DOC}injecting-simulated-ui-operations')
    def click(
        self, x: float | int, y: float | int, *, mode: Literal['single', 'double', 'long'] = 'single'
    ) -> tuple[str, str]:
        """Click at the specified coordinates.

        Args:
            x: The x coordinate.
            y: The y coordinate.
            mode: Set the click mode, supports 'single', 'double', and 'long'.

        Returns:
            stdout, stderr
        """
        match mode:
            case 'single':
                return self.cmd(['uiInput', 'click', str(x), str(y)])
            case 'double':
                return self.cmd(['uiInput', 'doubleClick', str(x), str(y)])
            case 'long':
                return self.cmd(['uiInput', 'longClick', str(x), str(y)])
            case _:
                raise ValueError(f'Invalid click mode: {mode}. Supported modes are: single, double, long.')

    @adb_mapping(cmd='adb shell input swipe', refer_chain=_REFER_CHAIN, doc=f'{_DOC}injecting-simulated-ui-operations')
    def swipe(
        self,
        from_x: float | int,
        from_y: float | int,
        to_x: float | int,
        to_y: float | int,
        velocity: int = 600,
    ) -> tuple[str, str]:
        """Swipe from one point to another with a specified velocity.

        Args:
            from_x: Starting X coordinate of the swipe.
            from_y: Starting Y coordinate of the swipe.
            to_x: Ending X coordinate of the swipe.
            to_y: Ending Y coordinate of the swipe.
            velocity: Velocity of the swipe, ranges from 200 to 40000, default is 600.

        Returns:
            stdout, stderr
        """
        return self.cmd(['uiInput', 'swipe', str(from_x), str(from_y), str(to_x), str(to_y), str(velocity)])

    @adb_mapping(
        cmd='adb shell input draganddrop', refer_chain=_REFER_CHAIN, doc=f'{_DOC}injecting-simulated-ui-operations'
    )
    def drag(
        self,
        from_x: float | int,
        from_y: float | int,
        to_x: float | int,
        to_y: float | int,
        velocity: int = 600,
    ) -> tuple[str, str]:
        """Drag one point to another with a specified velocity.

        Args:
            from_x: Starting X coordinate of the drag.
            from_y: Starting Y coordinate of the drag.
            to_x: Ending X coordinate of the drag.
            to_y: Ending Y coordinate of the drag.
            velocity: Velocity of the drag, ranges from 200 to 40000, default is 600.

        Returns:
            stdout, stderr
        """
        return self.cmd(['uiInput', 'drag', str(from_x), str(from_y), str(to_x), str(to_y), str(velocity)])

    @adb_mapping(cmd='todo', refer_chain=_REFER_CHAIN, doc=f'{_DOC}injecting-simulated-ui-operations')
    def fling(
        self,
        from_x: float | int,
        from_y: float | int,
        to_x: float | int,
        to_y: float | int,
        velocity: int = 600,
    ) -> tuple[str, str]:
        """Fling from one point to another with a specified velocity.

        Args:
            from_x: Starting X coordinate of the fling.
            from_y: Starting Y coordinate of the fling.
            to_x: Ending X coordinate of the fling.
            to_y: Ending Y coordinate of the fling.
            velocity: Velocity of the fling, ranges from 200 to 40000, default is 600.

        Returns:
            stdout, stderr
        """
        return self.cmd(['uiInput', 'fling', str(from_x), str(from_y), str(to_x), str(to_y), str(velocity)])

    @adb_mapping(cmd='adb shell input roll', refer_chain=_REFER_CHAIN, doc=f'{_DOC}injecting-simulated-ui-operations')
    def dirc_fling(self, direction: Literal['left', 'right', 'up', 'down'], velocity: int = 600) -> tuple[str, str]:
        """Fling in a specified direction with a specified velocity.

        Args:
            direction: The direction to fling, can be 'left', 'right', 'up', or 'down'.
            velocity: Velocity of the fling, ranges from 200 to 40000, default is 600.

        Returns:
            stdout, stderr
        """
        match direction:
            case 'left':
                direction = '0'
            case 'right':
                direction = '1'
            case 'up':
                direction = '2'
            case 'down':
                direction = '3'
            case _:
                raise ValueError(f'Invalid direction: {direction}. Supported directions are: left, right, up, down.')

        return self.cmd(['uiInput', 'dircFling', direction, str(velocity)])
