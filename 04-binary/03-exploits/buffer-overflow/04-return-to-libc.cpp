#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int vulnerable(char* str) {
  char buffer[128];

  strcpy(buffer, str);

  return 0;
}

int main(int argc, char** argv) {
  if (argc != 2) {
    printf("Usage: %s <payload>\n", argv[0]);
    return 0;
  }

  vulnerable(argv[1]);

  return 0;
}
