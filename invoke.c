#include <stdio.h>

int main(int argc, char* argv[]) {
    if (argc == 2) {
        FILE* file = fopen(argv[1], "w");
        if (file == NULL) return 1;
        else {
            fclose(file);
            return 0;
        }
    } else {
        return 1;
    }
}
