#!/usr/bin/python -tt

"""
Main driver class for pyDropper a python based shellcode encryption, packaging, and 
executable dropper creation program.
"""

import argparse
import os

def get_OS():
  """
  Gets the OS that being used to execute the program.
  """
  # Determine OS and load correct lib
  if os.name == 'WinNT':
    from lib.windows import packer
  elif os.name == 'posix':
    from lib.linux import packer
    exe = packer('a', True)
    print exe
  else:
    print "[-] Error pyDropper does not support the creation of dropper executables on your system."

def main():
  """
  Main function in program called on program execution.
  """
  # Create command line argument parser.
  parser = argparse.ArgumentParser(description="PyDropper a shellcode encryption, packaging, and executable dropper creation program", version=('%(prog)s 0.1'))
  parser.add_argument('-p', '--password', action='store', dest="enc_password", help="Password used to encrypt the shellcode. The password will be stored in the dropper executable(Optional)")
  parser.add_argument('-r', '--random', action='store_true', default=False, dest="use_random_password", help="Have the program use a random password to ecrypt the shellcode. The decryption password will be bruteforced at run time, and is not stored in the executable. (Default)")

  # Parse the command line arguments.
  args = parser.parse_args()

  # Handle the no argument case
  if not args.enc_password and not args.use_random_password:
    parser.print_help()

  # If encryption password was given use that else fall back to a random 
  if args.enc_password:
    # Check for OS
    get_OS()

  # Parse the command line arguments.
  args = parser.parse_args()

  # Handle command line arguments and encrypt the shellcode


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()