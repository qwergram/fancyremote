AUTHOR = "Norton Pengra"
VERSION = 0.0
DATE_CREATED = "July 5th, 2016"

import time
import io

class cpu_monitor(object):

	def __init__(self, proc_file="/proc/stat", interval=1, times=100):
		self.cpu_proc = proc_file
		self.interval = interval
		self.times = times
		self.svg = ""
		self.last = []
		self.history = [] # convert these numbers to percentages.

	def read_proc(self):
		with io.open(self.cpu_proc) as f:
			stats = f.readlines()
		self.record_proc(stats)

	def main(self):
		for time in range(times):
			self.read_proc()
			time.sleep(self.interval)

	def record_proc(self, contents):
		json = []
		for line in contents:
			line = line.strip()
			if line.startswith('cpu '): # Since there's only one core, we only need to check the average
				cpu, user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice = [lazy_int(string) for string in line.split()]
				json = [user, system, idle]
				break
		else:
			raise IOError("Invalid Procfile")
		if self.last:
			this_cycle_cpu_usage = ((json[0] - self.last[0]) + (json[1] - self.last[1])) / ((json[0] - self.last[0]) + (json[1] - self.last[1]) + (json[2] - self.last[2]))
			self.history.append(this_cycle_cpu_usage)
		self.last = json

def lazy_int(value):
	try:
		return int(value)
	except ValueError:
		return value




if __name__ == "__main__":
	C = cpu_monitor()
	C.read_proc()
	C.read_proc()
	C.read_proc()
	print(C.history)
