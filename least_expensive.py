import json
import get_data

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    a=get_data.get_data(file_path)
    b=(list(a.values()))
    s=list(a.keys())
    d=b.index(min(b))
    return s[d]

    
    pass

# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
