# Movie-Recommender-System

## Author
### Danila Kuzmin, 
### Email: d.kuzmin@innopolis.university
### Group: AAI BS21

## How to use repository:
1. Clone repository \
``` git clone ```
2. Install requirements \
``` pip install -r requirements.txt ```
3. Unpack data you need from "data" directory. "encoded_data.zip" is the ready-to-use data.
4. Run notebooks from "notebooks" section one-by-one. Replace only paths from which data and model download by your own.
5. If you want to use only pretrained model - you can find it in "models" directory in two variations - .pkl and .json

## How to use benchmark

If you want to use benchmark function - you have to follow these rules:
1. Benchmark function works with dicts that are saved as .pkl files (Examples that are ready-to-use are in "benchmark" folder).
2. As input it takes two dicts - one with predicted values and the second with original values
3. You can run the function from the command line by writing \
```python3 benchmark_script.py dict1.pkl dict2.pkl```
