# Khan
* Distributed AI for IOT applications, unifies distributed and AI paradigms. 
* Your finetunned data plataform for ondevice AI models. 

## Caracteristics
* Each IOT node has its own specific NN (or SML), with minimal computation (on device NN).
* Each IOT node has its own sensors and actuators.
* Each node has communication to any other node on the IOT network, sends sensors data and the posible "action" data to actuators
* The data sent to each other node finetune the NNs inside each IOT node and then replies if there is consensus (consensus, distributed algorithm) then the X,Y,Z actuator can perform.
* Consensus should be done based on data quality and decision making based on human input (RLHF: prompting, etc), and also via consensus algoritms like pbft.  



