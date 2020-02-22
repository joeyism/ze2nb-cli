
ze2nb CLI
=========

Installation
------------

.. code-block:: bash

   pip3 install ze2nb-cli

Usage
-----

.. code-block:: bash

   usage: ze2nb [-h] [-i INPUT] [--run-all] [--out-path OUT_PATH] [--to-html]
                [--to-py]

   optional arguments:
     -h, --help            show this help message and exit
     -i INPUT, --input INPUT
                           The input file_name
     --run-all             If set, walks through this directory and converts all
                           note.json to ipynb
     --out-path OUT_PATH   Output path
     --to-html             Converts to HTML
     --to-py               Converts to .py
