# MousePathGAN - DataCollection

Hello! This section of the repository contains the files necessary for collecting and recording real mouse movement data.
Essentially, running **CollectMouseData .py** will open a GUI with buttons that appear on screen in random locations. Click on one, it disappears, another appears, so on and so forth.
While you're demolishing red buttons, mouse position is being tracked over time, along with each button's position and dimensions.
The GUI runs in a loop--each iteration is made of **50 button generations.** When the last button is clicked, mouse data collection is paused until you resume by clicking the blue button to start the process again.

## Requirements
* **Python 3** (developed and tested on **3.7.4**)
* **TkInter** - Python GUI library (should be included in base Python installation)


## In Action!
I made a video detailing the process: https://www.youtube.com/watch?v=n0RM0ou-V4o
