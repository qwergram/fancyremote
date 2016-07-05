AUTHOR = "Norton Pengra"
VERSION = 0.0
DATE_CREATED = "July 5th, 2016"

import time
import io

class cpu_monitor(object):

	def __init__(self, proc_file="/proc/stat", interval=1):
		self.cpu_proc = proc_file
		self.interval = interval
		self.svg = ""
		self.history = []

	def read_proc(self):
		with io.open(self.cpu_proc) as f:
			stats = f.readlines()
		self.history.append(proc_parser(stats))

	def main(self):
		while True:
			self.read_proc()
			time.sleep(self.interval)


def lazy_int(value):
	try:
		return int(value)
	except ValueError:
		return value



def proc_parser(contents):
	json = {'intr': {}}
	for line in contents:
		line = line.strip()
		if line.startswith('cpu '): # Since there's only one core, we only need to check the average
			cpu, user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice = [lazy_int(string) for string in line.split()]
			json['cpu'] = {'user': user, 'nice': nice, 'system': system, 'idle': idle, 'iowait': iowait, 'irq': irq, 'softirq': softirq, 'steal': steal, 'guest': guest, 'guest_nice': guest_nice}
		if line.startswith('intr'):
			for i, interrupt in enumerate(line.split()[1:]):
				if interrupt != '0':
					json['intr'][i] = int(interrupt)

	return json


if __name__ == "__main__":
	C = cpu_monitor()
	C.read_proc()
	print(C.history[0])
