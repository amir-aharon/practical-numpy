# Challenge 2 — Indexing & Slicing

## 🎯 Overview

Arrays aren't useful until you can **select parts of them**. This challenge teaches you how to read and write specific elements, rows, columns, ranges, boolean masks, and fancy indexing — the essential skills you use every day in data science and scientific computing.

## 📚 Current Status

- ✅ **Section 1: Basic Indexing** - COMPLETED
- ✅ **Section 2: Advanced Slicing** - COMPLETED
- ✅ **Section 3: Boolean Masking** - COMPLETED
- 🚧 **Section 4: Fancy Indexing** - NOT IMPLEMENTED
- 🚧 **Section 5: Advanced Operations** - NOT IMPLEMENTED

---

## 🧩 Section 1: Basic Indexing ✅ COMPLETED

**What you learned:**

- Single element access with `[row, col]` indexing
- Extracting whole rows/columns with `:` slice notation
- In-place modifications using indexing
- Extracting structural elements (corners)

**What you learned in Section 2:**

- Step-based slicing with `::2` for every other row
- Negative step slicing `::-1` for reversing columns
- Center block extraction using calculated indices
- Multi-dimensional slicing for 3D arrays

**What you learned in Section 3:**

- Boolean masking to filter array elements conditionally
- Creating masks with comparison operators
- Combining boolean conditions with logical operations
- In-place modification using boolean indexing

**Functions completed:**

- `get_item_rc()` - Get single element by row/column
- `get_first_row_last_col()` - Extract first row and last column
- `set_border_zeros()` - Set border elements to zero in-place
- `corners()` - Extract the four corner elements

**Functions completed in Section 2:**

- `get_every_other_row()` - Extract every other row using step slicing
- `reverse_columns()` - Reverse column order using negative step
- `extract_center_block()` - Extract center square block
- `get_3d_slice()` - Extract 2D slices from 3D arrays

**Functions completed in Section 3:**

- `select_positive_elements()` - Filter array to keep only positive values
- `mask_above_threshold()` - Create boolean mask for elements above threshold
- `select_even_rows_odd_cols()` - Select elements with specific row/column conditions
- `replace_negative_with_zero()` - Replace negative values with zero in-place

---

## ✅ Section 2: Advanced Slicing (COMPLETED)

**Goal:** Master step-based slicing, negative indices, and multi-dimensional slicing.

### Proposed Exercises:

#### 2.1 Step-based Slicing

```python
def get_every_other_row(a: np.ndarray):
    """
    Return every other row of the array (rows 0, 2, 4, ...).
    - Input: 2D array 'a'
    - Return: 2D array with every other row
    """
    raise NotImplementedError

def reverse_columns(a: np.ndarray):
    """
    Return array with columns in reverse order.
    - Input: 2D array 'a'
    - Return: 2D array with columns reversed
    """
    raise NotImplementedError

def extract_center_block(a: np.ndarray, size: int):
    """
    Extract a square center block from the array.
    - Input: 2D array 'a' and block size 'size'
    - Return: center block of shape (size, size)
    - Assume: a.shape[0] >= size and a.shape[1] >= size
    """
    raise NotImplementedError
```

#### 2.2 Multi-dimensional Slicing

```python
def get_3d_slice(arr_3d: np.ndarray, plane: str):
    """
    Extract 2D slices from 3D arrays.
    - Input: 3D array and plane ('xy', 'xz', or 'yz')
    - Return: 2D slice at the middle of the specified plane
    """
    raise NotImplementedError
```

---

## ✅ Section 3: Boolean Masking (COMPLETED)

**Goal:** Use boolean arrays to conditionally select elements.

### Proposed Exercises:

#### 3.1 Basic Boolean Masks

```python
def select_positive_elements(a: np.ndarray):
    """
    Return only positive elements from the array.
    - Input: 1D array 'a'
    - Return: 1D array of only positive values
    """
    raise NotImplementedError

def mask_above_threshold(a: np.ndarray, threshold: float):
    """
    Create boolean mask for elements above threshold.
    - Input: array 'a' and threshold value
    - Return: boolean array of same shape
    """
    raise NotImplementedError
```

