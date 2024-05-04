import json
import get_data

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    a=get_data.get_data(file_path)
    b=(list(a.values()))
    s=list(a.keys())
    d=b.index(max(b))
    return s[d]
    pass

# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)