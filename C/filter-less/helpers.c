#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // first we loop through the image with a for loop, will be doing that a lot.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //set values of colors of the image to a variable so its easier to manipulate
            int blue = image[i][j].rgbtBlue;
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;

            //calculate averege (grey in hex it's the amount of RGB)
            int averege = round((blue + red + green) / 3.0);

            //pass that value to orginal colors
            image[i][j].rgbtBlue = averege;
            image[i][j].rgbtRed = averege;
            image[i][j].rgbtGreen = averege;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue = image[i][j].rgbtBlue;
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;

            //exactly the same but with another formula, and here we need to cap the values on 255 wich is the maximun number for the color
            int sepiaRed = round(.393 * red + .769 * green + .189 * blue);
            int sepiaGreen = round(.349 * red + .686 * green + .168 * blue);
            int sepiaBlue = round(.272 * red + .534 * green + .131 * blue);
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            //so by taking one we put that specific pixel in the opposite side, but for doing it we need to create an "empty glass" like in class so we temp store it
            RGBTRIPLE empty_glass = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = empty_glass;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
