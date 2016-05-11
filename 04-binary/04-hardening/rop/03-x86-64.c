#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int not_called() {
  system("/bin/sh");

  return 0;
}

int vulnerable() {
  char buffer[128];

  read(STDIN_FILENO, buffer, 256);

  return 0;
}

int main() {
  vulnerable();

  return 0;
}
