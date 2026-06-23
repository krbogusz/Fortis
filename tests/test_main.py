"""Smoke test for the end-to-end pipeline (src/fortis/main.py)."""

from src.fortis.main import main


def test_main_derives_every_word(project, capsys):
    main()
    out = capsys.readouterr().out
    # One surface form per word, and known syllabified derivations come through.
    assert out.count("Surface:") == len(project.words)
    assert "ˈħan.ti" in out  # *h₂énti: a-coloured by h₂ (now ħ, [+low]), stress kept
    assert "wul.kʷos" in out  # centumization + u-epenthesis, then syllabified
