from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.公用變數 import 分字符號
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.音標系統.閩南語綜合標音 import 閩南語綜合標音
from unittest.mock import patch


class 章單元試驗(TestCase):

    def test_章烏白傳(self):
        self.assertRaises(型態錯誤, 章, None)
        self.assertRaises(型態錯誤, 章, [None])
        self.assertRaises(型態錯誤, 章, ['sui2'])

    def test_看章(self):
        型 = '恁老母ti3佗位！恁老母ti3佗位！'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7 ! lin1 lau3 bu2 ti3 to1 ui7 !'
        章物件 = 拆文分析器.對齊章物件(型, 音)
        self.assertEqual(章物件.看型(), 型)
        self.assertEqual(章物件.看音(), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜! 恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜!'
        self.assertEqual(章物件.看分詞(), 分詞)
        self.assertEqual(章物件.看分詞('｜'), 分詞)
        分詞加 = '恁+lin1 老+lau3 母+bu2 ti3+ti3 佗+to1 位+ui7 ！+! 恁+lin1 老+lau3 母+bu2 ti3+ti3 佗+to1 位+ui7 ！+!'
        self.assertEqual(章物件.看分詞('+'), 分詞加)

    def test_看章加連字符(self):
        型 = '恁老母ti3佗位！恁lau3-bu2-ti3佗位！'
        音 = 'lin1 lau3-bu2 ti3 to1 ui7 ! lin1 lau3-bu2-ti3 to1-ui7 !'
        章物件 = 拆文分析器.對齊章物件(型, 音)
        無分字型 = 型.replace(分字符號, '')
        self.assertEqual(章物件.看型(), 無分字型)
        self.assertEqual(章物件.看音(), 音)
        分詞 = '恁｜lin1 老-母｜lau3-bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜! 恁｜lin1 lau3-bu2-ti3｜lau3-bu2-ti3 佗-位｜to1-ui7 ！｜!'
        self.assertEqual(章物件.看分詞(), 分詞)
        self.assertEqual(章物件.看分詞('｜'), 分詞)
        self.assertEqual(章物件.看分詞(物件分型音符號='｜'), 分詞)

    def test_看章換連字符(self):
        型 = '恁老母ti3佗位！恁老母ti3佗位！'
        音 = 'lin1 lau3-bu2 ti3 to1 ui7 ! lin1 lau3-bu2-ti3 to1-ui7 !'
        答型 = '恁|老_母|ti3|佗|位|！^恁|老_母_ti3|佗_位|！'
        答音 = 'lin1|lau3_bu2|ti3|to1|ui7|!^lin1|lau3_bu2_ti3|to1_ui7|!'
        章物件 = 拆文分析器.對齊章物件(型, 音)
        self.assertEqual(章物件.看型('_', '|', '^'), 答型)
        self.assertEqual(章物件.看音('_', '|', '^'), 答音)
        self.assertEqual(
            章物件.看型(物件分字符號='_', 物件分詞符號='|', 物件分句符號='^'), 答型)
        self.assertEqual(
            章物件.看音(物件分字符號='_', 物件分詞符號='|', 物件分句符號='^'), 答音)
        分詞 = '恁@lin1^老_母@lau3_bu2^ti3@ti3^佗@to1^位@ui7^！@!|恁@lin1^老_母_ti3@lau3_bu2_ti3^佗_位@to1_ui7^！@!'
        self.assertEqual(章物件.看分詞('@', '_', '^', '|'), 分詞)
        self.assertEqual(
            章物件.看分詞(物件分型音符號='@', 物件分字符號='_', 物件分詞符號='^', 物件分句符號='|'), 分詞
        )

    def test_預設分句符號(self):
        原本語句 = '食-飽｜tsiah8-pa2 未｜0bue7 ？｜? 食-飽｜tsiah8-pa2 矣｜0ah4 ！｜!'
        章物件 = 拆文分析器.分詞章物件(原本語句)
        self.assertEqual(章物件.看型(),
                         '食飽未？食飽矣！')
        self.assertEqual(章物件.看音(),
                         'tsiah8-pa2 0bue7 ? tsiah8-pa2 0ah4 !')
        self.assertEqual(章物件.看分詞(),
                         '食-飽｜tsiah8-pa2 未｜0bue7 ？｜? 食-飽｜tsiah8-pa2 矣｜0ah4 ！｜!')

    def test_換句分句符號(self):
        原本語句 = '食-飽｜tsiah8-pa2 未｜0bue7 ？｜? 食-飽｜tsiah8-pa2 矣｜0ah4 ！｜!'
        章物件 = 拆文分析器.分詞章物件(原本語句)
        self.assertEqual(章物件.看型(物件分句符號='\n'),
                         '食飽未？\n食飽矣！')
        self.assertEqual(章物件.看音(物件分句符號='\n'),
                         'tsiah8-pa2 0bue7 ?\ntsiah8-pa2 0ah4 !')
        self.assertEqual(章物件.看分詞(物件分句符號='\n'),
                         '食-飽｜tsiah8-pa2 未｜0bue7 ？｜?\n食-飽｜tsiah8-pa2 矣｜0ah4 ！｜!')

    def test_綜合標音章物件(self):
        章物件 = 拆文分析器.對齊章物件('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8 kha1,')
        頭一句, 上尾句 = 章物件.綜合標音(閩南語綜合標音)
        self.assertIn('漢字', 頭一句)
        self.assertIn('臺羅數字調', 頭一句)
        self.assertIn('臺羅閏號調', 頭一句)
        self.assertIn('通用數字調', 頭一句)
        self.assertIn('吳守禮方音', 頭一句)
        self.assertIn('分詞', 頭一句)
        self.assertIn('漢字', 上尾句)
        self.assertIn('臺羅數字調', 上尾句)
        self.assertIn('臺羅閏號調', 上尾句)
        self.assertIn('通用數字調', 上尾句)
        self.assertIn('吳守禮方音', 上尾句)
        self.assertIn('分詞', 上尾句)

    @patch('臺灣言語工具.基本物件.句.句.綜合標音')
    def test_綜合標音用句的來鬥(self, 句綜合標音mock):
        章物件 = 拆文分析器.對齊章物件('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8 kha1,')
        self.assertEqual(章物件.綜合標音(閩南語綜合標音), [
            句綜合標音mock.return_value[0],
            句綜合標音mock.return_value[0],
        ])
