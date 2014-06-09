"""
This is not needed to use vex.
It just lets us provide a convenient mechanism for people
with popular shells to set up autocompletion.
"""
import sys
import os

_HERE = os.path.dirname(os.path.abspath(__file__))

_BASH_CONFIG = b""
with open(os.path.join(_HERE, 'shell_configs', 'bash'), 'rb') as inp:
    _BASH_CONFIG = inp.read()

_ZSH_CONFIG = b""
with open(os.path.join(_HERE, 'shell_configs', 'zsh'), 'rb') as inp:
    _ZSH_CONFIG = inp.read()


_FISH_CONFIG = b""
with open(os.path.join(_HERE, 'shell_configs', 'fish'), 'rb') as inp:
    _FISH_CONFIG = inp.read()


def zsh_config(out, vexrc, environ):
    ve_base = vexrc.get_ve_base(environ).encode('ascii')
    if ve_base:
        data = _ZSH_CONFIG.replace(b'$WORKON_HOME', ve_base)
    else:
        data = _ZSH_CONFIG
    out.write(data)


def bash_config(out, vexrc, environ):
    ve_base = vexrc.get_ve_base(environ).encode('ascii')
    if ve_base:
        data = _BASH_CONFIG.replace(b'$WORKON_HOME', ve_base)
    else:
        data = _BASH_CONFIG
    out.write(data)


def fish_config(out, vexrc, environ):
    ve_base = vexrc.get_ve_base(environ).encode('ascii')
    if ve_base:
        data = _FISH_CONFIG.replace(b'$WORKON_HOME', ve_base)
    else:
        data = _FISH_CONFIG
    out.write(data)


_SHELLS = {
    'bash': bash_config,
    'zsh': zsh_config,
    'fish': fish_config,
}


def emit_shell_config_for(shell, vexrc, environ):
    function = _SHELLS.get(shell)
    if function:
        if hasattr(sys.stdout, 'buffer'):
            out = sys.stdout.buffer
        else:
            out = sys.stdout
        function(out, vexrc, environ)
