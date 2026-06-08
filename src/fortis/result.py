"""A Rust-style ``Result`` type for explicit, composable error handling.

``Result[T, E]`` is either ``Ok[T]`` (success) or ``Err[E]`` (failure). The
combinator methods (``map``, ``map_err``, ``and_then``, ``or_else``,
``unwrap_or_else``) let fallible stages be threaded together without
unwrapping; the first ``Err`` short-circuits the rest of a chain.
"""

from collections.abc import Callable
from dataclasses import dataclass
from typing import NoReturn


class ResultError(Exception):
    """Raised when a ``Result`` is unwrapped on the wrong variant."""


@dataclass(frozen=True, slots=True)
class Ok[T]:
    """A successful outcome.

    Attributes:
        value: The contained success value.
    """

    value: T

    def is_ok(self) -> bool:
        """Reports whether this is an ``Ok``.

        Returns:
            Always ``True``.
        """
        return True

    def is_err(self) -> bool:
        """Reports whether this is an ``Err``.

        Returns:
            Always ``False``.
        """
        return False

    def unwrap(self) -> T:
        """Returns the contained value.

        Returns:
            The inner success value.
        """
        return self.value

    def unwrap_err(self) -> NoReturn:
        """Fails, since there is no error to extract.

        Raises:
            ResultError: Always.
        """
        raise ResultError(f"Called unwrap_err() on an Ok value: {self.value!r}")

    def unwrap_or(self, default: object) -> T:  # noqa: ARG002
        """Returns the contained value, ignoring the default.

        Args:
            default: Unused fallback.

        Returns:
            The inner success value.
        """
        return self.value

    def unwrap_or_else(self, op: Callable[[object], object]) -> T:  # noqa: ARG002
        """Returns the contained value, never calling ``op``.

        Args:
            op: Unused recovery function.

        Returns:
            The inner success value.
        """
        return self.value

    def expect(self, msg: str) -> T:  # noqa: ARG002
        """Returns the contained value, ignoring the assertion message.

        Args:
            msg: Unused message describing the expected invariant.

        Returns:
            The inner success value.
        """
        return self.value

    def map[U](self, op: Callable[[T], U]) -> Ok[U]:
        """Transforms the contained value with ``op``.

        Args:
            op: Function applied to the success value.

        Returns:
            ``Ok`` wrapping ``op(value)``.
        """
        return Ok(op(self.value))

    def map_err(self, op: Callable[[object], object]) -> Ok[T]:  # noqa: ARG002
        """Leaves an ``Ok`` unchanged.

        Args:
            op: Unused error-mapping function.

        Returns:
            This instance.
        """
        return self

    def and_then[U, F](self, op: Callable[[T], Result[U, F]]) -> Result[U, F]:
        """Chains a fallible computation onto the contained value.

        Args:
            op: Function returning a new ``Result``.

        Returns:
            The ``Result`` produced by ``op(value)``.
        """
        return op(self.value)

    def or_else(self, op: Callable[[object], object]) -> Ok[T]:  # noqa: ARG002
        """Leaves an ``Ok`` unchanged.

        Args:
            op: Unused recovery function.

        Returns:
            This instance.
        """
        return self


@dataclass(frozen=True, slots=True)
class Err[E]:
    """A failed outcome.

    Attributes:
        error: The contained error value.
    """

    error: E

    def is_ok(self) -> bool:
        """Reports whether this is an ``Ok``.

        Returns:
            Always ``False``.
        """
        return False

    def is_err(self) -> bool:
        """Reports whether this is an ``Err``.

        Returns:
            Always ``True``.
        """
        return True

    def unwrap(self) -> NoReturn:
        """Fails, since there is no success value to extract.

        Raises:
            ResultError: Always.
        """
        raise ResultError(f"Called unwrap() on an Err value: {self.error!r}")

    def unwrap_err(self) -> E:
        """Returns the contained error.

        Returns:
            The inner error value.
        """
        return self.error

    def unwrap_or[U](self, default: U) -> U:
        """Returns the provided default.

        Args:
            default: Fallback returned in place of a value.

        Returns:
            ``default``.
        """
        return default

    def unwrap_or_else[U](self, op: Callable[[E], U]) -> U:
        """Computes a fallback from the contained error.

        Args:
            op: Function applied to the error to produce a fallback.

        Returns:
            ``op(error)``.
        """
        return op(self.error)

    def expect(self, msg: str) -> NoReturn:
        """Fails with a caller-supplied message.

        Args:
            msg: Description of the invariant expected to hold.

        Raises:
            ResultError: Always.
        """
        raise ResultError(f"{msg}: {self.error!r}")

    def map(self, op: Callable[[object], object]) -> Err[E]:  # noqa: ARG002
        """Leaves an ``Err`` unchanged.

        Args:
            op: Unused value-mapping function.

        Returns:
            This instance.
        """
        return self

    def map_err[F](self, op: Callable[[E], F]) -> Err[F]:
        """Transforms the contained error with ``op``.

        Args:
            op: Function applied to the error value.

        Returns:
            ``Err`` wrapping ``op(error)``.
        """
        return Err(op(self.error))

    def and_then[U](self, op: Callable[[object], object]) -> Err[E]:  # noqa: ARG002
        """Leaves an ``Err`` unchanged.

        Args:
            op: Unused chaining function.

        Returns:
            This instance.
        """
        return self

    def or_else[U, F](self, op: Callable[[E], Result[U, F]]) -> Result[U, F]:
        """Recovers from the error with a fallible computation.

        Args:
            op: Function returning a new ``Result`` from the error.

        Returns:
            The ``Result`` produced by ``op(error)``.
        """
        return op(self.error)


type Result[T, E] = Ok[T] | Err[E]


def present_errors(errors: list[str] | str) -> str:
    """Format error strings into a single human-readable message.

    A single string passes through unchanged; a list of strings is
    newline-joined.

    Args:
        errors: One error string or a list of error strings to format.

    Returns:
        A newline-joined string of all error messages.
    """
    if isinstance(errors, str):
        return errors
    return "\n".join(errors)
