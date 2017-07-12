import logging
import subprocess
import threading
import time
from kalliope.core.NeuronModule import NeuronModule



logging.basicConfig()
logger = logging.getLogger("kalliope")




class Delay(NeuronModule):
    def __init__(self, **kwargs):
        super(Delay, self).__init__(**kwargs)
        # the args from the neuron configuration
        self.seconds = kwargs.get('seconds', None)
        self.synapse = kwargs.get('synapse', None)
        self.time = time
        
       # check if parameters have been provided
        if self._is_parameters_ok():
            if self.seconds is not None and self.synapse is None:
                self.time.sleep(self.seconds)        
            if self.seconds is not None and self.synapse is not None:           
                delay_synapse = DelaySynapse(seconds=self.seconds, synapse=self.synapse)
                delay_synapse.start()        

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise

        .. raises:: MissingParameterException
        """
        if self.seconds and None:       
            raise MissingParameterException("You must set seconds of delay") 
        return True
        
class DelaySynapse(threading.Thread):
    """
    Class used to run an asynchrone Shell command

    .. notes:: Impossible to get the success code of the command
    """
    def __init__(self, seconds, synapse):
        self.stdout = None
        self.stderr = None
        
        threading.Thread.__init__(self)
        self.time = time
        self.seconds = seconds
        self.synapse = synapse

         
    def run(self):
        self.time.sleep(self.seconds)
        p = subprocess.Popen(("kalliope start --run-synapse") + (" ") + self.synapse,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)

        self.stdout, self.stderr = p.communicate()
    
