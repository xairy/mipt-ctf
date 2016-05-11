#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

const char* not_used = "/bin/sh";

int vulnerable() {
  char buffer[128];

  read(STDIN_FILENO, buffer, 256);

  return 0;
}

int main(int argc, char** argv) {
  vulnerable();

  return 0;
}
