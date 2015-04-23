#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv) {
    char buffer[128];

    // Suppose we did read(..., 256).
    read(STDIN_FILENO, buffer, 128);

    // And suppose we got our shell.
    system("/bin/sh");

    return 0;
}
