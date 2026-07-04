"""Analysis tools that consume the engine's output.

Unlike the engine layers (``models`` ← ``parsing`` ← ``loaders`` ← ``application``),
this package does not participate in derivation; it reads derivations and the
lexicon's target annotations to measure and report on them. The grader
(:mod:`src.fortis.analysis.grading`) is the first such tool.
"""
