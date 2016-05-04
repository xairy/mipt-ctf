#include <stdio.h>

int main() {
  // '%<N>$d' refers to the argument number N.
  printf("2nd argument: %2$d\n", 1, 2, 3);

  // '%n' stores the number of characters written so far into the integer
  // indicated by the int* pointer argument.
  int so_far;
  printf("Hello world!%n\n", &so_far);
  printf("characters so far: %d\n", so_far);

  return 0;
}
