#!/usr/bin/python
#
# LICENSE: See LICENSE file.
#
# WARNING: The Windows/Linux iface by is EXPERIMENTAL and has nothing to do
#          with good coding, security, etc. USE AT YOUR OWN RISK.
#
import ifaceclientlib, sys
ifaceclientlib.LOG_LEVEL = ifaceclientlib.LOG_WARNING

# Check args.
if len(sys.argv) != 2:
  print "usage: if-l-runt.py <cmd>"
  sys.exit(1)

# Invoke.
cmd = sys.argv[1]
print ifaceclientlib.Invoke("iface-l-runt", cmd)


