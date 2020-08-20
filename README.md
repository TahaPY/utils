# utils-tahapy
My common utility functions

## Persian
- convert_digits: convert english digits to persian digits
```python
from utils.persian import convert_digits
convert_digits("0987654321")    # => ۰۹۸۷۶۵۴۳۲۱
```    
## Strings
- is_null_or_empty: check string is empty or None
```python
from utils.strings import is_null_or_empty
is_null_or_empty(None)  # => True
is_null_or_empty("")    # => True
is_null_or_empty("Hi")  # => False
```
