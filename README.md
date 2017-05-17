# Code trimmer

Cut parts of code source according to comment annotations. Typically used
for generating a trimmed down version of a project that will be given
to students.

Example:

file: fact.c

    #include <stdio.h>

    void print_hello() {
      // TODO
      // START CUT
      printf("hello\n");
      // END CUT
    }

    int fact(int x) {
      // TODO
      // START CUT
      int res = 1;
      int i;
      for (i = 1; i <= x; i++) {
        res = res * i;
      }
      return res;
      // END CUT
      // UNCOMMENT    return 0; // CHANGE THIS
    }

    int main() {
      int x = 5;
      print_hello();
      printf("%d! = %d\n", x, fact(x));
      return 0;
    }

`./trimcode.py foobar.c -o dest` generates dest/fact.c:

    #include <stdio.h>

    void print_hello() {
      // TODO
    }

    int fact(int x) {
      // TODO
      return 0; // CHANGE THIS
    }

    int main() {
      int x = 5;
      print_hello();
      printf("%d! = %d\n", x, fact(x));
      return 0;
    }
