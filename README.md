
# Local Module

Making life easier since 2023!
This module will aid in properly executing shell commands. 


## Usage/Examples

### Simple
```python
from Local.shell import cmd
with cmd('ls') as cmd:
    print(cmd)
```
### Iteration
```python
with cmd('ls',listen=True) as cmd:
    for result in cmd:
        print(result)
```