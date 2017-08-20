from ctypes import *
i = c_int(25)

print i

print i.value

i.value = 123

print i.value



p = create_string_buffer(10)
p.raw
print p.raw

p.value = 'Student'

print p.raw


dll = cdll.LoadLibrary(r'C:\Users\SUNRISE\Documents\Visual Studio 2013\Projects\dead_loop\x64\Debug\dead_loop.dll')

ret = dll.DeadLoop(1000)


print ret




