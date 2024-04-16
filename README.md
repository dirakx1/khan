# Khan
Distributed AI for IOT implementations

## Caracteristics
* Each IOT node has its own LLM, with minimal computation.
* Each IOT node has sensors and actuators
* Each node has communication to any other node on the IOT network, sends sensors data and the posible actuation data to actuators
* The data sent to each other node finetune the LLMs inside each IOT node and then replies if there is consensus (consensus algorithm) then the X,Y,Z actuator can perform.



