#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int x = 0;

int main(int argc, char** argv) {
  char buffer[128];

  strncpy(buffer, argv[1], 128);
  printf(buffer);

  printf("x = %x\n", x);

  if (x == 0xdeadbeef) {
    printf("Nice!\n");
    system("/bin/sh");
    return 0;
  }

  return 0;
}
