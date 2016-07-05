AUTHOR = "Norton Pengra"
VERSION = 0.1
DATE_CREATED = "July 5th, 2016"

import time
import io
import bottle
import _thread

class cpu_monitor(object):

	def __init__(self, proc_file="/proc/stat", interval=1, times=100):
		self.cpu_proc = proc_file
		self.interval = interval
		self.times = times
		self.svg = ""
		self.last = []
		self.total_usage = 0
		self.history = [] # convert these numbers to percentages.

	def read_proc(self):
		with io.open(self.cpu_proc) as f:
			stats = f.readlines()
		self.record_proc(stats)

	def run(self):
		for t in range(self.times):
			self.read_proc()
			time.sleep(self.interval)
			print(self.history[-1:])

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
			try:
				this_cycle_cpu_usage = ((json[0] - self.last[0]) + (json[1] - self.last[1])) / ((json[0] - self.last[0]) + (json[1] - self.last[1]) + (json[2] - self.last[2]))
			except ZeroDivisionError:
				this_cycle_cpu_usage = 0
			self.history.append(this_cycle_cpu_usage * 100)
			self.total_usage += this_cycle_cpu_usage
		self.last = json


def lazy_int(value):
	try:
		return int(value)
	except ValueError:
		return value

if __name__ == "__main__":

	C = cpu_monitor(times=1000000000)


	def launch_cpu_monitor():
		C.run()


	@bottle.route('/')
	def hello():
		try:
			return str(C.history[-1])
		except KeyError:
			return '0'


	_thread.start_new_thread(launch_cpu_monitor, ())
	bottle.run(host='0.0.0.0', port=8080, debug=True)
