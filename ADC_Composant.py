import smbus

class ADC_Composant(object):
    def __init__(self):
        self.cmd = 0
        self.address = 0
        self.bus=smbus.SMBus(1)
        
    def detecteI2C(self,addr):
        try:
            self.bus.write_byte(addr,0)
            print("Composante trouvée à l'adresse 0x%x"%(addr))
            return True
        except:
            print("Composante non trouvée à l'adresse 0x%x"%(addr))
            return False
            
    def close(self):
        self.bus.close()

class ADS7830(ADC_Composant):
    def __init__(self):
        super(ADS7830, self).__init__()
        self.cmd = 0x84
        self.address = 0x4b # 0x4b est l'adresse i2c par défaut pour la composante ADS7830.   
        
    def lectureAnalogique(self, chn): # ADS7830 broches d'entrée: 0,1,2,3,4,5,6,7
        value = self.bus.read_byte_data(self.address, self.cmd|(((chn<<2 | chn>>1)&0x07)<<4))
        return value
