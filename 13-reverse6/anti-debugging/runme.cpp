#include <sys/ptrace.h>
#include <unistd.h>
#include <stdio.h>
 
void check(void) __attribute__((constructor));
 
void check(void) {
  if (ptrace(PTRACE_TRACEME, 0, 0, 0) == -1) {
    printf("No debuggers allowed!\n");
    _exit(-1);
  }
}

int main() {
  printf("No debugger found, you can proceed.\n");
  return 0;
}
