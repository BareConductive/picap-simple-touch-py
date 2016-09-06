################################################################################
#
# Bare Conductive Pi Cap
# ----------------------
#
# simple-touch.py - simple MPR121 touch detection demo with stdout output
#
# Written for Raspberry Pi.
#
# Bare Conductive code written by Szymon Kaliski.
#
# This work is licensed under a Creative Commons Attribution-ShareAlike 3.0
# Unported License (CC BY-SA 3.0) http://creativecommons.org/licenses/by-sa/3.0/
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#################################################################################

from time import sleep
import signal, sys, MPR121

try:
  sensor = MPR121.begin()
except Exception as e:
  print e
  sys.exit(1)

# handle ctrl+c gracefully
def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
  if sensor.touch_status_changed():
    sensor.update_touch_data()
    for i in range(12):
      if sensor.is_new_touch(i):
        print "electrode {0} was just touched".format(i)
      elif sensor.is_new_release(i):
        print "electrode {0} was just released".format(i)

  sleep(0.01)
