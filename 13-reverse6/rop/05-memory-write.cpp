#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int x = 0;

int vulnerable() {
  char buffer[128];

  read(STDIN_FILENO, buffer, 256);

  return 0;
}

int main() {
  vulnerable();

  printf("x = %x\n", x);

  if (x == 0xdeadbeef) {
    system("/bin/sh");
  }

  return 0;
}
