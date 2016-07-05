AUTHOR = "Norton Pengra"
VERSION = 0.0
DATE_CREATED = "July 5th, 2016"

import sleep

class cpu_monitor(object):

	def __init__(self, proc_file="/proc/stat", interval=1):
		self.cpu_proc = proc_file
		self.interval = interval
		self.svg = ""

	def read_proc(self):
		pass

	def main(self):
		while True:
			self.read_proc()
			time.sleep(self.interval)
