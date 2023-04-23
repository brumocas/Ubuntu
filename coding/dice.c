#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>


int main(){

    time_t t;
    /*Set seed*/
    srand((unsigned) time(&t));

    int times_roled = 0;
    int times_face_6[] = {0,0,0,0,0};
    printf("How many times to role the dice?\n");
    scanf("%d",&times_roled);

    for (int k = 0; k < 5; k++){
        
        for(int i = 0; i < times_roled; i++){
        int face = rand()%7;
        printf("Face = %d\n",face);

        if(face == 0){
            i--;
            continue;
        }


        if (face == 6)
        times_face_6[k]++;
        }
    }

    int expected = times_roled/6;

    for(int i = 0; i < 5; i++){
        
        printf("Times rooled the face 6 in the set %i = %i\n",i + 1,times_face_6[i] - expected);
    }

    printf("Expected result %i\n",expected);
}