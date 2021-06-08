Student's Name   I.D.Number  Department
Beylem Yavuz     260206002   ECE
Hatice Obuz      270206039   ECE
Serdar Sertgöz   260201030   CENG
Ertuğrul Demir   260201059   CENG


python version = Python 3.7.4
pygame version = pygame 1.9.6
dataclass = after python 3.7

C version to simulate program:
TDM-GCC 4.9.2 64-bit Release
-std=c99
-static-libgcc

You can simulate the values by using two_body_simulation.py or two_body_simulation.c file.
these programs yield different txt files named as locationVectorC.txt and locationVectorPY.txt 
due to understand the difference between C and python file. To use these locationVector file in the 
two_body_animation.py program, you need to be sure that you are reading right file. To change the 
file which you read, you need to change the name of the file in the App class -> readFile method.

Then you can run the two_body_animation.py file. you can see the animation according to your inputs. 
Press "Space" to stop/play animation, press "R" key to reload the animation and press "Q" key to exit
from animation.
And also if you want to see the orbit, you can make comment the line which fill black the screen.

In C program:

To obtain the coordinates of two body in c program run two_body_simulation.c and enter required inputs 
then text file will be recorded in the file where c program is.
The compiler options must be:

TDM-GCC 4.9.2 64-bit Release

Add the following commands when calling the compiler:
-std=c99
Add the following commands when calling the linker:
-static-libgcc


you can interpreted text files as body1_X_cordinates,body1_Y_cordinates,body2_X_cordinates,body2_Y_cordinates 
which has values what give the euler and runge-kutta functions. we will locate the bodies on the screen
by using this values 


