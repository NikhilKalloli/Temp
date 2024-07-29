# Temp

``` git clone https://github.com/NikhilKalloli/Temp.git```

``` cd Temp```

``` pip install virtualenv ```

``` python -m venv venv ```

``` venv\Scripts\activate ```

``` pip install -r requirements.txt```

## To get response in UI:  
``` python main.py ```

``` http://localhost:8002/ ```

## To get response in json format:  
``` python main2.py  ```
Open Postman and send post request to below url with json data. (Key: "Keyword", Value: "Topic of the poem")  
``` http://localhost:8002/generate ```