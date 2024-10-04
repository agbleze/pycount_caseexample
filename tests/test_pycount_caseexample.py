import matplotlib.container
from pycount_caseexample.pycount_caseexample import count_words
from collections import Counter
from pycount_caseexample.plotting import plot_words
import matplotlib
import pytest

@pytest.fixture
def einstein_counts():
    return Counter({'insanity': 1, 'is': 1, 'doing': 1, 
                    'the': 1, 'same': 1, 'thing': 1, 
                    'over': 2, 'and': 2, 'expecting': 1,
                    'different': 1, 'results': 1})
    
def test_count_words(einstein_counts):
    """Test word counting from a file."""
    expected = einstein_counts
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"

def test_plot_words(einstein_counts):
    """Test plotting of word counts."""
    counts = einstein_counts
    fig = plot_words(counts)
    assert isinstance(fig, matplotlib.container.BarContainer), "wrong plot type"
    assert len(fig.datavalues) == 10, "incorrect number of bars plotted"
    
@pytest.mark.parametrize("obj", [3.141, "test.txt", ["list", "of", "words"]])   
def test_plot_words_error(obj):
    """Check TypeError raised when Counter not used."""
    with pytest.raises(TypeError):
        plot_words(obj)
        
def test_integration():
    """Test count_words() and plot_words() workflow."""
    counts = count_words("tests/einstein.txt")
    fig = plot_words(counts)
    assert isinstance(fig, matplotlib.container.BarContainer), "wrong plot type"
    assert len(fig.datavalues) == 10, "incorrect number of bars plotted"
    assert max(fig.datavalues) == 2, "Highest word count should be 2"

def is_even(n):
    """Check if n is even"""
    if n % 2 == 0:
        return True
    else:
        return False
@pytest.mark.parametrize("n, result", [(2, True), (3, False), (4, True)])
def test_is_even(n, result):
    assert is_even(n) == result