#### 3.2 Conditional Selection

```python
def select_even_rows_odd_cols(a: np.ndarray):
    """
    Select elements where row index is even AND column index is odd.
    - Input: 2D array 'a'
    - Return: 1D array of selected elements
    """
    raise NotImplementedError

def replace_negative_with_zero(a: np.ndarray):
    """
    Replace all negative values with zero in-place.
    - Input: array 'a'
    - Return: modified array 'a'
    """
    raise NotImplementedError
```

---

## 🚧 Section 4: Fancy Indexing (NOT IMPLEMENTED)

**Goal:** Use integer arrays and advanced indexing techniques.

### Proposed Exercises:

#### 4.1 Integer Array Indexing

```python
def select_specific_indices(a: np.ndarray, row_indices: np.ndarray, col_indices: np.ndarray):
    """
    Select elements using arrays of indices.
    - Input: 2D array 'a' and 1D arrays of row/col indices
    - Return: 1D array of selected elements
    """
    raise NotImplementedError

def reorder_rows(a: np.ndarray, new_order: np.ndarray):
    """
    Reorder rows according to new_order array.
    - Input: 2D array 'a' and 1D array of new row order
    - Return: 2D array with reordered rows
    """
    raise NotImplementedError
```

#### 4.2 Advanced Indexing

```python
def extract_diagonal_pattern(a: np.ndarray, offset: int):
    """
    Extract diagonal elements with given offset.
    - Input: 2D array 'a' and offset (can be negative)
    - Return: 1D array of diagonal elements
    """
    raise NotImplementedError
```

---

## 🚧 Section 5: Advanced Operations (NOT IMPLEMENTED)

**Goal:** Combine multiple indexing techniques for complex operations.

### Proposed Exercises:

#### 5.1 Complex Selections

```python
def extract_chessboard_pattern(a: np.ndarray):
    """
    Extract elements in a chessboard pattern (alternating positions).
    - Input: 2D array 'a'
    - Return: 1D array of chessboard elements
    """
    raise NotImplementedError

def create_spiral_mask(shape: tuple):
    """
    Create a boolean mask that follows a spiral pattern.
    - Input: tuple of (rows, cols)
    - Return: boolean array with spiral pattern
    """
    raise NotImplementedError
```

#### 5.2 Performance Challenges

```python
def efficient_row_operations(a: np.ndarray, operation: str):
    """
    Perform operations on rows efficiently using indexing.
    - Input: 2D array 'a' and operation ('sum', 'max', 'min')
    - Return: 1D array of results
    - Constraint: no loops, use vectorized operations
    """
    raise NotImplementedError
```

---

## 🎯 Learning Objectives

By completing this challenge, you'll master:

1. **Basic Indexing** ✅ - Single elements, rows, columns
2. **Advanced Slicing** ✅ - Steps, negative indices, multi-D
3. **Boolean Masking** ✅ - Conditional selection
4. **Fancy Indexing** 🚧 - Integer arrays, advanced patterns
5. **Complex Operations** 🚧 - Combining multiple techniques

## 🧪 Testing Strategy

Each section includes:

- **Function definitions** with clear specifications
- **Comprehensive tests** that verify:
  - Correct output values
  - Proper data types
  - Array shapes
  - In-place modifications (where applicable)
- **Hints** for when you get stuck
- **Reference solutions** (hidden until completion)

## 🚀 Next Steps

1. **Complete Section 1** ✅ - You're done here!
2. **Complete Section 2** ✅ - Advanced slicing concepts mastered!
3. **Complete Section 3** ✅ - Boolean masking concepts mastered!
4. **Implement Section 4** - Fancy indexing concepts
5. **Work through Section 5** - Complex operations
6. **Run all tests** to ensure mastery of each concept

Remember: The goal is to build **intuition** for NumPy indexing, not just memorize syntax. Each exercise builds on the previous ones, so take your time and experiment!
