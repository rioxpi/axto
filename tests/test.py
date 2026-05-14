from axto import Engine

def test_engine():
    engine = Engine()
    assert not engine.running, "Engine should not be running initially"
    
    engine.start()
    assert engine.running, "Engine should be running after start()"
    
    engine.stop()
    assert not engine.running, "Engine should not be running after stop()"

if __name__ == "__main__":
    test_engine()
    print("All tests passed!")