// Tank Thunderbird 100-days-ML Day 002
// Looking at Matrix transformations, I decided to modify this code by David Eisenberg found here:
// https://processing.org/tutorials/transform2d/
// I didn't have time to make it more like the ones in the videos I am watching,
// in which the grid will shear and the points of the transformed grid will 
// match those of the original grid
// Made with processing 3.3.6 (Java)
////////////////////////////////////////////////////////////////////

PFont font; 
int startTone = 180;
int edgeOffset = 30;
int movement = 20;

void setup()
{
  size(400, 400);
  background(255);
  fill(0);
  font = loadFont("LiberationSans-9.vlw"); 
  
  pushMatrix();
  
  step2();
  
  popMatrix( );
}

void step1()
{

  gridColor(startTone, edgeOffset);
  drawGrid();
  stroke(255, 0, 0);
  line(0, 0, 80, 80);

}

void step2()
{
  step1();
  pushMatrix();
  translate(80, 80);
  rotate(radians(-25));
  gridColor(0, 0);
  drawGrid();
  popMatrix();
}