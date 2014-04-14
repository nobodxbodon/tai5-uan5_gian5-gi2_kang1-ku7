# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.閩南語音標介面 import 閩南語音標介面
import unicodedata

# 教會系羅馬音標聲調符號表 = dict(á = ('a', 2), à = ('a', 3), â = ('a', 5), ǎ = ('a', 6), ā = ('a', 7), a̍ = ('a', 8), a̋ = ('a', 9),
# é = ('e', 2), è = ('e', 3), ê = ('e', 5), ě = ('e', 6), ē = ('e', 7), e̍ = ('e', 8), e̋ = ('e', 9),
# í = ('i', 2), ì = ('i', 3), î = ('i', 5), ǐ = ('i', 6), ī = ('i', 7), i̍ = ('i', 8), i̋ = ('i', 9),
# ó = ('o', 2), ò = ('o', 3), ô = ('o', 5), ǒ = ('o', 6), ō = ('o', 7), o̍ = ('o', 8), ő = ('o', 9),
# ú = ('u', 2), ù = ('u', 3), û = ('u', 5), ǔ = ('u', 6), ū = ('u', 7), u̍ = ('u', 8), ű = ('u', 9),
# ḿ = ('m', 2), m̀ = ('m', 3), m̂ = ('m', 5), m̌ = ('m', 6), m̄ = ('m', 7), m̍ = ('m', 8), m̋ = ('m', 9),
# ń = ('n', 2), ǹ = ('n', 3), n̂ = ('n', 5), ň= ('n', 6), n̄ = ('n', 7), n̍ = ('n', 8), n̋ = ('n', 9),)
教會系羅馬音標聲調符號表 = {'á': ('a', 2), 'à': ('a', 3), 'â': ('a', 5), 'ǎ': ('a', 6), 'ā': ('a', 7), 'a̍': ('a', 8), 'a̋': ('a', 9),
'é': ('e', 2), 'è': ('e', 3), 'ê': ('e', 5), 'ě': ('e', 6), 'ē': ('e', 7), 'e̍': ('e', 8), 'e̋': ('e', 9),
'í': ('i', 2), 'ì': ('i', 3), 'î': ('i', 5), 'ǐ': ('i', 6), 'ī': ('i', 7), 'i̍': ('i', 8), 'i̋': ('i', 9),
'ó': ('o', 2), 'ò': ('o', 3), 'ô': ('o', 5), 'ǒ': ('o', 6), 'ō': ('o', 7), 'o̍': ('o', 8), 'ő': ('o', 9),
'ó͘': ('oo', 2), 'ò͘': ('oo', 3), 'ô͘': ('oo', 5), 'ǒ͘': ('oo', 6), 'ō͘': ('oo', 7), 'o̍͘': ('oo', 8), 'ő͘': ('oo', 9),
'ú': ('u', 2), 'ù': ('u', 3), 'û': ('u', 5), 'ǔ': ('u', 6), 'ū': ('u', 7), 'u̍': ('u', 8), 'ű': ('u', 9),
'ḿ': ('m', 2), 'm̀': ('m', 3), 'm̂': ('m', 5), 'm̌': ('m', 6), 'm̄': ('m', 7), 'm̍': ('m', 8), 'm̋': ('m', 9),
'ń': ('n', 2), 'ǹ': ('n', 3), 'n̂': ('n', 5), 'ň': ('n', 6), 'n̄': ('n', 7), 'n̍': ('n', 8), 'n̋': ('n', 9), 'ň' : ('n', 6), }

class 教會系羅馬音標(閩南語音標介面):
	# 0 tsh iaunnh 10
	音標上長長度 = 1 + 3 + 6 + 2
	聲 = None
	韻 = None
	調 = 1
	輕 = ''
	日本話 = ''
	音標 = None
	正規法 = lambda self, 音標:unicodedata.normalize('NFC', 音標)
	def 分析聲韻調(self, 音標):
		self.聲調符號表 = 教會系羅馬音標聲調符號表
