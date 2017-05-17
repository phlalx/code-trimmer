#!/usr/bin/python3

import os
import re
import argparse

def _process(filename, destdir, verbose):
  if verbose:
    print('processing:', filename)
  num_cut = 0
  try:
    srcfile = open(filename, 'r')
  except OSError:
    print('cannot open', filename)
    exit(1)
  destfile = open(destdir + '/' + filename, 'w')
  do_cut = False
  for l in srcfile:
    if 'START CUT' in l:
      do_cut = True
      num_cut += 1
      continue
    if 'END CUT' in l:
      if not do_cut:
        _die('END CUT not preceded by START CUT')
      do_cut = False
      num_cut += 1
      continue
    if 'UNCOMMENT' in l:
      # remove anything before UNCOMMENT, but keep indentation
      l = re.sub(r'[^ \t].*UNCOMMENT[ \t]*', '', l)
    if not do_cut:
      destfile.write(l)
    else:
      num_cut += 1
  if verbose:
    print('  number of lines cut', num_cut)

default_dest = 'skel'

def main():
  parser = argparse.ArgumentParser(description = 
    'Code trimmer. Cut part of the code based on comment annotations')
  parser.add_argument("files", metavar="FILE", help="file to be processed", 
                      nargs='+')
  parser.add_argument("-o", dest='destination', metavar="DIR", 
                      help="set destination directory to DIR. Default is '" + 
                           default_dest + "'", default=default_dest)
  parser.add_argument("-v", dest='verbose', action='store_true', 
                      help='verbose mode')
  parser.add_argument("-f", dest='force', action='store_true', 
                      help='overwrite existing directory')
  args = parser.parse_args()
  destdir = args.destination
  verbose = args.verbose
  if os.path.exists(destdir):
    if not args.force:
      print(destdir, "exists already. Delete it or use -f option.")
      exit(1)
  else:
    os.makedirs(destdir)
  if verbose:
    print('destination:', destdir)
  for f in args.files:
    _process(f, destdir, verbose)

if __name__ == "__main__":
    main()