Python collection queries - pycq
================================

[![Build Status](https://travis-ci.org/janusko/pycq.svg?branch=master)](https://travis-ci.org/janusko/pycq)

pycq is simple software library helping with processing collections
in Python 3. You can search, transform and process any iterator in Python.
You can think of it as the LINQ for Python.

Comparision with other libraries
--------------------------------

### List comprehensions

Why should you use this instead of standard list comprehensions? Okay,
it is quite a good question. List comprehensions/generators are powerful
syntactic sugar in Python 2/3, that allows you to process any iterable
in nice filter-map manner. You can do almost anything using it.

But there is one big "but". Readability. It is very hard to write complex
query by using list comprehensions and even harder to read it.

Take this example (converted from MSDN Linq example):

```python
import itertools

products = self.GetProducts()

group_key = lambda p: p.category
grouped_by_category = itertools.groupby(
    sorted(
        products,
        key=group_key
    ),
    key=group_key
)

max_price_for_category = ((k, g, max(p.unit_price for p in g)) for k, g in grouped_by_category)

categories = ((k, (p for p in g if p.unit_price == mp)) for k, g, mp in max_price_for_category)
```

Just compare it to original C# LINQ code:

```cs
List<Product> products = GetProductList(); 

var categories = 
    from p in products 
    group p by p.Category into g 
    let maxPrice = g.Max(p => p.UnitPrice) 
    select new { Category = g.Key, MostExpensiveProducts = g.Where(p => p.UnitPrice == maxPrice) }; 
```

In pycq, you can write the query in a similar manner:
```python
from q import Q, Expando
products = self.GetProducts()

categories = Q(products)\
    .group_by(lambda p: p.category)\
    .select(lambda g: Expando(
        category=g.key,
        most_expansive_products=g.items.having_max(lambda p: p.unit_price)
    ))
```

### py_linq

Yea, I know about [py_linq](https://github.com/viralogic/py-enumerable)
project. But it seems that this project has been stalled for a while. And its
implementation is not much optimized for speed. Collection queries are
used a much.
