// Tank Thunderbird 100-days-ML Day 002
// Looking at Matrix transformations, I decided to modify this code by David Eisenberg found here:
// https://processing.org/tutorials/transform2d/
// I didn't have time to make it more like the ones in the videos I am watching,
// in which the grid will shear and the points of the transformed grid will 
// match those of the original grid
// Made with processing 3.3.6 (Java)
////////////////////////////////////////////////////////////////////

void drawGrid( )
{

  drawGrid(true);
  
}

void gridColor(int greyTone, int movement)
{
  fill(greyTone);
  stroke(greyTone);
  translate(movement, movement);
  drawGrid( );
  noStroke();
  fill(0);
}

void drawGrid(boolean showZero)
{
  final int STEP = 40;
  final int MAX = 200;
  String numStr;

  textFont(font);
  if (showZero)
  {
    text("0", -textWidth("0"), -textDescent());
  }
  for (int x = 0; x < MAX + STEP; x += STEP)
  {
    if (showZero || x != 0 && (!showZero && x != MAX))
    {
      numStr = Integer.toString(x/40);
      text(numStr, x - textWidth(numStr) / 2, -textDescent());
    }
    line(x, 0, x, MAX);
  }
  for (int y = 0; y < MAX + STEP; y += STEP)
  {
    if (y != 0 )
    {
      numStr = Integer.toString(y/40);
      text(numStr, -textWidth(numStr)-2, y + textAscent() / 2 );
    }
    line(0, y, MAX, y);
  }
}