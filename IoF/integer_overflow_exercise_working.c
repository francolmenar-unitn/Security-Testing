#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("Hello, which product do you want to buy?\n");
    printf("1) IPhone 12\n");
    printf("2) IPhone 12 Pro\n");
    printf("3) IPhone 12 Pro Max Max\n");

    // Get item
    int item_choice;
    scanf("%d", &item_choice);

    printf("Great device, how many?\n");
    int item_quantity;
    scanf("%d", &item_quantity);

    printf("Quantity: %d\n", item_quantity);

    // 2^32 = 4294967296 Makes the quantity zero

    int insurance = 1200;

    // int price = item_quantity + insurance;
    // 2^32 - 1200 = 4294966096 Makes the price without multiplication zero

    // int price = item_quantity * 2;
    // 2^31 = 2147483648

    int price = item_quantity * 10 + 1200;
    // (2^32 - 1200) / 2 = 2147483048

    // int price = item_quantity * 1500 + insurance;
    printf("Price: %d\n", price);

    if (item_quantity <= 0) {
        printf("You should buy at least one Iphone!\n");
        return -1;
    }

    if (item_choice == 3) {
        int price = 1500 * item_quantity + insurance;
        printf("Price 222222: %d\n", price);

        if (price == 0) {
            printf("You solved the problem\n");
            printf("The Iphone Max Max is yours\n");
            return 1;
        }
        printf("You have to pay €%d\n", price);
    } else {
        if (item_quantity > 3) {
            printf("You can buy maximum 3\n");
            return -1;
        }
        int price = 1000 * item_quantity;
        printf("You have to pay €%d\n", price);
    }
    return 0;
}
