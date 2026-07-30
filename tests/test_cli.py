def test_convert_simple():
    from markdown_compiler import convert

    html = convert("**bold**")
    assert "<strong>bold</strong>" in html
