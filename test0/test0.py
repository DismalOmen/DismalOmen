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
 //create byte type, store byte data, create a counter, an array to store the image bites and declare the new file empty
 typedef uint8_t BYTE;
 BYTE BLOCK_SIZE = 512;
 BYTE buffer[512];
 int count = 0;
 char *filename = malloc(8);
 //loop through the image data
 while (fread(buffer, 1, BLOCK_SIZE, file) == 512 || 0)
 {
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff)
    {
         int len =  fread(buffer, 1,512,file);
         fwrite(buff,1,len,j);
    }

 }
    free(filename);
    fclose(file0);
}