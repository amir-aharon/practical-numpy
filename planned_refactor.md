# Planned Refactoring - PEP8 Compliance & Type Annotations

## 🎯 Overview

This document outlines all the PEP8 violations and missing type annotations found in the codebase that need to be fixed during refactoring.

## 📁 Files to Refactor

### 1. **tests/utils.py** - Critical Issues Found

#### **PEP8 Violations:**

- **Line 16-22**: `pretty_bool()` function has broken logic
  - Missing `output = ""` initialization
  - Unused `output` variable
  - Function returns undefined `output`

#### **Missing Type Annotations:**

- **Line 3**: `pretty(a, max_rows=6, max_cols=12, decimals=3)`
  - Missing parameter types and return type
- **Line 16**: `pretty_bool(a)`
  - Missing parameter type and return type
- **Line 25**: `format_output(obj)`
  - Missing parameter type and return type

#### **Proposed Fixes:**

```python
def pretty(a: Any, max_rows: int = 6, max_cols: int = 12, decimals: int = 3) -> np.ndarray:
def pretty_bool(a: np.ndarray) -> str:
def format_output(obj: Any) -> str:
```

---

### 2. **tests/challenge_01/section_01.py** - Minor Issues

#### **Missing Type Annotations:**

- **Line 4**: `run_all(ns)`
  - Missing parameter type and return type
- **Line 51**: Return type missing

#### **Proposed Fixes:**

```python
def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
```

---

### 3. **tests/challenge_01/section_02.py** - Minor Issues

#### **Missing Type Annotations:**

- **Line 4**: `run_all(ns)`
  - Missing parameter type and return type
- **Line 48**: Return type missing

#### **Proposed Fixes:**

```python
def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
```

---

### 4. **tests/challenge_01/section_03.py** - Minor Issues

#### **Missing Type Annotations:**

- **Line 4**: `run_all(ns)`
  - Missing parameter type and return type
- **Line 61**: Return type missing

#### **Proposed Fixes:**

```python
def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
```

---

### 5. **tests/challenge_01/section_04.py** - Minor Issues

#### **Missing Type Annotations:**

- **Line 4**: `run_all(ns)`
  - Missing parameter type and return type
- **Line 47**: Return type missing

#### **Proposed Fixes:**

```python
def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
```

---

### 6. **tests/challenge_01/section_05.py** - Minor Issues

#### **Missing Type Annotations:**

- **Line 4**: `run_all(ns)`
  - Missing parameter type and return type
- **Line 66**: Return type missing

#### **Proposed Fixes:**

```python
def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
```

---

### 7. **tests/challenge_02/section_01.py** - Minor Issues

#### **Missing Type Annotations:**

- **Line 4**: `run_all(ns)`
  - Missing parameter type and return type
- **Line 58**: Return type missing

#### **Proposed Fixes:**

```python
def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
```

---

### 8. **tests/challenge_02/section_02.py** - Minor Issues

#### **Missing Type Annotations:**

- **Line 4**: `run_all(ns)`
  - Missing parameter type and return type
- **Line 67**: Return type missing

#### **Proposed Fixes:**

```python
def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
```

---

### 9. **tests/challenge_02/section_03.py** - Minor Issues

#### **Missing Type Annotations:**

- **Line 4**: `run_all(ns)`
  - Missing parameter type and return type
- **Line 69**: Return type missing

#### **Proposed Fixes:**

```python
def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
```

---

## 🔧 **Required Imports for Type Annotations**

All test files will need these imports:

```python
from typing import Dict, Any, Tuple
import numpy as np
```

## 📊 **Summary of Issues**

### **Critical Issues (1 file):**

- `tests/utils.py` - Broken function logic, missing type annotations

### **Minor Issues (8 files):**

- All test files missing type annotations for `run_all()` functions
- Consistent pattern across all test files

### **Total Files to Refactor:** 9

## 🚀 **Refactoring Priority**

1. **HIGH PRIORITY**: Fix `tests/utils.py` broken function
2. **MEDIUM PRIORITY**: Add type annotations to all test files
3. **LOW PRIORITY**: Verify all functions follow consistent naming conventions

## 📝 **Notes**

- All notebook files (`practical_numpy_*.ipynb`) appear to follow PEP8 conventions
- Function definitions in notebooks already have proper type annotations
- Test files follow consistent structure and naming conventions
- No major PEP8 violations found beyond type annotations
- The refactoring will be straightforward and low-risk
