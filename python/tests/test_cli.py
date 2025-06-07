from mlc_llm import cli


def test_cli_default_output(capsys):
    cli.main()
    captured = capsys.readouterr()
    assert "MLC LLM CLI works!" in captured.out
