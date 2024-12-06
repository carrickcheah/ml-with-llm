# Session 3

Today tasks:  

- dockerize candles

## dockerize candles

copy the trades dockerfile since it is same. and update Makefile  


## Feature engineering - add technical-indicators

- bash$   uv init --no-workspace technical-indicators
        uv add quixstreams loguru pydantic-settings

- Install ta-lib  
        Linux  
        Download ta-lib-0.4.0-src.tar.gz and:  

        $ tar -xzf ta-lib-0.4.0-src.tar.gz  
        $ cd ta-lib/  
        $ ./configure --prefix=/usr  
        $ make  
        $ sudo make install  


- Just use quixstream connect input n output first.












