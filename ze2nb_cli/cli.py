#!/usr/bin/env python3
import sys
import os
import argparse

from ze2nb import ze2nb

def run_all(out_path=None, to_html=False, to_py=False):
  for directory, folders, files in os.walk("."):
    for f in files:
      if f == "note.json":
        fullpath = os.path.join(directory, f)
        ze2nb(
            fullpath,
            out_path=out_path,
            to_html=to_html,
            to_py=to_py)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", help="The input file_name", type=str)
  parser.add_argument("--run-all", help="If set, walks through this directory and converts all note.json to ipynb", action="store_true")
  parser.add_argument("--out-path", help="Output path", type=str)
  parser.add_argument("--to-html", help="Converts to HTML", action="store_true")
  parser.add_argument("--to-py", help="Converts to .py", action="store_true")

  args = parser.parse_args()

  if not args.input and not args.run_all:
    raise Exception("One of `--input` or `--run-all` must be included")

  if args.run_all:
    run_all(
        out_path=args.out_path,
        to_html=args.to_html,
        to_py=args.to_py)
  else:
    ze2nb(
        args.input,
        out_path=args.out_path,
        to_html=args.to_html,
        to_py=args.to_py)


if __name__ == "__main__":
  main()
