import square.checker as check

def test_isMagic_ok(square_ok):
    ok = check.isMagicSquare(square_ok)
    assert ok

def test_isMagic_ko(square_ko):
    ok = check.isMagicSquare(square_ko)
    assert not ok

def test_all_present_ok(square12_ok_willem_barink):
    ok = check.allPresent(square12_ok_willem_barink)
    assert ok

def test_all_present_ok(square4_ko_josep_maria_subirachs):
    ok = check.allPresent(square4_ko_josep_maria_subirachs)
    assert ok