#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int x = 0;

int main(int argc, char** argv) {
  char buffer[128];

  strncpy(buffer, argv[1], 128);
  printf(buffer);

  printf("x = %d\n", x);

  if (x == 10) {
    printf("Nice!\n");
    system("/bin/sh");
    return 0;
  }

  return 0;
}
