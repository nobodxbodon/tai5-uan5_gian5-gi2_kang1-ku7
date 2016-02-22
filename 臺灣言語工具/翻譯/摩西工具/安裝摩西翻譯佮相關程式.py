# -*- coding: utf-8 -*-
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
from os import makedirs
from os.path import join, isdir
from shutil import copy


from 臺灣言語工具.系統整合.外部程式 import 外部程式


class 安裝摩西翻譯佮相關程式(程式腳本):
    pull深度 = '100'

    @classmethod
    def 安裝moses(cls, moses安裝路徑=外部程式.目錄(), 編譯CPU數=4):
        makedirs(moses安裝路徑, exist_ok=True)
        moses程式碼目錄 = join(moses安裝路徑, 'mosesdecoder')
        if not isdir(moses程式碼目錄):
            with cls._換目錄(moses安裝路徑):
                cls._下載專案(
                    'https://github.com/moses-smt/mosesdecoder.git'
                )
        else:
            with cls._換目錄(moses程式碼目錄):
                cls._更新專案()
        with cls._換目錄(moses程式碼目錄):
            cls._走指令(['./bjam', '-j{0}'.format(編譯CPU數)], 愛直接顯示輸出=True)

    @classmethod
    def 安裝gizapp(cls, gizapp安裝路徑=外部程式.目錄()):
        makedirs(gizapp安裝路徑, exist_ok=True)
        gizapp程式碼目錄 = join(gizapp安裝路徑, 'giza-pp')
        if not isdir(gizapp程式碼目錄):
            with cls._換目錄(gizapp安裝路徑):
                cls._下載專案(
                    'https://github.com/sih4sing5hong5/giza-pp.git'
                )
        else:
            with cls._換目錄(gizapp程式碼目錄):
                cls._更新專案()
        with cls._換目錄(gizapp程式碼目錄):
            cls._走指令('make', 愛直接顯示輸出=True)
        執行檔目錄 = cls._細項目錄(gizapp程式碼目錄, 'bin')
        for 資料夾, 檔名 in [
            ('GIZA++-v2', 'GIZA++'),
            ('GIZA++-v2', 'snt2cooc.out'),
            ('mkcls-v2', 'mkcls'),
        ]:
            copy(join(gizapp程式碼目錄, 資料夾, 檔名), join(執行檔目錄, 檔名))

    @classmethod
    def 安裝mgiza(cls, mgiza安裝路徑=外部程式.目錄()):
        makedirs(mgiza安裝路徑, exist_ok=True)
        mgiza程式碼目錄 = join(mgiza安裝路徑, 'mgiza', 'mgizapp')
        if not isdir(mgiza程式碼目錄):
            with cls._換目錄(mgiza安裝路徑):
                cls._下載專案(
                    'https://github.com/moses-smt/mgiza.git'
                )
        else:
            with cls._換目錄(mgiza程式碼目錄):
                cls._更新專案()
        with cls._換目錄(mgiza程式碼目錄):
            cls._走指令(['cmake', '.'])
            cls._走指令('make', 愛直接顯示輸出=True)
            cls._走指令(['make', 'install'], 愛直接顯示輸出=True)
            copy(
                join('scripts', 'merge_alignment.py'),
                join('bin', 'merge_alignment.py')
            )

    @classmethod
    def _下載專案(cls, 專案git路徑):
        try:
            cls._走指令([
                'git', 'clone',
                '--depth', cls.pull深度,
                專案git路徑
            ])
        except:
            cls._走指令([
                'git', 'clone',
                專案git路徑
            ])

    @classmethod
    def _更新專案(cls):
        try:
            cls._走指令(
                ['git', 'pull', '--depth', cls.pull深度],
                愛直接顯示輸出=True
            )
        except:
            cls._走指令(
                ['git', 'pull'],
                愛直接顯示輸出=True
            )
