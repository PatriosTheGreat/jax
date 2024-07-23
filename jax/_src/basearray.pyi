# Copyright 2022 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import abc
from collections.abc import Callable, Sequence
from typing import Any, Union
import numpy as np

from jax._src.sharding import Sharding

Shard = Any

# TODO: alias this to xla_client.Traceback
Device = Any
Traceback = Any


class Array(abc.ABC):
  aval: Any

  @property
  def dtype(self) -> np.dtype: ...

  @property
  def ndim(self) -> int: ...

  @property
  def size(self) -> int: ...

  @property
  def itemsize(self) -> int: ...

  @property
  def shape(self) -> tuple[int, ...]: ...

  def __init__(self, shape, dtype=None, buffer=None, offset=0, strides=None,
               order=None):
    raise TypeError("jax.numpy.ndarray() should not be instantiated explicitly."
                    " Use jax.numpy.array, or jax.numpy.zeros instead.")

  def __getitem__(self, key) -> Array: ...
  def __setitem__(self, key, value) -> None: ...
  def __len__(self) -> int: ...
  def __iter__(self) -> Any: ...
  def __reversed__(self) -> Any: ...
  def __round__(self, ndigits=None) -> Array: ...

  # Comparisons

  # these return bool for object, so ignore override errors.
  def __lt__(self, other) -> Array: ...
  def __le__(self, other) -> Array: ...
  def __eq__(self, other) -> Array: ...  # type: ignore[override]
  def __ne__(self, other) -> Array: ...  # type: ignore[override]
  def __gt__(self, other) -> Array: ...
  def __ge__(self, other) -> Array: ...

  # Unary arithmetic

  def __neg__(self) -> Array: ...
  def __pos__(self) -> Array: ...
  def __abs__(self) -> Array: ...
  def __invert__(self) -> Array: ...

  # Binary arithmetic

  def __add__(self, other) -> Array: ...
  def __sub__(self, other) -> Array: ...
  def __mul__(self, other) -> Array: ...
  def __matmul__(self, other) -> Array: ...
  def __truediv__(self, other) -> Array: ...
  def __floordiv__(self, other) -> Array: ...
  def __mod__(self, other) -> Array: ...
  def __divmod__(self, other) -> Array: ...
  def __pow__(self, other) -> Array: ...
  def __lshift__(self, other) -> Array: ...
  def __rshift__(self, other) -> Array: ...
  def __and__(self, other) -> Array: ...
  def __xor__(self, other) -> Array: ...
  def __or__(self, other) -> Array: ...

  def __radd__(self, other) -> Array: ...
  def __rsub__(self, other) -> Array: ...
  def __rmul__(self, other) -> Array: ...
  def __rmatmul__(self, other) -> Array: ...
  def __rtruediv__(self, other) -> Array: ...
  def __rfloordiv__(self, other) -> Array: ...
  def __rmod__(self, other) -> Array: ...
  def __rdivmod__(self, other) -> Array: ...
  def __rpow__(self, other) -> Array: ...
  def __rlshift__(self, other) -> Array: ...
  def __rrshift__(self, other) -> Array: ...
  def __rand__(self, other) -> Array: ...
  def __rxor__(self, other) -> Array: ...
  def __ror__(self, other) -> Array: ...

  def __bool__(self) -> bool: ...
  def __complex__(self) -> complex: ...
  def __int__(self) -> int: ...
  def __float__(self) -> float: ...
  def __index__(self) -> int: ...

  def __buffer__(self, flags: int) -> memoryview: ...
  def __release_buffer__(self, view: memoryview) -> None: ...

  # np.ndarray methods:
  def all(self, axis: int | Sequence[int] | None = None, out=None,
          keepdims=None, *, where: ArrayLike | None = ...) -> Array: ...
  def any(self, axis: int | Sequence[int] | None = None, out=None,
          keepdims=None, *, where: ArrayLike | None = ...) -> Array: ...
  def argmax(self, axis: int | None = None, out=None, keepdims=None) -> Array: ...
  def argmin(self, axis: int | None = None, out=None, keepdims=None) -> Array: ...
  def argpartition(self, kth, axis=-1, kind='introselect', order=None) -> Array: ...
  def argsort(self, axis: int | None = -1, kind='quicksort', order=None) -> Array: ...
  def astype(self, dtype) -> Array: ...
  def choose(self, choices, out=None, mode='raise') -> Array: ...
  def clip(self, min=None, max=None, out=None) -> Array: ...
  def compress(self, condition, axis: int | None = None, out=None) -> Array: ...
  def conj(self) -> Array: ...
  def conjugate(self) -> Array: ...
  def copy(self) -> Array: ...
  def cumprod(self, axis: int | Sequence[int] | None = None,
              dtype=None, out=None) -> Array: ...
  def cumsum(self, axis: int | Sequence[int] | None = None,
             dtype=None, out=None) -> Array: ...
  def diagonal(self, offset=0, axis1: int = 0, axis2: int = 1) -> Array: ...
  def dot(self, b, *, precision=None) -> Array: ...
  def flatten(self) -> Array: ...
  @property
  def imag(self) -> Array: ...
  def item(self, *args) -> Any: ...
  def max(self, axis: int | Sequence[int] | None = None, out=None,
          keepdims=None, initial=None, where=None) -> Array: ...
  def mean(self, axis: int | Sequence[int] | None = None, dtype=None,
           out=None, keepdims=False, *, where=None,) -> Array: ...
  def min(self, axis: int | Sequence[int] | None = None, out=None,
          keepdims=None, initial=None, where=None) -> Array: ...
  @property
  def nbytes(self) -> int: ...
  def nonzero(self, *, size=None, fill_value=None) -> Array: ...
  def prod(self, axis: int | Sequence[int] | None = None, dtype=None,
           out=None, keepdims=None, initial=None, where=None) -> Array: ...
  def ptp(self, axis: int | Sequence[int] | None = None, out=None,
          keepdims=False,) -> Array: ...
  def ravel(self, order='C') -> Array: ...
  @property
  def real(self) -> Array: ...
  def repeat(self, repeats, axis: int | None = None, *,
             total_repeat_length=None) -> Array: ...
  def reshape(self, *args, order='C') -> Array: ...
  def round(self, decimals=0, out=None) -> Array: ...
  def searchsorted(self, v, side='left', sorter=None) -> Array: ...
  def sort(self, axis: int | None = -1, kind='quicksort', order=None) -> Array: ...
  def squeeze(self, axis: int | Sequence[int] | None = None) -> Array: ...
  def std(self, axis: int | Sequence[int] | None = None,
          dtype=None, out=None, ddof=0, keepdims=False, *, where=None) -> Array: ...
  def sum(self, axis: int | Sequence[int] | None = None, dtype=None,
          out=None, keepdims=None, initial=None, where=None) -> Array: ...
  def swapaxes(self, axis1: int, axis2: int) -> Array: ...
  def take(self, indices, axis: int | None = None, out=None,
           mode=None) -> Array: ...
  def tobytes(self, order='C') -> bytes: ...
  def tolist(self) -> list[Any]: ...
  def trace(self, offset=0, axis1: int = 0, axis2: int = 1, dtype=None,
            out=None) -> Array: ...
  def transpose(self, *args) -> Array: ...
  @property
  def T(self) -> Array: ...
  @property
  def mT(self) -> Array: ...
  def var(self, axis: int | Sequence[int] | None = None,
          dtype=None, out=None, ddof=0, keepdims=False, *, where=None) -> Array: ...
  def view(self, dtype=None, type=None) -> Array: ...

  # Even though we don't always support the NumPy array protocol, e.g., for
  # tracer types, for type checking purposes we must declare support so we
  # implement the NumPy ArrayLike protocol.
  def __array__(self, dtype: np.dtype | None = ...,
                copy: bool | None = ...) -> np.ndarray: ...
  def __dlpack__(self) -> Any: ...

  # JAX extensions
  @property
  def at(self) -> _IndexUpdateHelper: ...
  @property
  def weak_type(self) -> bool: ...

  # Methods defined on ArrayImpl, but not on Tracers
  def addressable_data(self, index: int) -> Array: ...
  def block_until_ready(self) -> Array: ...
  def copy_to_host_async(self) -> None: ...
  def delete(self) -> None: ...
  def devices(self) -> set[Device]: ...
  @property
  def sharding(self) -> Sharding: ...
  @property
  def device(self) -> Device | Sharding: ...
  @property
  def addressable_shards(self) -> Sequence[Shard]: ...
  @property
  def global_shards(self) -> Sequence[Shard]: ...
  def is_deleted(self) -> bool: ...
  @property
  def is_fully_addressable(self) -> bool: ...
  @property
  def is_fully_replicated(self) -> bool: ...
  def on_device_size_in_bytes(self) -> int: ...
  @property
  def traceback(self) -> Traceback: ...
  def unsafe_buffer_pointer(self) -> int: ...
  def to_device(self, device: Device | Sharding, *, stream: int | Any | None) -> Array: ...


