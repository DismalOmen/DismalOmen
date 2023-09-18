#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    //first we loop through the height and width of the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //now we can say that if the pixels of the image are black (0x00) set them to another color 
            if ((image[i][j].rgbtRed == 0x00 && image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtBlue == 0x00))
            {
                image[i][j].rgbtBlue = 0xff;
            }
        }
    }
}
