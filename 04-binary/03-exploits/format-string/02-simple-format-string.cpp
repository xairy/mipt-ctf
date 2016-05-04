#include <stdio.h>
#include <string.h>

int main(int argc, char** argv) {
    char buffer[128];
    strncpy(buffer, argv[1], 128);
    printf(buffer);
    return 0;
}