StaticScalar = Union[
  np.bool_, np.number,  # NumPy scalar types
  bool, int, float, complex,  # Python scalar types
]

ArrayLike = Union[
  Array,  # JAX array type
  np.ndarray,  # NumPy array type
  StaticScalar,  # valid scalars
]


# TODO: restructure to avoid re-defining this here?
# from jax._src.numpy.lax_numpy import _IndexUpdateHelper

class _IndexUpdateHelper:
  def __getitem__(self, index: Any) -> _IndexUpdateRef: ...

class _IndexUpdateRef:
  def get(self, indices_are_sorted: bool = False, unique_indices: bool = False,
          mode: str | None = None, fill_value: StaticScalar | None = None) -> Array: ...
  def set(self, values: Any,
          indices_are_sorted: bool = False, unique_indices: bool = False,
          mode: str | None = None, fill_value: StaticScalar | None = None) -> Array: ...
  def add(self, values: Any, indices_are_sorted: bool = False,
          unique_indices: bool = False, mode: str | None = None) -> Array: ...
  def mul(self, values: Any, indices_are_sorted: bool = False,
          unique_indices: bool = False, mode: str | None = None) -> Array: ...
  def multiply(self, values: Any, indices_are_sorted: bool = False,
               unique_indices: bool = False, mode: str | None = None) -> Array: ...
  def divide(self, values: Any, indices_are_sorted: bool = False,
             unique_indices: bool = False, mode: str | None = None) -> Array: ...
  def power(self, values: Any, indices_are_sorted: bool = False,
            unique_indices: bool = False, mode: str | None = None) -> Array: ...
  def min(self, values: Any, indices_are_sorted: bool = False,
          unique_indices: bool = False, mode: str | None = None) -> Array: ...
  def max(self, values: Any, indices_are_sorted: bool = False,
          unique_indices: bool = False, mode: str | None = None) -> Array: ...
  def apply(self, func: Callable[[ArrayLike], ArrayLike], indices_are_sorted: bool = False,
            unique_indices: bool = False, mode: str | None = None) -> Array: ...
