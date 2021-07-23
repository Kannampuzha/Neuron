#include <stdio.h>
#include <stdlib.h>

int time=1;

void fire_signal()
{
    puts("Fire !");

}
void action(int intensity) {

    int y = time - (11 - intensity);
    printf("Time %i" ,time);
    if (y > 2)
    {

        fire_signal();
        time = 1;
    }
    else
    {
        time++;
    }

}


int main() {

    int Intensity;
    do
    {


        FILE *fp = fopen("D:\\Neuron\\input.io", "r");
        char intensity[3];
        fgets(intensity, 3, fp);
        fclose(fp);

        Intensity = atoi(&intensity);
        if (Intensity != 0 && Intensity <11)
        {
            action(Intensity);
        }

    }
    while (1);


}

