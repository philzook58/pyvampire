# Vampire

A simple repackaging of the [Vampire](https://vprover.github.io/) automated theorem prover for ease of installation and execution from python. All rights and licensing are up to the Vampire team.

Supplies an x86_64 binary built under Ubuntu 22.04. If you are not running something similar, this is unlikely to work.

## Installation

```bash
python3 -m pip install -e .
```

```python
import vampire
vampire.binpath()
vampire.run(["/tmp/test.p"]) # same arguments as subprocess.run
```
