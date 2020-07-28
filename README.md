# File-Logger
This project is to be used for logging to the local file system during the execution of a python application.    

> #### Table of Contents  
> [1. Installation](#installation)  
> [2. Initialization](#initialization)  
> [3. Logging A Message](#logging-a-message)  

## Installation
Installation instructions here

## Initialization
To initialize the logger create a new instance of the logger.

```python
self._logger = Logger(application_name, logging.DEBUG, file_name)
```

## Logging A Message
To log a message provide the logging level and the message you want to log

```python
self._logger.log("debug", log_message)
```

> ##### Supported Logging Levels
> 1. "debug"
> 2. "info"
> 3. "warning"
> 4. "error"
> 5. "critical"