import subprocess
import os
import signal
import subprocess

class clone:
    isRunning = False
    proc = None

    def stop(self):
        self.isRunning = False
        os.killpg(os.getpgid(self.proc.pid), signal.SIGTERM)
        
    def clone(self, screen):
        self.isRunning = True
        n = screen.prevSlider
        self.proc = self.update(n)
        while self.isRunning:
            if n != screen.prevSlider:
                self.proc.kill()
                n = screen.prevSlider
                self.proc = self.update(n)

    def update(self, n):
        value = int(n) * 100
        command = 'play -q -V0 "|rec -q -V0 -n -d -R riaa bend pitch {}"'.format(value)
        print("Voice Deformation Value: " + str(value))
        print("Voice Deformation Command: " + str(command))
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        return proc
    


            
       

 

