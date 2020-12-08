#include <stdio.h>
#include <stdlib.h>
#include<stdbool.h>

int makeTainted(char * tainted_var) {

}

int makeCondTainted(char * tainted_var, char * taint_cond) {

}

char * array(char * taintCond) {

}

bool isTainted(char * tainted_var) {

}

bool isIoF(char * tainted_var) {

}

int main() {
    printf("Hello, which product do you want to buy?\n");
    printf("1) IPhone 12\n");
    printf("2) IPhone 12 Pro\n");
    printf("3) IPhone 12 Pro Max Max\n");

    // Get item
    int item_choice;
    scanf("%d", &item_choice);
    makeTainted("item_choice");

    printf("Great device, how many?\n");
    int item_quantity;
    scanf("%d", &item_quantity);
    makeTainted("item_quantity");

    if (item_quantity <= 0) {
        printf("You should buy at least one Iphone!\n");
        return -1;
    }

    int price = 1000 * item_quantity;
    makeCondTainted("item_quantity", array("item_quantity"));

    int insurance = 1200;
    if (item_choice == 3) {
        int price = 1500 * item_quantity + insurance;
        makeCondTainted("price", array("item_quantity"));

        if(isTainted("price") && isIoF("price")){
            printf("IoF violation\n");
            exit(-1);
        }
        if (price == 0) {
            printf("You solved the problem\n");
            printf("The Iphone Max Max is yours\n");
            return 1;
        }

        if(isTainted("price")){
            printf("Printing tainted variable\n");
            exit(-1);
        }
        printf("You have to pay €%d\n", price);
    } else {
        if (item_quantity > 3) {
            printf("You can buy maximum 3\n");
            return -1;
        }

        if(isTainted("price")){
            printf("Printing tainted variable\n");
            exit(-1);
        }
        printf("You have to pay €%d\n", price);
    }
    return 0;
}
