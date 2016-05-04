How to control gdb evironment
=============================

```
g++ -m32 stack.cpp -o stack
```

```
env - gdb -q /usr/bin/printenv -ex "set confirm off" -ex "unset env" -ex "r" -ex "q"
```

```
env - gdb -q $(pwd)/stack -ex "set confirm off" -ex "unset env" -ex "r" -ex "q"
```

```
env - PWD=$(pwd) $(pwd)/stack
```
