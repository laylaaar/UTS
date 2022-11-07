class clock :
    def __init__ (self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec
        
waktu  = clock(24, 60, 60)

print("Jam : {}".format(waktu.hour))
print("Menit : {}".format(waktu.min))
print("Detik : {}".format(waktu.sec))