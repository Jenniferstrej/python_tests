import unittest
from ddt import ddt, data, unpack
from sample import activity_DepositAssets

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.depositassets = activity_DepositAssets()

    @unpack
    @data({'input': '.tif', 'expected': ['.tif']},
          {'input': '.jpg, .tiff, .png', 'expected':['.jpg', '.tiff', '.png']})
    def test_get_no_download_extensions(self, input, expected):
        result = self.depositassets.get_no_download_extensions(input)
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
