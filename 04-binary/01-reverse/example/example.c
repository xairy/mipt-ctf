#include <stdio.h>

void if_demo() {
  int x = 1337;

  if (x == 42) {
    printf("x == 42\n");
  } else {
    printf("x == %d\n", 1337);
  }
}

int for_demo() {
  int i;
  int x = 0;

  for (i = 0; i < 10; i++) {
    x += i;
  }

  return x;
}

int switch_demo() {
  int x = 42;

  switch (x) {
    case 0:
      puts("Zero!\n");
      break;
    case 1:
      puts("One!\n");
      break;
    case 2:
      puts("Two!\n");
      break;
    case 3:
      puts("Three!\n");
      break;
    case 4:
      puts("Four!\n");
      break;
    case 5:
      puts("Five!\n");
      break;
    case 6:
      puts("Six!\n");
      break;
    case 7:
      puts("Seven!\n");
      break;
  }
}

int main() {
  if_demo();
  for_demo();
  switch_demo();
  return 0;
}
