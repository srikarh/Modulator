import subprocess
class clone:
    isRunning = False

    def stop(self):
        self.isRunning = False

    
    def clone(self, screen):
        self.isRunning = True
        n = screen.prevSlider
        proc = self.update(n)
        while self.isRunning:
            if n != screen.prevSlider:
                proc.kill()
                n = screen.prevSlider
                self.update(n)

    def update(self, n):
        
        value = int(n) * 100
        command = 'play -q -V0 "|rec -q -V0 -n -d -R riaa bend pitch {}"'.format(value)
        print("Voice Deformation Value: " + str(value))
        print("Voice Deformation Command: " + str(command))
        proc = subprocess.Popen(command)
        return proc

            
       

