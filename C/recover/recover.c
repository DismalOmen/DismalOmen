#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <cs50.h>

int main(int argc, char *argv[])
{
// larger than 2 and it will not execute
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

 // open file, then read it
 FILE *file = fopen(argv[1], "r");
 if (file == NULL)
 {
    printf("could not open image\n");
    return 1;
 }
 // define new type for buffer
 typedef uint8_t BYTE;

 BYTE buffer[512];

 //assign required space to filename
 char *filename = malloc(8);

 //create an empty file
 FILE *file0 = NULL;

 int counter = 0;

 while (fread(buffer, 1, 512, file) == 512)
 {
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        if (counter == 0)
        {
         sprintf(filename, "%03i.jpg", counter);
         file0 = fopen(filename, "w");
         fwrite(buffer, 1, 512, file0);
         counter++;
        }
        else
        {
         fclose(file0);
         sprintf(filename, "%03i.jpg", counter);
         file0 = fopen(filename, "w");
         fwrite(buffer, 1, 512, file0);
         counter++;
        }
    }
    else
    {
      if (counter > 0)
      {
       fwrite(buffer, 1, 512, file0);
      }
    }
 }
 fclose(file0);
 fclose(file);
 free(filename);
}


