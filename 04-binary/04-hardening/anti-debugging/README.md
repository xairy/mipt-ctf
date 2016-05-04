Anti-debugging
==============

```
g++ runme.cpp -o runme
```

```
$ strace ./runme
execve("./runme", ["./runme"], [/* 55 vars */]) = 0
...
write(1, "No debuggers allowed!\n", 22No debuggers allowed!
) = 22
...
```

```
gcc -shared -fPIC -o fake.so fake.c
```

```
$ strace -E LD_PRELOAD=./fake.so ./runme
execve("./runme", ["./runme"], [/* 56 vars */]) = 0
...
open("./fake.so", O_RDONLY|O_CLOEXEC)   = 3
...
write(1, "No debugger found, you can proce"..., 36No debugger found, you can proceed.
    ) = 36
...
```

```
$ gdb -q ./runme -ex "set env LD_PRELOAD = ./fake.so" -ex "r"
Reading symbols from ./runme...(no debugging symbols found)...done.
Starting program: .../runme 
No debugger found, you can proceed.
[Inferior 1 (process 10848) exited normally]
```
