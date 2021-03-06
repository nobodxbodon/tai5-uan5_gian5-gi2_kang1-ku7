# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.語音合成.閩南語音韻.變調判斷 import 變調判斷
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 試驗.語音合成.閩南語音韻.變調判斷規則 import 全部規則


def _產生變調判斷單元試驗():
    def 產生套用前物件(self, 漢字, 臺羅):
        return (
            拆文分析器.對齊章物件(漢字, 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅))
            .轉音(臺灣閩南語羅馬字拼音)
            .轉音(臺灣閩南語羅馬字拼音, 函式='音值')
        )

    def 判斷(漢字, 臺羅, 答案):
        def 試(self):
            章物件 = self.產生套用前物件(漢字, 臺羅)
            self.assertEqual(變調判斷.判斷(章物件), 答案, '\n{}\n{}'.format(漢字, 臺羅))
        return 試

    試驗函式 = {'判斷': 判斷, '產生套用前物件': 產生套用前物件}
    for 編號, 試驗 in enumerate(全部規則):
        試驗函式['test_{}_{}' .format(試驗['名'], 編號)] = (
            判斷(試驗['漢字'], 試驗['臺羅'], 試驗['答案'])
        )
    return type('變調判斷單元試驗', (TestCase,), 試驗函式)


變調判斷單元試驗 = _產生變調判斷單元試驗()
