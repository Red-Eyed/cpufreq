import cpufreq
import time

cpu = cpufreq.CPUFreq()
cpu.list_current_governos()
cpu.list_current_frequencies()

cpu.change_governo("userspace")
cpu.get_frequencies()  # list of possible frequencies for all cpus
freq = cpu.get_frequencies()[0]['data']  # cpu frequencies
for f in freq:
    print("Frequency %s" % f)
    cpu.change_frequency(f)  # change frequency all cpus
    cpu.list_current_frequencies()
    time.sleep(1)

cpu.change_governo("ondemand")
cpu.list_current_governos()
cpu.list_current_frequencies()

c = 3
print("Disabling the core %d" % c)
cpu.disable_cpu(c)
time.sleep(5)
print("Enabling the core %d" % c)
cpu.enable_cpu(c)
time.sleep(5)
