#!/usr/bin/python
#
# LICENSE: See LICENSE file.
#
# WARNING: The Windows/Linux iface by is EXPERIMENTAL and has nothing to do
#          with good coding, security, etc. USE AT YOUR OWN RISK.
#
import ifaceclientlib, sys, os
ifaceclientlib.LOG_LEVEL = ifaceclientlib.LOG_WARNING

# Check args.
if len(sys.argv) != 2:
  print "usage: if-l-run.py <cmd>"
  sys.exit(1)

# Invoke.
cmd = sys.argv[1]
cwd = ifaceclientlib.Invoke("translate-path", os.getcwd())
print ifaceclientlib.Invoke("iface-l-run", cmd, cwd)
