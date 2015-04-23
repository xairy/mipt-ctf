#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int not_called() {
    system("/bin/sh");

    return 0;
}

int vulnerable(char* str) {
  char buffer[128];

  strcpy(buffer, str);

  return 0;
}

int main(int argc, char** argv) {
  int x = 0;

  if (argc != 2) {
    printf("Usage: %s <payload>\n", argv[0]);
    return 0;
  }

  vulnerable(argv[1]);

  return 0;
}
