# Testing your Python projects

## Using `pytest`

```bash
pip install pytest
```

```python
# function to test
def get_answer():
    return 42


# actual test
def test_answer_to_file_is_42():
    assert get_answer() == 42

```

```
py.test
```

```
==================== test session starts ===========================
platform darwin -- Python 3.5.1, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: stuff/hitchhikers-guide/tech-tutorials/testtesttest, inifile:
collected 1 items

test_life.py .

==================== 1 passed in 0.01 seconds =======================
```

## Where to store your tests

```
.
├── docs
│   └── documentation_here.txt
├── etl
│   └── code_to_load_to_db.txt
├── evaluation
│   └── code_to_evaluate_models_here.txt
├── exploration
│   └── jupyter_notebooks_with_cool_plots_here.txt
├── features
│   └── code_to_generate_features_here.txt
├── lib
│   ├── lib
│   │   ├── __init__.py
│   │   ├── db
│   │   │   ├── __init__.py
│   │   │   ├── load.py
│   │   │   └── process.py
│   │   └── util.py
│   └── tests
│       ├── test_db.py
│       └── test_util.py
└── model
    └── code_to_train_models_here.txt
```

## Tools

*   unittest (part of the Python standard library)

*   [py.test](http://pytest.org/latest/) (if you don't know which to use, use this)

*   [nose](https://github.com/nose-devs/nose)
