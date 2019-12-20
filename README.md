# ITX-pandas
Igor ITX to pandas

This is a simple set of commands/boiler plates that I use for plotting data from transport measurement. 
- `helvetica.py` I use Helvetica instead of the Deju Vu Sans, Arial, etc whenever it is possible. Matplotlib has missing font info bug being there for a while. 
- `boilerplate.py`	boilerplate with some device info. 
- `boilerplate_matplotlib.py`	boilerplate for just plotting in matplotlib. 
- `itx_to_pandas_df.py` This is the file for the main functions. 

# itx_to_pandas_df.py 
- `itx_to_pandas` reads the itx file to pandas dataframe. 
- `all_its` reads all itx files inside of the specified directory to a dataframe. 
- `resample_itx` resample the dataframe df(current, voltage) with respect to a specified array of currents 

# example outputs 
![Alt text](result.png?raw=true "Title")
![Alt text](Plateau.png?raw=true "Title")
![Alt text](GIV.png?raw=true "Title")


# using transconductance.py
![Alt text](result2.png?raw=true "Title")

