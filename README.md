# Khan
* Distributed AI for IOT applications
* Your finetunned data plataform for ondevice AI models. 

## Caracteristics
* Each IOT node has its own specific NN, with minimal computation (on device NN).
* Each IOT node has its own sensors and actuators.
* Each node has communication to any other node on the IOT network, sends sensors data and the posible "action" data to actuators
* The data sent to each other node finetune the NNs inside each IOT node and then replies if there is consensus (consensus, distributed algorithm) then the X,Y,Z actuator can perform.
* COnsensus should be done based on data quality and desition making based on human input (RLHF: prompting, etc) 



