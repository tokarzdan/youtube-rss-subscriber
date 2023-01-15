import unittest
from youtube_rss_subscriber import video_filter_match

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.filters = ["Official Music Video", "Official Video", "Music Video"]

    def test_match_upper(self):
        self.assertTrue(video_filter_match("San Luis (OFFICIAL VIDEO)", self.filters))

    def test_match_lower(self):
        self.assertTrue(video_filter_match("San Luis (official music video)", self.filters))

    def test_no_match(self):
        self.assertFalse(video_filter_match("San Luis", self.filters))
        self.assertFalse(video_filter_match("San Luis (Official)", self.filters))




if __name__ == "__main__":
    unittest.main()
