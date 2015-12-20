Socrates - Socrata data manager
===============================

It's a data manager. The application will provide an interface for adding datasets through the Socrata APIs. Once a dataset is added, the applications will continuously check for updates to the dataset. When there is an update available, Socrates will automajically download the newest version.

* Add a dataset.
* Watch the dataset.
* Update the dataset.

```
    Data/
        911_response_fires/
            11_21_14/
                data.csv
            10_12_15/
                data.csv
        
        Bike_Sharing_data
            11_21_14/
                data.csv
            10_12_15/
                data.csv
```

















## Scratch

* autocorrellation
    - Building permits
    - Housing prices
* Crosscorrellation
    - Take two signals
    - Take signal A and select a linear subset starting at time t_i.
    - Take signal B and select a linear subset starting at time t_j
    - For each t_i, crossCorrellate(signal_A[t_i:t_i + 50], signal_B[t_j:t_j + 50])
* Range of data, plus another range in data(?)





