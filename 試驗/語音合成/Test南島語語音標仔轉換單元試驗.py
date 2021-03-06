# -*- coding: utf-8 -*-
from unittest.case import TestCase


from 臺灣言語工具.語音合成.南島語語音標仔轉換 import 南島語語音標仔轉換
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 南島語語音標仔轉換單元試驗(TestCase):

    def test_海岸阿美(self):
        句物件 = 拆文分析器.建立句物件("nga'ay ho")
        for 字物件, 音值 in zip(
            句物件.篩出字物件(),
            [[['ŋ', 'a'], ['ʔ', 'a', 'y']], [['h', 'u']]]
        ):
            字物件.音 = 音值
        self.assertEqual(
            南島語語音標仔轉換.物件轉完整合成標仔(句物件),
            [
                'x-sil+x/調:x<x>x/詞:x!x@x/句:x^x_x',
                'sil-ŋ+a/調:x<x>x/詞:0!2@2/句:0^2_2',
                'ŋ-a+ʔ/調:x<x>x/詞:0!2@2/句:0^2_2',
                'a-ʔ+a/調:x<x>x/詞:1!1@2/句:0^2_2',
                'ʔ-a+y/調:x<x>x/詞:1!1@2/句:0^2_2',
                'a-y+h/調:x<x>x/詞:1!1@2/句:0^2_2',
                'y-h+u/調:x<x>x/詞:0!1@1/句:1^1_2',
                'h-u+sil/調:x<x>x/詞:0!1@1/句:1^1_2',
                'x-sil+x/調:x<x>x/詞:x!x@x/句:x^x_x',
            ]
        )

    def test_有標點符號的無音(self):
        句物件 = 拆文分析器.建立句物件("nga'ay ho ?")
        for 字物件, 音值 in zip(
            句物件.篩出字物件(),
            [[['ŋ', 'a'], ['ʔ', 'a', 'y']], [['h', 'u']], '']
        ):
            字物件.音 = 音值
        self.assertEqual(
            南島語語音標仔轉換.物件轉完整合成標仔(句物件),
            [
                'x-sil+x/調:x<x>x/詞:x!x@x/句:x^x_x',
                'sil-ŋ+a/調:x<x>x/詞:0!2@2/句:0^3_3',
                'ŋ-a+ʔ/調:x<x>x/詞:0!2@2/句:0^3_3',
                'a-ʔ+a/調:x<x>x/詞:1!1@2/句:0^3_3',
                'ʔ-a+y/調:x<x>x/詞:1!1@2/句:0^3_3',
                'a-y+h/調:x<x>x/詞:1!1@2/句:0^3_3',
                'y-h+u/調:x<x>x/詞:0!1@1/句:1^2_3',
                'h-u+sil/調:x<x>x/詞:0!1@1/句:1^2_3',
                'x-sil+x/調:x<x>x/詞:x!x@x/句:x^x_x',
                'x-sil+x/調:x<x>x/詞:x!x@x/句:x^x_x',
            ]
        )

    def test_空的(self):
        句物件 = 拆文分析器.建立句物件("")
        self.assertEqual(
            南島語語音標仔轉換.物件轉完整合成標仔(句物件),
            [
                'x-sil+x/調:x<x>x/詞:x!x@x/句:x^x_x',
            ]
        )