# 		self.音標 = ''
		音標 = self.正規法(音標)
		if 音標.startswith('0'):
			self.輕 = '0'
			音標 = 音標[1:]
		elif 音標.startswith('1'):
			self.日本話 = '1'
			音標 = 音標[1:]
		self.音標 = self.__轉教羅韻符號(音標)
		音標是著的, 無調號音標 = self.__分離閏號聲調(self.音標)
		聲韻符合, self.聲, self.韻 = self.__揣聲韻(無調號音標)
		if not 聲韻符合:
			音標是著的 = False
		elif self.韻.endswith('p') or self.韻.endswith('t') or self.韻.endswith('k') or self.韻.endswith('h'):
			if self.調 == 1:
				self.調 = 4
			elif self.調 != 0 and self.調 != 4 and self.調 != 8 and self.調 != 10:
				音標是著的 = False
		if self.聲 == 'm' or self.聲 == 'ng':
			if self.韻 != 'ng' and self.韻 != 'ngh' and ('n' in self.韻 or 'm' in self.韻):
				音標是著的 = False
		self.調 = str(self.調)
		if 音標是著的:
			self.做音標()
		else:
			self.音標 = None
		return self.音標
	def 做音標(self):
		self.音標 = ''.join([self.輕, self.日本話, self.聲, self.韻, self.調])
	def __轉教羅韻符號(self, 音標):
		一開始 = True
		字元陣列 = []
		for 字元 in 音標:
			if 一開始:
				字元 = 字元.lower()
				一開始 = False
			if 字元 == '.' and self.音標[-1:] == ['o']:
				字元 = 'o'
			elif 字元 == 'o͘':
				字元 = 'oo'
			elif 字元 == 'N':
				字元 = 'nn'
			elif 字元 == 'ⁿ':
				字元 = 'nn'
			else:
				字元 = 字元.lower()
			字元陣列.append(字元)
		return ''.join(字元陣列)
	def __分離閏號聲調(self, 音標):
		無調號音標 = ''
		前一字元 = ''
		前一音調 = ''
		愛結束矣 = False
		音標是著的 = True
		for 字元 in self.音標 :
# 			print(無調號音標 + '  ' + 前一字元 + '  ' + 字元)
			if 前一音調 == '1' and 字元 == '0':
				self.調 = 10
				愛結束矣 = True
			elif 字元.isdigit():
				if self.調 == 1:
					self.調 = int(字元)
				else:
					音標是著的 = False
				愛結束矣 = True
				前一音調 = 字元
			elif 愛結束矣:
				音標是著的 = False
			elif 字元 in self.聲調符號表:
				無調字元 , self.調 = self.聲調符號表[字元]
				無調號音標 += 前一字元 + 無調字元
				前一字元 = ''
			elif 前一字元 + 字元 in self.聲調符號表:
				無調字元 , self.調 = self.聲調符號表[前一字元 + 字元]
				無調號音標 += 無調字元
				前一字元 = ''
			elif 無調號音標[-1:] + 前一字元 + 字元 in self.聲調符號表:
				無調字元 , self.調 = self.聲調符號表[無調號音標[-1:] + 前一字元 + 字元]
				無調號音標 = 無調號音標[:-1] + 無調字元
				前一字元 = ''
			else:
				無調號音標 += 前一字元
				前一字元 = 字元
		無調號音標 += 前一字元
		無調號音標 = 無調號音標.replace('o͘', 'oo')
		return 音標是著的, 無調號音標
	def __揣聲韻(self, 無調號音標):
		for 聲母 in self.聲母表:
			if 無調號音標.startswith(聲母):
				賰的 = 無調號音標[len(聲母):]
				if 賰的 in self.韻母表:
					return True, 聲母, 賰的
		return False, None, None
# 聲 介 韻 調，韻含元音跟韻尾

