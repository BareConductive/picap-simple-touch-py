################################################################################
#
# Bare Conductive Pi Cap
# ----------------------
#
# simple-touch.py - simple MPR121 touch detection demo with stdout output
#
# Written for Raspberry Pi.
#
# Bare Conductive code written by Szymon Kaliski and Tom Hartley.
#
# This work is licensed under a MIT license https://opensource.org/licenses/MIT
#
# Copyright (c) 2016, Bare Conductive
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#################################################################################

from time import sleep
import MPR121

try:
  sensor = MPR121.begin()
except Exception as e:
  print (e)
  sys.exit(1)

# this is the touch threshold - setting it low makes it more like a proximity trigger default value is 40 for touch
touch_threshold = 40

# this is the release threshold - must ALWAYS be smaller than the touch threshold default value is 20 for touch
release_threshold = 20

# set the thresholds
sensor.set_touch_threshold(touch_threshold)
sensor.set_release_threshold(release_threshold)


running = True
while running:
  try:
    if sensor.touch_status_changed():
      sensor.update_touch_data()
      for i in range(12):
        if sensor.is_new_touch(i):
          print ("electrode {0} was just touched".format(i))
        elif sensor.is_new_release(i):
          print ("electrode {0} was just released".format(i))
    sleep(0.01)
  except KeyboardInterrupt:
    running = False
  
