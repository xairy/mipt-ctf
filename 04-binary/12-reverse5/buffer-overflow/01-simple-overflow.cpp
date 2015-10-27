#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {
  char buffer[128];
  int x = 0;

  if (argc != 2) {
    printf("Usage: %s <payload>\n", argv[0]);
    return 0;
  }

  strcpy(buffer, argv[1]);
   
  if (x == 0xdeadbeef) {
    system("/bin/sh");
  }

  return 0;
}
