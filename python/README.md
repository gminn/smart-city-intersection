# Python Guide

If you want to copy and paste some code snippets, please refer to [devtips.md](./devtips.md).

## Requirements

- Python 3.6
- SENSR

## Installation

```bash
pip3 install -r requirements.txt
./gen_proto.sh
```

## Execution

- Dump the output messages received from SENSR
  ```bash
  python3 message_receiver.py
  # Run SENSR in another terminal
  ```
- Parse binary output frames
  ```bash
  python3 parse.py ../binary_files/sample_output
  ```
