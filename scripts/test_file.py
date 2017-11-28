import os
import unittest
import subprocess



def analyze_hbase():
    """Checking the number of records in hbase table"""
    hbase_count = 0
    hbase_count = int(subprocess.check_output("hbase shell ./hbase_cmd.txt | tail -2 | sed \'/^$/d\' | awk \'{print $1}\'", shell=True, universal_newlines=True).strip())

    return(hbase_count)



def analyze_text(filename):
    """Calculate the number of lines and characters in a file.

    Args:
        filename: The name of the file to analyze.

    Raises:
        IOError: If ``filename`` does not exist or can't be read.

    Returns: A tuple where the first element is the number of lines in
        the file and the second element is the number of characters.
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)


class TextAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'trial.csv'
        f = open(self.filename, 'r')


    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.close(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename)[0], analyze_hbase())


    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file."""
        with self.assertRaises(IOError):
            analyze_text('trial.csv')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()

